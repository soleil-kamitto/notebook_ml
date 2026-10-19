# Aprendiendo IA desde cero

Espacio de estudio a tiempo completo de **Soleil** — estudiante de Ingeniería de Sistemas y Computer Science en Lima, investigadora de Computer Vision aplicada a microbiología.

Objetivo: dominar **machine learning, inteligencia artificial y reverse engineering desde las bases matemáticas**, en 24 semanas, programando todo a mano antes de usar librerías, y documentando el avance en público.

Objetivo final, declarado: **poder programar sin IA, entender cada línea y saber qué cuesta**, para construir yo misma la infraestructura de mi startup.

Serie de contenido: **"Día X aprendiendo IA desde cero"**. Inicio: 2026-10-19.

---

## La regla principal

Este repo trabaja con Claude Code en **modo tutor, no en modo programador**.

- Claude **nunca** escribe la solución de un ejercicio.
- Si pido ayuda, recibo **pistas, preguntas o la explicación del concepto**.
- La solución solo aparece si escribo exactamente: `me rindo`.
- Un test que pasa **no** es un tema aprendido: hay que defenderlo línea por línea.

Las reglas completas viven en [CLAUDE.md](CLAUDE.md) para que se respeten en cada sesión.

### Modo sin IA

- Los ejercicios se escriben con **autocompletado de IA apagado**. Se registra cada día en `progreso.json`.
- Tres veces por semana, **retos en blanco**: reescribir de memoria, 20 minutos, sin mirar nada.
- Cada función a mano se compara con su versión NumPy, se mide con `time.perf_counter()` y se explica de dónde sale la diferencia.

---

## Tablero de estudio

[`web/index.html`](web/index.html) — se abre en el navegador y muestra qué toca hoy con el enlace exacto, un laboratorio de matrices editable para verificar los cálculos a mano, y los comandos por síntoma.

---

## Ruta de estudio

