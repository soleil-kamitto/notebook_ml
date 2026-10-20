# Mi cuaderno de IA

Estoy aprendiendo inteligencia artificial desde cero, empezando por las matemáticas. Son 24 semanas, 6 días por semana, 7 horas al día. Todo lo programo a mano antes de usar cualquier librería.

Soy Soleil, estudiante de Ingeniería de Sistemas y Computer Science en Lima. Investigo visión por computadora aplicada a microbiología.

Publico un video cada día de la serie "Día X aprendiendo IA desde cero".

Empecé el 19 de octubre de 2026.

---

## Por qué lo hago así

Quiero poder escribir el código yo sola, entender cada línea y saber qué cuesta. No quiero saber usar librerías, quiero saber qué hacen por dentro.

Por eso programo sin autocompletado de IA y cada día anoto si fue un día limpio.

Escribo todo primero en Python puro y después en NumPy, y comparo las dos versiones para ver qué me estaba ahorrando.

Que los tests pasen no significa que aprendí. Tengo que poder explicar cada línea, cuánto cuesta y cómo se optimiza.

Tres veces por semana reescribo de memoria una función que ya resolví, en 20 minutos, sin mirar nada.

---

## El cuaderno

Abro `web/index.html` en el navegador. Es un cuaderno de verdad, tiene tapa, se abre y trae una hoja por cada día de la semana.

Cada hoja me muestra para qué sirve lo que estudio ese día y dónde se usa en la vida real, los videos y lecturas con enlace directo, qué hacer en papel después del video, qué funciones programar y cómo comprobarlas, el guion del video de 1 minuto y un espacio para escribir mis apuntes.

---

## Qué estoy estudiando

| Semanas | Tema |
|---|---|
| 1 a 8 | Matemáticas, álgebra lineal, cálculo, probabilidad y estadística |
| 9 a 16 | Redes neuronales desde cero hasta armar un mini GPT |
| 17 a 24 | Visión por computadora, CNNs, PyTorch e imágenes de microbiología |
| 12 a 24 | Reverse engineering con C, ensamblador y Ghidra, en paralelo |
| 9 a 24 | Agentes y sistemas con modelos de lenguaje, en paralelo |

Esta semana estoy en vectores, combinaciones lineales, transformaciones y producto punto. El viernes programo una neurona a mano.

El plan completo está en `plan/ruta.md`.

---

## De dónde aprendo

[3Blue1Brown, Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) para la intuición.

[Khan Academy](https://www.khanacademy.org/math/linear-algebra) para ejercicios con corrección automática.

[Immersive Math](https://immersivemath.com/ila/index.html), un libro interactivo donde las figuras se mueven.

[Mathematics for Machine Learning](https://mml-book.com), el libro formal, en PDF gratis.

[MIT 18.06 con Gilbert Strang](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/), el curso universitario completo.

[Neural Networks, Zero to Hero de Karpathy](https://karpathy.ai/zero-to-hero.html) para la fase 2.

[picoCTF](https://picoctf.org/) y [crackmes.one](https://crackmes.one/) para reverse engineering.

---

## Cómo corro mis ejercicios

```bash
pip install -r requirements.txt
python -m pytest -v
```

Las funciones vienen vacías y las lleno yo. Esta semana son 24 funciones y 51 tests.

---

## Qué hay en cada carpeta

```
web/index.html     Mi cuaderno, se abre en el navegador
plan/              La ruta de 24 semanas y hacia dónde apunta
semanas/           Qué estudiar cada semana, día por día
ejercicios/        Las funciones que tengo que programar y sus tests
progreso/          Mis horas reales, qué domino y qué me falta
diario/            Un archivo por día con qué aprendí y qué me costó
contenido/         El guion del video de cada día
noticias/          Un script que trae papers filtrados por mi tema
datos/             Protocolo para mis fotos de microscopio
```

---

## Cómo mido si voy bien

`progreso/progreso.json` guarda la verdad, mis horas reales, qué temas domino, cuáles me cuestan y cuántos días estudié sin ayuda de IA.

Un tema cuenta como aprendido solo si pasan sus tests y además puedo explicarlo línea por línea. Si no, vuelve a repaso a los 3, 7 y 21 días.

Cada domingo sale un reporte de la semana.

---

## A dónde quiero llegar

Quiero entender esto a fondo para construir yo misma la infraestructura de mi startup. La idea que más me interesa es la lectura automática de placas y antibiogramas desde la foto de un celular, para laboratorios que no pueden pagar los equipos de cientos de miles de dólares.

Eso está en `plan/posicionamiento.md`.
