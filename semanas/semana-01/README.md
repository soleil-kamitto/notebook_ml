# Semana 1 — Álgebra lineal: del vector a la neurona

**Fase 1 · semana 1 de 24 · 2026-10-19 al 2026-10-24**

Al final de esta semana tengo que poder escribir, sin mirar nada, una neurona que calcule `y = f(w·x + b)` y explicar qué significa geométricamente cada parte.

---

## Por qué este orden

El producto punto **es** la operación de una neurona. Todo lo anterior existe para que el viernes entienda qué estoy calculando y no solo cómo:

- Un **vector** es la entrada `x` y también los pesos `w`.
- Una **combinación lineal** es exactamente `w₁x₁ + w₂x₂ + ...`.
- Una **transformación lineal** es lo que hace una capa entera de neuronas.
- El **producto punto** mide cuánto se parece `x` a `w`: eso es lo que una neurona detecta.

---

## Día por día

### Lunes — Vectores
- **Video:** [Cap. 1 · Vectores, ¿qué son realmente?](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- **Lectura:** MML 2.1–2.2
- **Código:** `ejercicios/semana_01/vectores.py`
- **Debo poder:** sumar y escalar vectores a mano y dibujar el resultado; explicar las tres formas de ver un vector (flecha, lista de números, elemento de un espacio).

### Martes — Combinaciones lineales, span y base
- **Video:** [Cap. 2 · Combinaciones lineales, span y vectores base](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- **Lectura:** MML 2.5
- **Código:** `ejercicios/semana_01/span.py`
- **Debo poder:** decir si dos vectores son linealmente dependientes mirándolos; explicar qué es el span de dos vectores en 3D.

### Miércoles — Transformaciones lineales y matrices
- **Video:** [Cap. 3 · Transformaciones lineales y matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- **Lectura:** MML 2.7
- **Código:** `ejercicios/semana_01/transformaciones.py`
- **Herramienta:** el laboratorio de matrices en `web/index.html` — escribo la matriz, comparo con lo que calculé a mano.
- **Debo poder:** leer una matriz 2×2 y decir a dónde manda î y ĵ; aplicarla a un vector sin calculadora.

### Jueves — Composición y producto punto
- **Videos:** [Cap. 4 · Multiplicación de matrices como composición](https://www.youtube.com/watch?v=XkY2DOUCWMU) y [Cap. 9 · Producto punto y dualidad](https://www.youtube.com/watch?v=LyGKycYT2v0)
- **Lectura:** MML 3.1–3.2
- **Código:** `ejercicios/semana_01/producto_punto.py`
- **Debo poder:** explicar por qué `AB ≠ BA` en términos de transformaciones; explicar el producto punto como proyección.

### Viernes — Mini proyecto: una neurona a mano
- **Sin video nuevo.**
- **Código:** `ejercicios/semana_01/neurona.py`
- Primero en Python puro, reusando mi `producto_punto`. Después la versión `_np` en NumPy.
- **Debo poder:** decir qué hace `b` geométricamente, y qué pasa si quito la activación.

### Sábado — Repaso, publicar, grabar
- Volver a lo que costó (lo que quedó `debil` en `progreso.json`).
- Subir el mini proyecto a GitHub con README propio.
- Grabar el video de la semana.

### Domingo — Descanso
El reporte semanal se genera solo en `progreso/`.

---

## Cómo corro mis ejercicios

```bash
python -m pytest ejercicios/tests/test_semana_01.py -v
```

O dentro de el tutor: `/check`

Las funciones están vacías con un `raise NotImplementedError`. Las lleno yo. el tutor no las toca.

---

## Las preguntas que cierran la semana

Si no puedo responder estas cinco sin mirar, la semana no está terminada aunque los tests pasen:

1. ¿Por qué el producto punto de dos vectores perpendiculares es cero?
2. ¿Qué significa que el determinante de una matriz sea negativo?
3. Si una matriz 2×2 manda todo el plano a una línea, ¿qué pasó con su determinante y con su rango?
4. En `y = f(w·x + b)`, ¿qué controla `w` y qué controla `b`?
5. ¿Por qué una red sin función de activación, con muchas capas, es equivalente a una sola capa?

(La 5 es la que importa. Si sale sola, entendí la semana.)
