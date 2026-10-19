"""Semana 1 · miercoles — Transformaciones lineales y matrices.

Video: 3Blue1Brown, cap. 3.
Lectura: MML 2.7.

Representacion: una matriz es una lista de filas.
    [[a, b],
     [c, d]]   se escribe   [[a, b], [c, d]]

La idea central del capitulo: las COLUMNAS de la matriz son a donde aterrizan
los vectores base. La primera columna es donde cae i, la segunda donde cae j.

Verificacion visual: el laboratorio de matrices en web/index.html.
Calcular a mano primero, comparar despues.
"""


def aplicar(matriz, v):
    """Aplica la matriz al vector v y devuelve el vector resultante.

    aplicar([[1, 0], [0, 1]], [3, 4]) -> [3, 4]      (identidad)
    aplicar([[0, -1], [1, 0]], [1, 0]) -> [0, 1]     (rotar 90 grados)

    Funciona para matrices de n filas por m columnas y vectores de dimension m.

    Pista conceptual: el resultado es una combinacion lineal de las COLUMNAS de
    la matriz, con pesos iguales a las componentes de v. Si eso se ve, la funcion
    sale en dos lineas.

    Levanta ValueError si el ancho de la matriz no coincide con len(v).
    """
    raise NotImplementedError


def transpuesta(matriz):
    """Devuelve la matriz con filas y columnas intercambiadas.

    transpuesta([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    """
    raise NotImplementedError


def identidad(n):
    """Devuelve la matriz identidad de n por n.

    identidad(2) -> [[1, 0], [0, 1]]

    Es la transformacion que no mueve nada.
    """
    raise NotImplementedError


def determinante_2x2(matriz):
    """Devuelve el determinante de una matriz 2x2.

    determinante_2x2([[1, 0], [0, 1]]) -> 1
    determinante_2x2([[2, 0], [0, 3]]) -> 6

    Que significa: cuanto se multiplica el area despues de la transformacion.
    Si sale 0, el plano se aplasto en una linea o en un punto.
    Si sale negativo, el plano se dio vuelta (la orientacion se invirtio).

    Levanta ValueError si la matriz no es 2x2.
    """
    raise NotImplementedError
