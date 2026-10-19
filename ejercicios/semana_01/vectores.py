"""Semana 1 · lunes — Vectores.

Video: 3Blue1Brown, Essence of Linear Algebra, cap. 1.
Lectura: Mathematics for Machine Learning, 2.1-2.2.

Reglas:
  - Python puro. No importar numpy en este archivo.
  - Un vector se representa como una lista de floats: [1.0, 2.0, 3.0].
  - Si las dimensiones no coinciden, levantar ValueError.

Correr los tests:  python -m pytest ejercicios/tests/test_semana_01.py -v
"""


def sumar(v, w):
    """Suma dos vectores componente a componente.

    sumar([1, 2], [3, 4]) -> [4, 6]

    Geometricamente: poner la cola de w en la punta de v.

    Levanta ValueError si len(v) != len(w).
    """
    raise NotImplementedError


def escalar(k, v):
    """Multiplica el vector v por el numero k.

    escalar(2, [1, -3]) -> [2, -6]

    Geometricamente: estirar v por k. Si k es negativo, tambien lo da vuelta.
    """
    raise NotImplementedError


def restar(v, w):
    """Resta w de v.

    restar([5, 5], [1, 2]) -> [4, 3]

    Pista: se puede escribir usando sumar y escalar, sin bucle nuevo.
    """
    raise NotImplementedError


def magnitud(v):
    """Devuelve la longitud (norma euclidiana) de v.

    magnitud([3, 4]) -> 5.0

    Esto es la raiz de la suma de los cuadrados. Sale del teorema de Pitagoras
    extendido a n dimensiones.
    """
    raise NotImplementedError


def normalizar(v):
    """Devuelve un vector con la misma direccion que v y magnitud 1.

    normalizar([3, 4]) -> [0.6, 0.8]

    Levanta ValueError si v es el vector cero (no tiene direccion).
    """
    raise NotImplementedError
