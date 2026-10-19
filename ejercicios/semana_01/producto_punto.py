"""Semana 1 · jueves — Producto punto y multiplicacion de matrices.

Videos: 3Blue1Brown, cap. 4 (composicion) y cap. 9 (producto punto y dualidad).
Lectura: MML 3.1-3.2.

Este es el archivo mas importante de la semana: la neurona del viernes se
construye encima de producto_punto. Hacerlo bien.

Reglas:
  - Python puro, con bucles explicitos. Nada de numpy, nada de sum(zip(...)).
    El punto del ejercicio es sentir el costo de la operacion.
"""

import math


def producto_punto(v, w):
    """Devuelve la suma de los productos componente a componente.

    producto_punto([1, 2, 3], [4, 5, 6]) -> 32     (1*4 + 2*5 + 3*6)
    producto_punto([1, 0], [0, 1]) -> 0            (perpendiculares)

    Formula: sum de v[i] * w[i].

    Que mide: cuanto apunta v en la direccion de w, por la longitud de w.
      - Positivo: apuntan al mismo lado.
      - Cero: perpendiculares.
      - Negativo: apuntan a lados opuestos.

    Esto es exactamente lo que calcula una neurona sobre su entrada.

    Levanta ValueError si len(v) != len(w).
    """
    raise NotImplementedError


def angulo_entre(v, w):
    """Devuelve el angulo entre v y w, en radianes, entre 0 y pi.

    angulo_entre([1, 0], [0, 1]) -> 1.5707...   (pi/2)

    De la definicion geometrica: v . w = |v| |w| cos(theta).

    Cuidado: por error de punto flotante el coseno puede salir 1.0000000002 y
    math.acos explota. Hay que recortarlo al rango [-1, 1].

    Levanta ValueError si alguno de los dos es el vector cero.
    """
    raise NotImplementedError


def matmul(a, b):
    """Multiplica la matriz a por la matriz b con tres bucles anidados.

    matmul([[1, 2], [3, 4]], [[1, 0], [0, 1]]) -> [[1, 2], [3, 4]]

    El elemento (i, j) del resultado es el producto punto de la fila i de a con
    la columna j de b.

    Que significa: aplicar primero la transformacion b y despues la a. Por eso
    el orden importa y matmul(a, b) no es matmul(b, a).

    Levanta ValueError si el ancho de a no coincide con la altura de b.
    """
    raise NotImplementedError


def matmul_np(a, b):
    """La misma multiplicacion, pero con numpy.

    Se escribe DESPUES de que matmul funcione, no antes.
    Devolver una lista de listas de Python, no un ndarray, para que los tests
    comparen las dos versiones directamente.

    Pista de sintaxis permitida: numpy tiene un operador @ para esto, y los
    arrays tienen un metodo .tolist().
    """
    raise NotImplementedError