| Fase | Semanas | Tema | Fuentes base |
|---|---|---|---|
| 1 | 1–8 | Matemáticas para ML: álgebra lineal, cálculo, probabilidad y estadística | [3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) · [Mathematics for Machine Learning](https://mml-book.com) |
| 2 | 9–16 | Redes neuronales desde cero: de micrograd a un mini GPT | [Karpathy, Zero to Hero](https://karpathy.ai/zero-to-hero.html) |
| 3 | 17–24 | Computer Vision: CNNs, PyTorch, proyectos con imágenes de microbiología | papers + proyectos propios |
| 4 | 12–24 (en paralelo) | Reverse engineering: C, ensamblador x86, Ghidra | [picoCTF](https://picoctf.org/) · [crackmes.one](https://crackmes.one/) |
| 5 | 9–24 (en paralelo) | Agentes y sistemas con LLMs, sobre la base matemática | API, evaluación, RAG medido |

Todo en fase 1 se programa **primero en Python puro y después en NumPy**, para entender el cálculo antes de delegarlo.

Cada semana cierra con un **mini proyecto** publicable en GitHub y mostrable en video.

**Semana 1:** vectores, combinaciones lineales, transformaciones lineales, producto punto y multiplicación de matrices → el viernes, una **neurona programada a mano**. Detalle en [semanas/semana-01/README.md](semanas/semana-01/README.md).

Ruta completa en [plan/ruta.md](plan/ruta.md). Hacia dónde apunta todo esto: [plan/posicionamiento.md](plan/posicionamiento.md).

---

## Rutina diaria

Lunes a sábado. Domingo descanso.

| Horario | Bloque |
|---|---|
| 08:00 – 12:00 | Estudio profundo (teoría, video, lectura) |
| 14:00 – 17:00 | Práctica (ejercicios, código, proyecto) |
| 19:00 – 20:00 | Contenido (grabar y publicar) |

---

## Comandos

| Comando | Qué hace |
|---|---|
| `/hoy` | Qué estudiar hoy según mi progreso: el video o lectura exacta y los ejercicios |
| `/check` | Corre los tests y dice qué pasa y qué falla — **sin dar la respuesta** |
| `/explicar <tema>` | Explica un concepto con analogías y luego me hace 3 preguntas |
| `/defender <tema>` | Me examina línea por línea: qué hace, qué cuesta, cómo se optimiza. Decide si el tema queda dominado |
| `/reto` | Reto en blanco: reescribir de memoria una función ya resuelta, 20 minutos, sin mirar |
| `/cierre` | Guarda el diario, actualiza `progreso.json` y propone la idea de video del día |
| `/semana` | Horas, temas dominados, temas débiles y si voy atrasada |
| `/noticias` | Trae papers filtrados por mis temas y guarda el resumen del día |

## Agentes

En [.claude/agents/](.claude/agents/). Son también mi primer laboratorio de la fase 5: los uso y los modifico.

| Agente | Para qué |
|---|---|
| `tutor-socratico` | Pistas sin solución. **Sin permiso de escritura**, así no puede resolver el ejercicio ni por accidente |
| `examinador` | La defensa oral: línea por línea, complejidad, bordes, optimización |
| `revisor-codigo` | Busca atajos, código que funciona por casualidad y complejidad de más. Señala, no arregla |
| `curador-papers` | Filtra papers según el tema de la semana. Máximo 5, descarta el resto |
| `guionista` | El guion del video de 1 minuto, a partir del diario del día |

---

## Estructura

```
plan/ruta.md              Ruta completa por fases
plan/posicionamiento.md   Hacia qué mercados apunta todo esto
semanas/semana-NN/        README del tema, recursos y ejercicios de la semana
ejercicios/semana_NN/     Funciones vacías con docstrings, para completar yo
ejercicios/tests/         Tests pytest (los escribe el tutor, no se tocan)
ejercicios/retos-en-blanco/  Reescrituras de memoria, cronometradas
progreso/                 progreso.json y reportes semanales
diario/                   Un archivo por día: qué aprendí, qué me costó
noticias/                 traer.py (RSS, sin claves de API) + resúmenes diarios
contenido/                Una idea de video por día: gancho, explicación, qué muestro
web/index.html            Tablero de estudio
CLAUDE.md                 Reglas permanentes del tutor
.claude/commands/         Comandos slash
.claude/agents/           Agentes especializados
```

---

## Cómo corro los ejercicios

```bash
pip install -r requirements.txt
python -m pytest -v                      # todo
python -m pytest -v -k lunes             # solo el día que toca
```

Las funciones llegan vacías con `raise NotImplementedError`. Las lleno yo.

---

## Monitoreo

`progreso/progreso.json` es la fuente de verdad: temas completados, fechas, horas reales y días limpios sin IA.

- Un tema pasa a `dominado` solo si **pasa los tests y la defensa**. Si no, queda `debil`.
- Los temas débiles vuelven a repaso a los **3, 7 y 21 días** (repetición espaciada).
- Si me salto días o me atraso, el tutor **me lo dice directo** y reajusta el calendario — sin hacer el contenido más liviano.
- Cada domingo: reporte semanal automático en `progreso/`.

---

## Noticias

`noticias/traer.py` lee 11 fuentes con RSS, sin claves de API: arXiv (cs.CV, cs.LG, cs.AI), Hacker News, Import AI, y los blogs de NVIDIA, OpenAI, Google DeepMind, Google Research, Hugging Face y BAIR. Filtra por mis palabras clave **y** por el tema de la semana según `progreso.json`.

```bash
python noticias/traer.py            # filtrado
python noticias/traer.py --todo     # sin filtrar
```

Anthropic y Meta AI quedaron fuera: sus feeds devuelven 404. El feed de arXiv cs.AI suele venir vacío porque sus papers aparecen cruzados en cs.CV y cs.LG.
