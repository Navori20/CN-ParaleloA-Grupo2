
import math
import pytest

from metodo.taylor import taylor


def test_capacitor_rc():
    """Prueba obligatoria del Grupo 2."""
    resultado = taylor("exp(-x)", "0", "1", 15, 3)

    assert resultado["orden_requerido"] == 8
    assert resultado["terminos_requeridos"] == 9
    assert resultado["valor_verdadero"] == pytest.approx(
        math.exp(-1), abs=1e-9
    )
    assert resultado["resultados"][8]["aproximacion"] == pytest.approx(
        0.367881944, abs=1e-9
    )


def test_ejemplo_libro():
    """Ejemplo de cos(x) del libro de Chapra."""
    resultado = taylor("cos(x)", "pi/4", "pi/3", 6, 3)

    esperado = [
        0.707106781,
        0.521986659,
        0.497754491,
        0.499869147,
        0.500007551,
        0.500000304,
        0.499999988,
    ]

    for n, valor in enumerate(esperado):
        assert resultado["resultados"][n]["aproximacion"] == pytest.approx(
            valor, abs=1e-8
        )


def test_scarborough():
    """Comprobar 3 cifras significativas para exp(0.5)."""
    resultado = taylor("exp(x)", "0", "0.5", 15, 3)

    assert resultado["terminos_requeridos"] == 6
    assert resultado["resultados"][5]["aproximacion"] == pytest.approx(
        1.648697917, abs=1e-9
    )


def test_orden_invalido():  
    """El programa debe rechazar órdenes superiores a 15."""
    with pytest.raises(ValueError):
        taylor("exp(-x)", "0", "1", 16, 3)


def test_taylor_seno():
    """Comprueba la aproximación de Taylor para sin(x)."""
    resultado = taylor("sin(x)", "0", "0.5", 15, 3)

    assert resultado["valor_verdadero"] == pytest.approx(
        math.sin(0.5), abs=1e-9
    )
    assert resultado["resultados"][7]["aproximacion"] == pytest.approx(
        math.sin(0.5), abs=1e-6
    )



def test_cifras_significativas_invalidas():
    """Comprueba que no se permiten cero cifras significativas."""
    with pytest.raises(ValueError):
        taylor("exp(-x)", "0", "1", 15, 0)

