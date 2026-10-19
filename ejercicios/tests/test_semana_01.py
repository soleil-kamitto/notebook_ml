"""Tests de la semana 1. Escritos por el tutor; no se modifican para que pasen.

Correr todo:        python -m pytest ejercicios/tests/test_semana_01.py -v
Correr un dia:      python -m pytest ejercicios/tests/test_semana_01.py -v -k lunes
Parar en el primer fallo:   python -m pytest ejercicios/tests/test_semana_01.py -x

Los marcadores (lunes, martes, ...) permiten correr solo el dia que toca.
"""

import math

import pytest

from ejercicios.semana_01 import (
    neurona as N,
    producto_punto as P,
    span as S,
    transformaciones as T,
    vectores as V,
)

APROX = 1e-9


# --------------------------------------------------------------- lunes
@pytest.mark.lunes
class TestVectores:
    def test_sumar(self):
        assert V.sumar([1, 2], [3, 4]) == pytest.approx([4, 6])
        assert V.sumar([0, 0, 0], [1, -1, 2]) == pytest.approx([1, -1, 2])
        assert V.sumar([-1.5], [1.5]) == pytest.approx([0.0])

    def test_sumar_dimensiones_distintas(self):
        with pytest.raises(ValueError):
            V.sumar([1, 2], [1, 2, 3])

    def test_escalar(self):
        assert V.escalar(2, [1, -3]) == pytest.approx([2, -6])
        assert V.escalar(0, [5, 5]) == pytest.approx([0, 0])
        assert V.escalar(-1, [1, 2]) == pytest.approx([-1, -2])

    def test_restar(self):
        assert V.restar([5, 5], [1, 2]) == pytest.approx([4, 3])
        assert V.restar([1, 1], [1, 1]) == pytest.approx([0, 0])

    def test_magnitud(self):
        assert V.magnitud([3, 4]) == pytest.approx(5.0)
        assert V.magnitud([0, 0]) == pytest.approx(0.0)
        assert V.magnitud([1, 1, 1, 1]) == pytest.approx(2.0)

    def test_normalizar(self):
        assert V.normalizar([3, 4]) == pytest.approx([0.6, 0.8])
        assert V.magnitud(V.normalizar([7, -2, 3])) == pytest.approx(1.0)

    def test_normalizar_vector_cero(self):
        with pytest.raises(ValueError):
            V.normalizar([0, 0])


# --------------------------------------------------------------- martes
@pytest.mark.martes
class TestSpan:
    def test_combinacion_lineal_base_canonica(self):
        assert S.combinacion_lineal([[1, 0], [0, 1]], [3, -2]) == pytest.approx([3, -2])

    def test_combinacion_lineal_general(self):
        r = S.combinacion_lineal([[1, 2], [3, 4], [5, 6]], [1, 0, -1])
        assert r == pytest.approx([-4, -4])

    def test_combinacion_lineal_pesos_cero(self):
        assert S.combinacion_lineal([[1, 2], [3, 4]], [0, 0]) == pytest.approx([0, 0])

    def test_combinacion_lineal_errores(self):
        with pytest.raises(ValueError):
            S.combinacion_lineal([[1, 2], [3, 4]], [1])
        with pytest.raises(ValueError):
            S.combinacion_lineal([], [])
        with pytest.raises(ValueError):
            S.combinacion_lineal([[1, 2], [3, 4, 5]], [1, 1])

    def test_son_paralelos(self):
        assert S.son_paralelos([1, 2], [2, 4]) is True
        assert S.son_paralelos([1, 2], [-3, -6]) is True
        assert S.son_paralelos([1, 2], [2, 5]) is False
        assert S.son_paralelos([1, 0], [0, 1]) is False

    def test_son_paralelos_con_cero(self):
        assert S.son_paralelos([0, 0], [1, 2]) is True

    def test_esta_en_el_span_base_completa(self):
        assert S.esta_en_el_span([3, 3], [1, 0], [0, 1]) is True
        assert S.esta_en_el_span([-7.5, 0.25], [1, 0], [0, 1]) is True

    def test_esta_en_el_span_degenerado(self):
        # v y w paralelos: solo cubren el eje x
        assert S.esta_en_el_span([1, 1], [1, 0], [2, 0]) is False
        assert S.esta_en_el_span([5, 0], [1, 0], [2, 0]) is True

    def test_esta_en_el_span_todo_cero(self):
        assert S.esta_en_el_span([0, 0], [0, 0], [0, 0]) is True
        assert S.esta_en_el_span([1, 0], [0, 0], [0, 0]) is False


