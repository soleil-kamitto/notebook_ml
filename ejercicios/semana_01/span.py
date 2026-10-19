"""Semana 1 · martes — Combinaciones lineales, span e independencia.

Video: 3Blue1Brown, cap. 2.
Lectura: MML 2.5.

Reglas:
  - Python puro. Se pueden importar funciones de vectores.py.
  - Comparar floats siempre con tolerancia, nunca con ==.
"""

from .vectores import sumar, escalar


def combinacion_lineal(vectores, pesos):
    """Devuelve la suma de cada vector multiplicado por su peso.

    combinacion_lineal([[1, 0], [0, 1]], [3, -2]) -> [3, -2]

    Esta es LA operacion de la semana: w1*v1 + w2*v2 + ... Es lo que hace una
    neurona, y es lo que hace una matriz al multiplicar por un vector.

    Levanta ValueError si len(vectores) != len(pesos), o si la lista esta vacia,
    o si los vectores no tienen todos la misma dimension.
    """
    raise NotImplementedError


def son_paralelos(v, w, tol=1e-9):
    """Dice si v y w apuntan en la misma direccion o en la opuesta.

    son_paralelos([1, 2], [2, 4]) -> True
    son_paralelos([1, 2], [2, 5]) -> False

    Dos vectores son paralelos si uno es un multiplo escalar del otro.
    El vector cero es paralelo a todo.

    Pista: en 2D hay una cuenta con dos multiplicaciones que lo decide.
    Pensar en que pasa cuando el area del paralelogramo que forman es cero.
    """
    raise NotImplementedError


def esta_en_el_span(objetivo, v, w, tol=1e-9):
    """Dice si el vector objetivo (2D) se puede escribir como combinacion de v y w.

    esta_en_el_span([3, 3], [1, 0], [0, 1]) -> True
    esta_en_el_span([1, 1], [1, 0], [2, 0]) -> False   (v y w solo cubren el eje x)

    Solo para vectores de dimension 2.

    Casos a pensar antes de programar:
      - Si v y w NO son paralelos, cubren todo el plano. Entonces la respuesta es...
      - Si v y w SI son paralelos, cubren solo una linea. Entonces hay que ver si
        el objetivo cae sobre esa linea.
      - Si los dos son el vector cero, el span es solo el origen.
    """
    raise NotImplementedError
