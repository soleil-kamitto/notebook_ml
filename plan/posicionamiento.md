# Posicionamiento: de la ruta técnica al mercado

Documento de trabajo. Se revisa al final de cada fase, no antes.

Regla de este archivo: **primero la base técnica, después el mercado.** La ruta de 24 semanas no se recorta para perseguir una oportunidad. Lo que sí hace este documento es apuntar los mini proyectos semanales hacia terreno que después vale dinero, sin cambiar el contenido de estudio.

---

## 1. Qué tengo que nadie más tiene

Esto es lo que define el mercado, no al revés. Mi ventaja no es "saber IA" — eso lo va a tener todo el mundo. Es la intersección:

| Activo | Por qué es raro |
|---|---|
| Computer Vision + microbiología real | Los ingenieros de ML no tienen acceso a muestras, microscopios ni a gente de laboratorio. Los microbiólogos no programan CNNs. La intersección es minúscula. |
| Acceso a laboratorios en Lima | Los datos de microscopía no se compran en Kaggle. El que tiene muestras, tiene el dataset. El dataset es el foso. |
| Bases matemáticas escritas a mano | Cuando el modelo falla raro, el que entiende el gradiente lo arregla; el que solo llama a `.fit()` cambia de librería. |
| Operar en LatAm con costos de LatAm | Puedo vender a precios a los que un competidor de SF no puede bajar. |
| Construyo en público desde el día 1 | 144 días de contenido = distribución y credibilidad antes de tener producto. Casi nadie lo hace con rigor técnico. |

**La pregunta correcta no es "¿qué mercado está de moda?" sino "¿qué problema puedo ver yo que en San Francisco no pueden ver?"** La respuesta vive en un laboratorio de Lima, no en un pitch deck.

---

## 2. Lo que se está construyendo ahora (dato verificado, octubre 2026)

De la investigación de hoy, separado entre lo confirmado y lo que es ruido:

**Señales sólidas:**

