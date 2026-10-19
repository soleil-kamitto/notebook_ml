# Datos propios

**Las imágenes no se suben a git.** `.gitignore` las excluye. Acá solo viven el protocolo y el catálogo.

Por qué esta carpeta existe desde la semana 1 y no desde la 22: el dataset es el único activo que no se puede copiar. Un competidor replica mi modelo en una tarde; mis muestras, no. Juntar datos no requiere saber ML, así que empieza ya.

---

## Protocolo de captura

Si las condiciones cambian entre fotos, el modelo aprende la iluminación en vez de la biología. La consistencia vale más que la cantidad.

| Variable | Regla |
|---|---|
| Distancia | Fija. Marcar la altura con cinta o un soporte, y anotar los centímetros. |
| Luz | La misma fuente, siempre. Sin flash. Sin sombra de mi mano encima. |
| Fondo | Uniforme, del mismo color en todas las tomas. |
| Encuadre | La placa completa dentro del cuadro, centrada. |
| Enfoque | Manual si el equipo lo permite. Foto borrosa se descarta, no se "arregla" después. |
| Escala | Una referencia física visible en el cuadro (regla, moneda, marca de tamaño conocido). Sin escala, no se pueden medir halos. |
| Formato | El original sin comprimir. Nunca una captura de pantalla ni una foto reenviada por WhatsApp. |

**Cada foto necesita 3 tomas** de la misma muestra, movidas un poco. Eso da augmentación real, no sintética.

## Nombre de archivo

```
AAAA-MM-DD_<muestra>_<condicion>_<n>.jpg
2026-10-19_ecoli-01_amoxi-10ug_1.jpg
```

Sin tildes, sin ñ, sin espacios.

## Etiquetas

Una fila por foto en `datos/catalogo.csv`, llenado el mismo día:

```
archivo,fecha,muestra,organismo,condicion,medio,horas_incubacion,escala_mm_px,etiqueta,quien_etiqueto,notas
```

`etiqueta` es lo que quiero que el modelo prediga (conteo de colonias, diámetro del halo en mm, clase morfológica). **La etiqueta la pone un microbiólogo, no yo sola** — y se anota quién la puso. Si dos personas discrepan, se guardan las dos opiniones; ese desacuerdo es información sobre la dificultad real del problema.

## Lo que no se hace

- No inventar etiquetas por lo que "parece".
- No borrar las fotos difíciles o raras: son las que importan.
- No mezclar tomas de distintas condiciones en la misma carpeta sin registrarlo.
- No tocar imágenes con datos de pacientes. Si vienen de muestras clínicas: sin identificadores, nunca, y consentimiento de quien las cede por escrito antes de capturar nada.

## Estado

| Fecha | Muestras | Fotos | Etiquetadas |
|---|---|---|---|
| 2026-10-19 | 0 | 0 | 0 |