# --------------------------------------------------------------- miercoles
@pytest.mark.miercoles
class TestTransformaciones:
    def test_aplicar_identidad(self):
        assert T.aplicar([[1, 0], [0, 1]], [3, 4]) == pytest.approx([3, 4])

    def test_aplicar_rotacion_90(self):
        assert T.aplicar([[0, -1], [1, 0]], [1, 0]) == pytest.approx([0, 1])
        assert T.aplicar([[0, -1], [1, 0]], [0, 1]) == pytest.approx([-1, 0])

    def test_aplicar_columnas_son_destino_de_la_base(self):
        # La primera columna es donde cae i, la segunda donde cae j.
        m = [[2, -1], [5, 3]]
        assert T.aplicar(m, [1, 0]) == pytest.approx([2, 5])
        assert T.aplicar(m, [0, 1]) == pytest.approx([-1, 3])

    def test_aplicar_no_cuadrada(self):
        # 3 filas, 2 columnas: toma un vector 2D y devuelve uno 3D
        m = [[1, 0], [0, 1], [1, 1]]
        assert T.aplicar(m, [2, 3]) == pytest.approx([2, 3, 5])

    def test_aplicar_dimension_incompatible(self):
        with pytest.raises(ValueError):
            T.aplicar([[1, 0], [0, 1]], [1, 2, 3])

    def test_transpuesta(self):
        assert T.transpuesta([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
        assert T.transpuesta(T.transpuesta([[1, 2], [3, 4]])) == [[1, 2], [3, 4]]

    def test_identidad(self):
        assert T.identidad(1) == [[1]]
        assert T.identidad(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def test_determinante(self):
        assert T.determinante_2x2([[1, 0], [0, 1]]) == pytest.approx(1)
        assert T.determinante_2x2([[2, 0], [0, 3]]) == pytest.approx(6)
        assert T.determinante_2x2([[1, 2], [2, 4]]) == pytest.approx(0)
        assert T.determinante_2x2([[0, 1], [1, 0]]) == pytest.approx(-1)

    def test_determinante_no_2x2(self):
        with pytest.raises(ValueError):
            T.determinante_2x2([[1, 2, 3], [4, 5, 6]])


# --------------------------------------------------------------- jueves
@pytest.mark.jueves
class TestProductoPunto:
    def test_producto_punto(self):
        assert P.producto_punto([1, 2, 3], [4, 5, 6]) == pytest.approx(32)
        assert P.producto_punto([1, 0], [0, 1]) == pytest.approx(0)
        assert P.producto_punto([1, 1], [-1, -1]) == pytest.approx(-2)

    def test_producto_punto_consigo_mismo_es_magnitud_cuadrada(self):
        v = [3, 4]
        assert P.producto_punto(v, v) == pytest.approx(V.magnitud(v) ** 2)

    def test_producto_punto_conmutativo(self):
        assert P.producto_punto([1, 2], [3, 4]) == pytest.approx(
            P.producto_punto([3, 4], [1, 2])
        )

    def test_producto_punto_dimensiones(self):
        with pytest.raises(ValueError):
            P.producto_punto([1, 2], [1, 2, 3])

    def test_angulo_entre(self):
        assert P.angulo_entre([1, 0], [0, 1]) == pytest.approx(math.pi / 2)
        assert P.angulo_entre([1, 0], [1, 0]) == pytest.approx(0.0, abs=1e-7)
        assert P.angulo_entre([1, 0], [-1, 0]) == pytest.approx(math.pi, abs=1e-7)
        assert P.angulo_entre([1, 1], [1, 0]) == pytest.approx(math.pi / 4)

    def test_angulo_vector_cero(self):
        with pytest.raises(ValueError):
            P.angulo_entre([0, 0], [1, 1])

    def test_matmul_identidad(self):
        a = [[1, 2], [3, 4]]
        assert P.matmul(a, T.identidad(2)) == pytest.approx(a)
        assert P.matmul(T.identidad(2), a) == pytest.approx(a)

    def test_matmul_no_conmutativo(self):
        a = [[1, 1], [0, 1]]
        b = [[1, 0], [1, 1]]
        assert P.matmul(a, b) != P.matmul(b, a)

    def test_matmul_rectangular(self):
        a = [[1, 2, 3], [4, 5, 6]]       # 2x3
        b = [[7, 8], [9, 10], [11, 12]]  # 3x2
        assert P.matmul(a, b) == pytest.approx([[58, 64], [139, 154]])

    def test_matmul_es_composicion(self):
        # Aplicar b y despues a == aplicar (a*b) de una vez
        a = [[0, -1], [1, 0]]
        b = [[2, 0], [0, 2]]
        v = [1, 3]
        assert T.aplicar(P.matmul(a, b), v) == pytest.approx(
            T.aplicar(a, T.aplicar(b, v))
        )

    def test_matmul_dimensiones(self):
        with pytest.raises(ValueError):
            P.matmul([[1, 2]], [[1, 2]])

    def test_matmul_np_coincide_con_la_version_a_mano(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[7, 8], [9, 10], [11, 12]]
        assert P.matmul_np(a, b) == pytest.approx(P.matmul(a, b))


# --------------------------------------------------------------- viernes
@pytest.mark.viernes
class TestNeurona:
    def test_escalon(self):
        assert N.escalon(1.0) == pytest.approx(1.0)
        assert N.escalon(-1.0) == pytest.approx(0.0)
        assert N.escalon(0.0) == pytest.approx(0.0)

    def test_sigmoide(self):
        assert N.sigmoide(0.0) == pytest.approx(0.5)
        assert N.sigmoide(2.0) == pytest.approx(0.8807970779778823)
        assert N.sigmoide(-2.0) == pytest.approx(0.11920292202211755)

    def test_sigmoide_no_desborda(self):
        # Si la formula se escribio sin cuidado, esto explota con OverflowError.
        assert N.sigmoide(-1000.0) == pytest.approx(0.0)
        assert N.sigmoide(1000.0) == pytest.approx(1.0)

    def test_sigmoide_es_simetrica(self):
        assert N.sigmoide(3.0) + N.sigmoide(-3.0) == pytest.approx(1.0)

    def test_relu(self):
        assert N.relu(3.0) == pytest.approx(3.0)
        assert N.relu(-3.0) == pytest.approx(0.0)
        assert N.relu(0.0) == pytest.approx(0.0)

    def test_neurona_es_un_and(self):
        w, b = [1, 1], -1.5
        assert N.neurona([1, 1], w, b, N.escalon) == pytest.approx(1.0)
        assert N.neurona([1, 0], w, b, N.escalon) == pytest.approx(0.0)
        assert N.neurona([0, 1], w, b, N.escalon) == pytest.approx(0.0)
        assert N.neurona([0, 0], w, b, N.escalon) == pytest.approx(0.0)

    def test_neurona_es_un_or(self):
        w, b = [1, 1], -0.5
        assert N.neurona([1, 1], w, b, N.escalon) == pytest.approx(1.0)
        assert N.neurona([1, 0], w, b, N.escalon) == pytest.approx(1.0)
        assert N.neurona([0, 0], w, b, N.escalon) == pytest.approx(0.0)

    def test_neurona_usa_la_activacion_que_se_le_pasa(self):
        assert N.neurona([1, 1], [1, 1], 0.0, N.sigmoide) == pytest.approx(
            N.sigmoide(2.0)
        )
        assert N.neurona([1, 1], [1, 1], -5.0, N.relu) == pytest.approx(0.0)

    def test_neurona_dimensiones(self):
        with pytest.raises(ValueError):
            N.neurona([1, 2], [1], 0.0)

    def test_capa(self):
        salida = N.capa([1, 1], [[1, 1], [-1, -1]], [-0.5, 1.5], N.escalon)
        assert salida == pytest.approx([1.0, 0.0])

    def test_capa_una_neurona_por_fila(self):
        salida = N.capa([2.0], [[1], [2], [3]], [0, 0, 0], N.relu)
        assert salida == pytest.approx([2.0, 4.0, 6.0])

    def test_capa_dimensiones(self):
        with pytest.raises(ValueError):
            N.capa([1, 1], [[1, 1], [1, 1]], [0.0])

    def test_neurona_np_coincide_con_la_version_a_mano(self):
        x, w, b = [0.5, -1.5, 2.0], [1.0, 2.0, -0.5], 0.25
        assert N.neurona_np(x, w, b) == pytest.approx(N.neurona(x, w, b, N.sigmoide))

    def test_neurona_np_devuelve_float_de_python(self):
        r = N.neurona_np([1.0, 1.0], [1.0, 1.0], 0.0)
        assert type(r) is float