- **Lotes recientes de Y Combinator**: el peso de "physical AI" / industriales subió a ~23% del batch, desde ~12.8% del anterior. La ola se mueve de software puro a software que toca materia. Fuente: [análisis del batch S26](https://www.extruct.ai/research/ycx26/).
- **Verticales aburridos con IA**: contratos de HVAC, trabajo no-creativo de estudios de arquitectura, diligencia de private equity, hoteles. Ver [startups de YC W26](https://techcrunch.com/2026/03/26/16-of-the-most-interesting-startups-from-yc-w26-demo-day/). Patrón: el dinero está donde el software nunca llegó, no donde todos miran.
- **Automatización de laboratorios de microbiología**: una [revisión en Frontiers](https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2026.1766429/full) lista como barreras reales el costo de capital, la interoperabilidad y la falta de estándares de interfaz. Esto es exactamente mi terreno.
- **Brecha de costo para laboratorios chicos**: el mercado de automatización de laboratorio crece ~6.6% anual, pero la implementación y el entrenamiento suman hasta 15% al costo total, lo que deja afuera a los laboratorios medianos y chicos. Fuente: [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/lab-automation-market-1158.html). **Ese "afuera" es un mercado.**
- **Fabricación en el espacio**: un [tópico SBIR de NASA para 2026](https://www.sbir.gov/topics/1012241) dice literalmente que el equipamiento actual fue diseñado para investigación en lotes chicos y no para manufactura, y que faltan tecnologías de automatización, control de calidad y repetibilidad. Es demanda escrita por el cliente, con dinero público detrás.
- **Hábitats lunares** aparecieron ya en un batch de YC ([Forbes](https://www.forbes.com/sites/dariashunina/2026/03/16/21-most-promising-startups-from-y-combinators-latest-batch/)). Lo de Marte que viste existe como tesis de inversión, pero no encontré evidencia de un mercado con clientes pagando hoy.

**Lo que no pude verificar, y por eso no planifico sobre eso:** herramientas de construcción específicas para Marte con clientes reales, y datos de financiamiento de imagen para resistencia antimicrobiana. Son hipótesis, no hechos.

**Sobre Inklop** (el caso que mencionaste): plataforma que conecta creadores emergentes con marcas, pago por vista verificada, 70% para el creador, campañas desde ~$85, y una capa de IA que valida el video contra el brief y filtra vistas no humanas. Compite con Insense, Billo y Collabstr. Lo interesante no es el marketplace — es la **verificación**: distinguir una vista humana de una falsa, y comprobar que un video cumple un brief. Eso es un problema de visión por computadora y detección de fraude, o sea mi terreno técnico aplicado a otro sector. Guardá el patrón: *el negocio obvio es el marketplace; el foso técnico es la verificación.*

---

## 3. Dónde apuntar: mercados raros con poca competencia

Ordenados por qué tan bien encajan con lo que voy a saber hacer. No son para elegir hoy: son para probar como mini proyecto cuando llegue la semana.

### A. Microbiología clínica asequible — el más fuerte

**El problema:** identificar bacterias y medir su sensibilidad a antibióticos (antibiograma) toma 24–72 horas y necesita equipos de cientos de miles de dólares. En LatAm la mayoría de los laboratorios no los tiene; leen placas a ojo.

**Lo que yo podría construir:** lectura automática de placas y antibiogramas desde la foto de un celular o un microscopio barato. Medir halos de inhibición, contar colonias, clasificar morfología.

- **Por qué hay poco competidor:** los players grandes venden el instrumento completo, no software para el laboratorio que no puede comprar el instrumento. El mercado "laboratorio chico sin presupuesto" está explícitamente desatendido según el dato de costos de arriba.
- **Mi ventaja:** acceso a muestras, a microbiólogos, y a la realidad de un laboratorio peruano.
- **Dónde empieza:** semana 23 de la ruta (segmentación U-Net). Pero el dataset lo puedo empezar a juntar **desde ya**: fotos etiquetadas de placas, con un protocolo consistente. Eso no requiere saber ML.
- **Por qué importa más allá del dinero:** la resistencia a antibióticos mata, y el diagnóstico lento es parte de la causa.

### B. Visión por computadora para bioprocesos de bajo costo

Fermentadores, biorreactores y producción de alimentos en LatAm: monitorear crecimiento, contaminación y turbidez con una cámara en vez de sensores caros. Los informes de 2026 ponen robótica y IA en bioprocesos como tendencia, pero la oferta apunta a biofarma grande. Cervecerías, lácteos y acuicultura regional no son el cliente de nadie.

### C. Verificación de contenido y de vistas (el ángulo Inklop)

Dado un video y un brief, ¿cumple? Dada una vista, ¿es humana? Es detección de fraude + visión. El mercado de creadores crece y la verificación es el cuello de botella que todos tercerizan. Es más fácil de monetizar rápido y más fácil de copiar: sirve como producto puente, no como la apuesta de fondo.

### D. Inspección visual para minería y agroindustria peruana

Sectores enormes en Perú, software casi inexistente, nadie en SF entiende el contexto ni quiere viajar a una mina. Detección de defectos, conteo, clasificación de calidad. Aburrido, local, pagable.

### E. Datos para robótica fuera de la Tierra (apuesta larga)

El tópico de NASA pide control de calidad y repetibilidad para manufactura en órbita. Eso es inspección visual en condiciones raras: poca luz, microgravedad, sin operador humano. Es la versión de ciencia ficción de lo mismo que haría en una mina. **No se persigue ahora**: se mira de nuevo en la semana 24, con portafolio en mano.

---

## 4. Cómo se cruzan las subáreas (ahí está el foso)

Una habilidad sola es un commodity. Dos cruzadas son defendibles:

| Cruce | Lo que habilita |
|---|---|
| CV + microbiología | Diagnóstico asequible. Nadie puede copiarlo sin acceso a muestras. |
| CV + reverse engineering | Correr modelos en hardware barato o viejo: entender el binario, cuantizar, optimizar. Un laboratorio peruano no tiene una A100. **Esto es el cruce menos obvio y más valioso.** |
| Reverse engineering + GPUs | Leer y escribir kernels. Es lo que separa a quien usa modelos de quien los hace rendir 10x más barato. |
| Agentes + laboratorio | El agente no diagnostica: ordena el trabajo, documenta, hace trazabilidad para el regulador. El valor no está en el modelo, está en el flujo. |
| Construir en público + deep tech | La distribución llega antes que el producto. Cuando tenga algo que vender, ya hay quien escuche. |

El cruce que más protege es **CV + reverse engineering**: en LatAm el costo de cómputo es la barrera real, y casi nadie que sepa de modelos sabe además optimizarlos a nivel de hardware. Por eso la fase 4 no es un hobby.

---

## 5. Qué hago distinto desde esta semana (sin cambiar el estudio)

Tres cosas, que cuestan casi nada:

1. **Empezar el dataset ahora.** Cada visita a un laboratorio, fotos de placas con protocolo fijo: misma distancia, misma luz, etiqueta de qué es. Carpeta `datos/` fuera de git si son sensibles. Para la semana 22 tendré algo que nadie puede descargar.
2. **Cada mini proyecto del viernes, con datos propios cuando se pueda.** La regresión de la semana 4 sobre una medición real de laboratorio en vez de datos de juguete. Mismo contenido técnico, portafolio distinto.
3. **Un cuaderno de problemas.** `plan/problemas.md`: cada vez que alguien de un laboratorio se queja de algo, se anota literal, con fecha y quién lo dijo. Las startups buenas salen de esa lista, no de un brainstorming. **Diez quejas textuales valen más que cien ideas.**

---

## 6. Revisiones del plan

- **Fin de fase 1 (semana 8):** ¿sigo creyendo en el mercado A? ¿cuántas quejas tengo anotadas?
- **Fin de fase 2 (semana 16):** primer prototipo feo de lectura de placas, con mi propio código.
- **Fin de fase 3 (semana 24):** pipeline real, métricas honestas, y 3 conversaciones con laboratorios que pagarían.

---

## 7. Lo que no voy a hacer

- Fundar antes de tener la base técnica. Una startup de deep tech con fundadora que no entiende su modelo se muere en la primera pregunta técnica de un inversionista o en el primer caso raro en producción.
- Perseguir el mercado de moda. Cuando algo es tendencia en SF, la ventana de entrada sin capital ya se cerró.
- Elegir un mercado por raro. Se elige por **acceso**: un problema que yo puedo ver y otros no.
- Creer que "poca competencia" es siempre buena señal. A veces no hay competencia porque no hay dinero. La forma de distinguirlo es hablar con diez clientes, no leer informes.
