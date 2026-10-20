# Ruta completa — 24 semanas

Inicio: **2026-10-19**. Lunes a sábado, domingo descanso. 7 h/día: 4 h teoría, 3 h práctica, 1 h contenido.

Regla transversal: **nada se usa de una librería antes de haberlo programado a mano**. Si no puedo escribir la versión lenta, no tengo derecho a la rápida.

---

## Fase 1 · Matemáticas para ML (semanas 1–8)

Fuentes base: 3Blue1Brown [*Essence of Linear Algebra*](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) y [*Essence of Calculus*](https://www.3blue1brown.com/topics/calculus); libro [*Mathematics for Machine Learning*](https://mml-book.com) (MML), PDF gratis.

| Sem | Tema | Video / lectura | Mini proyecto del viernes |
|---|---|---|---|
| 1 | Vectores, span, transformaciones, producto punto | EoLA caps. 1–4 y 9 · MML 2.1–2.7, 3.1–3.2 | **Una neurona a mano**: `y = f(w·x + b)` en Python puro y en NumPy |
| 2 | Determinante, inversa, rango, espacio nulo | EoLA caps. 5–8 · MML 2.8, 4.1 | Resolver `Ax = b` con eliminación de Gauss escrita por mí |
| 3 | Producto punto, cambio de base, eigen | EoLA caps. 9–14 · MML 4.2–4.5 | Potencia iterada: encontrar el eigenvector dominante sin `numpy.linalg` |
| 4 | Proyecciones, mínimos cuadrados, SVD | EoLA cap. 15–16 · MML 3.6–3.8, 4.5 | **Regresión lineal por mínimos cuadrados**, con ecuación normal a mano |
| 5 | Derivadas, regla de la cadena | EoC caps. 1–4 · MML 5.1–5.2 | Derivada numérica vs. analítica: medir el error |
| 6 | Gradientes, derivadas parciales, jacobiano | EoC caps. 5–8 · MML 5.3–5.6 | **Descenso de gradiente a mano** sobre la regresión de la semana 4 |
| 7 | Probabilidad, Bayes, distribuciones | MML 6.1–6.5 | Clasificador Naive Bayes desde cero sobre texto corto |
| 8 | Estadística, máxima verosimilitud, entropía | MML 6.6–6.7, 8.1–8.3 | **Cierre de fase**: ajustar una distribución por MLE y graficar la verosimilitud |

Entregable de fase: un repo `fundamentos-ml` con mi propia mini librería de álgebra lineal y optimización, con tests y README.

**Puerta de salida de la fase 1** (no se avanza sin esto): puedo derivar a mano la regla de la cadena para una composición de 3 funciones, y explicar por qué el gradiente apunta en la dirección de máximo ascenso.

---

## Fase 2 · Redes neuronales desde cero (semanas 9–16)

Fuente base: Andrej Karpathy, [*Neural Networks: Zero to Hero*](https://karpathy.ai/zero-to-hero.html) · [notebooks](https://github.com/karpathy/nn-zero-to-hero).

| Sem | Tema | Clase | Mini proyecto del viernes |
|---|---|---|---|
| 9 | Backprop a mano, grafo de cómputo | micrograd | **Mi propio micrograd**: clase `Valor` con `backward()` |
| 10 | MLP, pérdida, entrenamiento | micrograd (cierre) | MLP que aprende XOR, entrenado con mi micrograd |
| 11 | Modelo de lenguaje por bigramas, one-hot | makemore 1 | Generador de nombres por conteo y por red de 1 capa |
| 12 | MLP para lenguaje, embeddings | makemore 2 | Embeddings entrenados, visualizados en 2D |
| 13 | Activaciones, BatchNorm, inicialización | makemore 3 | Diagnosticar una red muerta: histogramas de activación y gradiente |
| 14 | Backprop manual sobre un MLP completo | makemore 4 | Derivar y verificar todos los gradientes sin autograd |
| 15 | WaveNet, jerarquías, capas | makemore 5 | Red jerárquica para nombres, comparada contra el MLP plano |
| 16 | Atención y Transformer | **nanoGPT** | **Mini GPT a nivel carácter** entrenado en texto propio |

**Puerta de salida**: puedo escribir en una pizarra, de memoria, el paso forward y backward de la atención con una sola cabeza.

---

## Fase 3 · Computer Vision (semanas 17–24)

Fuentes: papers + [tutoriales de PyTorch](https://pytorch.org/tutorials/) + [Hugging Face Papers](https://huggingface.co/papers) + mis propias imágenes de microbiología.

| Sem | Tema | Mini proyecto del viernes |
|---|---|---|
| 17 | Imágenes como tensores, convolución a mano | Convolución 2D con bucles: bordes, blur, Sobel, sin OpenCV |
| 18 | CNN desde cero, pooling, padding | CNN de 2 capas sobre MNIST, entrenada con mi backprop |
| 19 | PyTorch de verdad: tensores, autograd, `nn.Module` | La misma CNN en PyTorch, comparando tiempos y resultados |
| 20 | Datos, augmentación, overfitting | Pipeline de datos propio con augmentación y validación honesta |
| 21 | Arquitecturas: ResNet, skip connections | ResNet pequeña implementada desde el paper |
| 22 | Transfer learning y fine-tuning | **Clasificador de imágenes de microbiología** con fine-tuning |
| 23 | Segmentación: U-Net, métricas IoU/Dice | Segmentar células o colonias en mis propias imágenes |
| 24 | Evaluación, errores, publicación | **Proyecto final**: pipeline completo + README + video + paper corto |

**Puerta de salida**: un proyecto de CV sobre datos reales de microbiología, con métricas honestas, análisis de errores y limitaciones escritas.

---

## Fase 4 · Reverse engineering (semanas 12–24, en paralelo)

3–4 h por semana, sábados. Fuentes: [picoCTF](https://picoctf.org/), [crackmes.one](https://crackmes.one/), [Ghidra](https://ghidra-sre.org/).

| Sem | Tema |
|---|---|
| 12–13 | C: punteros, memoria, structs, compilación |
| 14–15 | Ensamblador x86-64: registros, stack, convención de llamada |
| 16–17 | Leer desensamblado: `objdump`, `gdb` |
| 18–19 | Ghidra: navegar binarios, renombrar, decompilar |
| 20–21 | Retos de reversing de picoCTF, de menor a mayor |
| 22–24 | Crackmes reales + escribir un write-up por cada uno |

Por qué está aquí: entender qué hace la máquina por debajo es lo que separa a quien usa modelos de quien los optimiza. Es también la base para leer kernels CUDA más adelante.

---

## Fase 5 · Agentes y sistemas con LLMs (en paralelo desde la semana 9)

2 h por semana, dentro del bloque de contenido. No reemplaza la fase matemática: se construye **sobre** ella.

| Sem | Tema |
|---|---|
| 9–11 | Llamadas a la API, prompting, tool use, costos y límites |
| 12–14 | Un agente propio con bucle de herramientas, escrito a mano |
| 15–17 | Evaluación de agentes: casos de prueba, métricas, regresiones |
| 18–20 | RAG honesto: embeddings, recuperación, medición de la mejora |
| 21–24 | Un agente que haga algo útil para mi investigación de CV |

Los agentes del tutor en la carpeta de agentes son el primer laboratorio: los uso y los modifico.

---

## Cómo se mide el avance

- `progreso/progreso.json`: temas, estado (`pendiente` / `debil` / `dominado`), horas reales, fechas.
- Tests en `ejercicios/tests/` por semana. Un tema no está dominado hasta que pasan **y** respondo las preguntas del tutor.
- Reporte cada domingo en `progreso/`.
- Un video por día. Si no puedo explicarlo en un minuto, no lo entendí.
