# Semana 2 — Determinante, inversa, rango y espacio nulo

**Fase 1 · semana 2 de 24 · 2026-10-26 al 2026-10-31**

Al final de esta semana tengo que poder resolver `Ax = b` a mano con eliminación de Gauss, y decir **antes de calcular** si el sistema tiene una solución, infinitas o ninguna, mirando la matriz.

---

## Por qué este orden

La semana 1 fue qué hace una matriz. Esta semana es **cuándo se puede deshacer**. Importa para ML porque entrenar es resolver sistemas: cuando una matriz no tiene inversa, el modelo tiene infinitas soluciones igual de buenas, y ahí aparecen la regularización y los problemas mal condicionados. El rango es, literalmente, cuánta información distinta hay en mis datos.

---

## Día por día

### Lunes — El determinante
- **Video:** [Cap. 6 · El determinante](https://www.youtube.com/watch?v=Ip3X9LOh2dk)
- **Lectura:** MML 4.1
- **Debo poder:** explicar el determinante como factor de área o volumen, y qué significa que sea 0 o negativo.

### Martes — Matrices inversas, rango y espacio nulo
- **Video:** cap. 7 · Matrices inversas, espacio columna y espacio nulo — buscarlo en la [playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (no pude verificar el enlace directo)
- **Lectura:** MML 2.8
- **Debo poder:** decir qué vectores manda una matriz al origen, y por qué eso es el espacio nulo.

### Miércoles — Matrices no cuadradas
- **Video:** cap. 8 · Matrices no cuadradas como transformaciones entre dimensiones — mismo [playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- **Debo poder:** explicar qué hace una matriz de 3×2 y qué una de 2×3.

### Jueves — Eliminación de Gauss
- **Lectura:** MML 2.3 (resolución de sistemas) y 2.4.
- **Debo poder:** llevar una matriz a forma escalonada a mano, en papel, sin equivocarme en los signos.

### Viernes — Mini proyecto: resolver `Ax = b`
- Eliminación de Gauss con pivoteo parcial, en Python puro.
- Después `numpy.linalg.solve` y comparar: resultados, tiempo y qué pasa con una matriz casi singular.
- **Debo poder:** explicar por qué el pivoteo parcial existe y qué se rompe sin él.

### Sábado — Repaso, publicar, grabar
Más reverse engineering no: eso arranca en la semana 12.

---

## Preguntas que cierran la semana

1. ¿Por qué una matriz con determinante 0 no tiene inversa?
2. Si el rango de una matriz 3×3 es 2, ¿qué le pasó al espacio?
3. ¿Cómo se relacionan el rango y el espacio nulo? (teorema del rango-nulidad, pero explicado con las manos)
4. En `Ax = b`, ¿qué significa geométricamente que no haya solución?
5. ¿Por qué en ML una matriz "casi" singular es más peligrosa que una singular?

(La 5 es la que importa: la singular falla fuerte y se nota; la casi singular da resultados que parecen bien y están mal.)

---

## Nota del tutor

Los esqueletos de `ejercicios/semana_02/` y sus tests se crean **el lunes 2026-10-26**, no antes. Ver una función vacía de un tema que todavía no estudié no ayuda: adelanta la respuesta y quita la sorpresa de descubrir qué hay que hacer.
