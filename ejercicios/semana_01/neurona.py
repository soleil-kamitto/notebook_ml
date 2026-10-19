"""Semana 1 · viernes — Mini proyecto: una neurona a mano.

Sin video nuevo. Esto se construye con el producto punto del jueves.

    y = f(w . x + b)

    x = entrada          (lo que la neurona ve)
    w = pesos            (que le importa a la neurona)
    b = sesgo            (cuanto le cuesta activarse)
    f = activacion       (la no linealidad, lo que hace que apilar capas sirva)

Orden de trabajo: primero todo en Python puro reusando producto_punto, despues
las versiones _np, y recien entonces comparar.
"""

from .producto_punto import producto_punto


def escalon(z):
    """Activacion escalon: 1.0 si z > 0, si no 0.0.

    La activacion original del perceptron de 1958. No se usa hoy porque su
    derivada es cero en todas partes, asi que no se puede entrenar con gradiente.
    """
    raise NotImplementedError


def sigmoide(z):
    """Activacion sigmoide: 1 / (1 + e^(-z)).

    Aplasta cualquier numero real al intervalo (0, 1), asi que se puede leer
    como probabilidad.

    Cuidado con el overflow: e^(710) no cabe en un float. Para z muy negativo
    hay que reescribir la formula de otra manera algebraicamente equivalente.
    Pensar como, no envolver en try/except.
    """
    raise NotImplementedError


def relu(z):
    """Activacion ReLU: el maximo entre 0 y z.

    La que se usa hoy en casi todo. Barata y su derivada no se desvanece para
    z positivo.
    """
    raise NotImplementedError


def neurona(x, w, b, activacion=sigmoide):
    """Calcula la salida de una neurona: activacion(w . x + b).

    neurona([1, 1], [1, 1], -1.5, escalon) -> 0.0
    neurona([1, 1], [1, 1], -0.5, escalon) -> 1.0

    Levanta ValueError si len(x) != len(w).

    Para pensar mientras se programa: con w = [1, 1] y b = -1.5, la neurona
    responde 1 solo cuando las DOS entradas estan encendidas. Eso es un AND.
    Con b = -0.5 es un OR. El sesgo es el umbral.
    """
    raise NotImplementedError


def capa(x, pesos, sesgos, activacion=sigmoide):
    """Calcula la salida de una capa entera: una neurona por cada fila de pesos.

    capa([1, 1], [[1, 1], [-1, -1]], [-0.5, 1.5], escalon) -> [1.0, 0.0]

    Devuelve una lista con una salida por neurona.

    Esto es la matriz de la semana en accion: pesos es una matriz, y aplicarla a
    x es exactamente lo del miercoles, mas el sesgo y la activacion.

    Levanta ValueError si len(pesos) != len(sesgos).
    """
    raise NotImplementedError


def neurona_np(x, w, b, activacion=None):
    """La misma neurona, en NumPy, sin bucles de Python.

    Se escribe DESPUES de que neurona() funcione.
    Devolver un float de Python, no un escalar de numpy.

    Si activacion es None, usar la sigmoide vectorizada de numpy.

    Despues de escribirla, anotar en el diario:
      - Cuantas lineas tiene cada version.
      - Que operacion de numpy reemplazo a mi bucle.
      - Que me esta ocultando numpy aqui.
    """
    raise NotImplementedError
