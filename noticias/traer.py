"""Trae noticias y papers de IA desde fuentes con RSS o API gratuita.

Uso:
    python noticias/traer.py                 # filtrado por palabras clave + tema de la semana
    python noticias/traer.py --todo           # sin filtrar
    python noticias/traer.py --max 40         # mas candidatos
    python noticias/traer.py --fuente arxiv   # una sola fuente

Imprime JSON por stdout. El comando /noticias toma esa salida y escribe el
resumen en noticias/AAAA-MM-DD.md.

Este archivo es infraestructura, no un ejercicio: el tutor puede modificarlo.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree

RAIZ = Path(__file__).resolve().parent.parent
PROGRESO = RAIZ / "progreso" / "progreso.json"

TIMEOUT = 20
# Un agente con parentesis lo rechazan varios feeds (hnrss entre ellos).
AGENTE = "Mozilla/5.0 (compatible; aprendiendo-ia-desde-cero/1.0)"
PAUSA = 0.6  # segundos entre pedidos: arxiv devuelve el feed vacio si se lo apura

# Fuentes RSS o Atom, todas verificadas el 2026-10-19. Nada que necesite clave de API.
# Anthropic y Meta AI quedaron fuera: sus feeds devuelven 404 y no publican uno.
FUENTES = {
    "arxiv_cv": "https://rss.arxiv.org/rss/cs.CV",
    "arxiv_lg": "https://rss.arxiv.org/rss/cs.LG",
    "arxiv_ai": "https://rss.arxiv.org/rss/cs.AI",
    # hnrss devuelve 502 con consultas largas (OR multiples). Una sola palabra aguanta.
    "hn": "https://hnrss.org/newest?q=AI&points=80",
    "import_ai": "https://jack-clark.net/feed/",
    "nvidia": "https://blogs.nvidia.com/feed/",
    "openai": "https://openai.com/news/rss.xml",
    "deepmind": "https://deepmind.google/blog/rss.xml",
    "huggingface": "https://huggingface.co/blog/feed.xml",
    "google_research": "https://research.google/blog/rss/",
    "bair": "https://bair.berkeley.edu/blog/feed.xml",
}

# Mis intereses permanentes.
CLAVES = [
    "computer vision", "vision", "image", "imaging", "segmentation", "detection",
    "microscopy", "microbiolog", "cell", "bacteria", "biomedical", "medical imaging",
    "histopatholog", "diagnosis",
    "cnn", "convolution", "transformer", "attention", "diffusion", "vit",
    "gpu", "cuda", "kernel", "chip", "inference", "quantization", "training efficiency",
    "latin america", "peru", "brazil", "mexico",
    "dataset", "benchmark", "open source", "open weights",
]

# Palabras clave extra segun el tema de la semana, para que lo de hoy aparezca.
POR_TEMA = {
    "algebra": ["matrix", "linear", "vector", "eigen", "dot product", "svd", "projection"],
    "calculo": ["gradient", "derivative", "optimization", "backprop", "jacobian"],
    "probabilidad": ["bayes", "probabilistic", "uncertainty", "likelihood", "distribution"],
    "red": ["neural network", "mlp", "backprop", "activation", "initialization"],
    "lenguaje": ["language model", "tokenizer", "embedding", "gpt", "attention"],
    "vision": ["cnn", "resnet", "unet", "segmentation", "augmentation", "pretraining"],
    "reverse": ["binary", "disassembl", "decompil", "reverse engineering", "assembly"],
}


def sin_tildes(texto: str) -> str:
    base = unicodedata.normalize("NFD", texto)
    return "".join(c for c in base if unicodedata.category(c) != "Mn").lower()


def limpiar_html(texto: str) -> str:
    texto = re.sub(r"<[^>]+>", " ", texto or "")
    texto = texto.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    texto = texto.replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", texto).strip()


def tema_de_la_semana() -> str:
    """Devuelve el tema de la semana actual segun progreso.json, o cadena vacia."""
    try:
        datos = json.loads(PROGRESO.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""
    semana = str(datos.get("semana_actual", ""))
    return datos.get("semanas", {}).get(semana, {}).get("tema", "")


def claves_activas(tema: str) -> list[str]:
    tema_norm = sin_tildes(tema)
    extra: list[str] = []
    for gatillo, palabras in POR_TEMA.items():
        if gatillo in tema_norm:
            extra.extend(palabras)
    return CLAVES + extra


def descargar(url: str) -> bytes | None:
    """Descarga el feed. Descomprime gzip: varios servidores lo mandan igual."""
    pedido = urllib.request.Request(
        url,
        headers={
            "User-Agent": AGENTE,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
            "Accept-Encoding": "gzip, identity",
        },
    )
    try:
        with urllib.request.urlopen(pedido, timeout=TIMEOUT) as respuesta:
            datos = respuesta.read()
            codificacion = (respuesta.headers.get("Content-Encoding") or "").lower()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None

    if "gzip" in codificacion or datos[:2] == b"\x1f\x8b":
        try:
            datos = gzip.decompress(datos)
        except (OSError, EOFError, gzip.BadGzipFile):
            return None
    return datos


def parsear(xml: bytes, fuente: str) -> list[dict]:
    """Extrae items de un feed RSS 2.0 o Atom sin depender de feedparser."""
    try:
        raiz = ElementTree.fromstring(xml)
    except ElementTree.ParseError:
        return []

    items: list[dict] = []
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    nodos = raiz.findall(".//item")
    if nodos:  # RSS
        for nodo in nodos:
            items.append({
                "fuente": fuente,
                "titulo": limpiar_html(nodo.findtext("title", "")),
                "enlace": (nodo.findtext("link", "") or "").strip(),
                "fecha": (nodo.findtext("pubDate", "") or "").strip(),
                "resumen": limpiar_html(nodo.findtext("description", ""))[:600],
            })
        return items

    for nodo in raiz.findall(".//atom:entry", ns):  # Atom
        enlace = ""
        etiqueta = nodo.find("atom:link", ns)
        if etiqueta is not None:
            enlace = etiqueta.get("href", "")
        items.append({
            "fuente": fuente,
            "titulo": limpiar_html(nodo.findtext("atom:title", "", ns)),
            "enlace": enlace.strip(),
            "fecha": (nodo.findtext("atom:updated", "", ns) or "").strip(),
            "resumen": limpiar_html(
                nodo.findtext("atom:summary", "", ns) or nodo.findtext("atom:content", "", ns)
            )[:600],
        })
    return items


def puntuar(item: dict, claves: list[str]) -> tuple[int, list[str]]:
    texto = sin_tildes(item["titulo"] + " " + item["resumen"])
    encontradas = [c for c in claves if c in texto]
    puntos = len(encontradas)
    # El titulo pesa el doble: una clave en el titulo dice mas que una en el resumen.
    titulo = sin_tildes(item["titulo"])
    puntos += sum(1 for c in encontradas if c in titulo)
    return puntos, encontradas


def main() -> int:
    ap = argparse.ArgumentParser(description="Trae noticias de IA filtradas.")
    ap.add_argument("--todo", action="store_true", help="no filtrar por palabras clave")
    ap.add_argument("--max", type=int, default=25, help="maximo de items a devolver")
    ap.add_argument("--fuente", help="traer solo una fuente (nombre de FUENTES)")
    args = ap.parse_args()

    fuentes = FUENTES
    if args.fuente:
        if args.fuente not in FUENTES:
            print(
                json.dumps({"error": f"fuente desconocida: {args.fuente}",
                            "disponibles": sorted(FUENTES)}, ensure_ascii=False),
            )
            return 2
        fuentes = {args.fuente: FUENTES[args.fuente]}

    tema = tema_de_la_semana()
    claves = claves_activas(tema)

    crudos: list[dict] = []
    fallaron: list[str] = []
    for indice, (nombre, url) in enumerate(fuentes.items()):
        if indice:
            time.sleep(PAUSA)
        xml = descargar(url)
        if xml is None:
            fallaron.append(nombre)
            continue
        obtenidos = parsear(xml, nombre)
        if not obtenidos:
            fallaron.append(nombre)
        crudos.extend(obtenidos[:30])

    # Quitar duplicados por enlace.
    vistos: set[str] = set()
    unicos: list[dict] = []
    for item in crudos:
        clave = item["enlace"] or item["titulo"]
        if clave and clave not in vistos:
            vistos.add(clave)
            unicos.append(item)

    if args.todo:
        seleccion = unicos[: args.max]
    else:
        puntuados = []
        for item in unicos:
            puntos, encontradas = puntuar(item, claves)
            if puntos:
                item = dict(item, puntos=puntos, claves=encontradas[:6])
                puntuados.append(item)
        puntuados.sort(key=lambda x: x["puntos"], reverse=True)
        seleccion = puntuados[: args.max]

    salida = {
        "generado": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "tema_de_la_semana": tema,
        "fuentes_consultadas": len(fuentes),
        "fuentes_sin_respuesta": fallaron,
        "candidatos": len(unicos),
        "devueltos": len(seleccion),
        "items": seleccion,
    }
    print(json.dumps(salida, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
