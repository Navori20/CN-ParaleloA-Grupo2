
import math
import sympy as sp


def taylor(funcion, x0, x, orden_maximo=15, cifras=3):
    """
    Calcula la serie de Taylor y sus errores.

    funcion: expresión matemática, por ejemplo 'exp(-x)'
    x0: punto base de la serie
    x: punto donde se evalúa
    orden_maximo: orden máximo del polinomio (0 a 15)
    cifras: número de cifras significativas
    """

    variable = sp.Symbol("x")

    # Convertimos los textos en expresiones matemáticas
    expresion = sp.sympify(funcion)
    x0 = float(sp.N(sp.sympify(x0)))
    x = float(sp.N(sp.sympify(x)))

    if not 0 <= orden_maximo <= 15:
        raise ValueError("El orden debe estar entre 0 y 15.")

    if cifras < 1:
        raise ValueError("Las cifras significativas deben ser positivas.")

    # Función verdadera
    f = sp.lambdify(variable, expresion, "math")
    valor_verdadero = float(f(x))

    # Criterio de Scarborough
    tolerancia = 0.5 * 10 ** (2 - cifras)

    h = x - x0
    aproximacion = 0.0
    aproximacion_anterior = None
    resultados = []
    primer_orden_valido = None

    derivada = expresion

    for n in range(orden_maximo + 1):

        # Evaluar la derivada en el punto base
        funcion_derivada = sp.lambdify(
            variable, derivada, "math"
        )
        valor_derivada = float(funcion_derivada(x0))

        # Término de Taylor
        termino = valor_derivada * h**n / math.factorial(n)

        # Sumatoria programada manualmente
        aproximacion += termino

        # Error verdadero
        error_verdadero = valor_verdadero - aproximacion

        if valor_verdadero != 0:
            error_relativo_verdadero = (
                error_verdadero / valor_verdadero
            ) * 100
        else:
            error_relativo_verdadero = None

        # Error aproximado
        if aproximacion_anterior is None or aproximacion == 0:
            error_aproximado = None
        else:
            error_aproximado = (
                (aproximacion - aproximacion_anterior)
                / aproximacion
            ) * 100

        # Derivada siguiente y residuo estimado
        siguiente_derivada = sp.diff(derivada, variable)

        f_siguiente = sp.lambdify(
            variable, siguiente_derivada, "math"
        )

        residuo = (
            float(f_siguiente(x0))
            * h ** (n + 1)
            / math.factorial(n + 1)
        )

        resultados.append({
            "orden": n,
            "termino": termino,
            "aproximacion": aproximacion,
            "error_verdadero": error_verdadero,
            "error_relativo_verdadero": error_relativo_verdadero,
            "error_aproximado": error_aproximado,
            "residuo": residuo
        })

        # Primera vez que cumple la tolerancia
        if (
            primer_orden_valido is None
            and error_aproximado is not None
            and abs(error_aproximado) < tolerancia
        ):
            primer_orden_valido = n

        aproximacion_anterior = aproximacion
        derivada = siguiente_derivada

    return {
        "funcion": str(expresion),
        "valor_verdadero": valor_verdadero,
        "tolerancia": tolerancia,
        "resultados": resultados,
        "orden_requerido": primer_orden_valido,
        "terminos_requeridos": (
            primer_orden_valido + 1
            if primer_orden_valido is not None
            else None
        )
    }


if __name__ == "__main__":

    # Caso obligatorio del grupo 2:
    # Descarga del capacitor RC cuando t = RC

    resultado = taylor(
        funcion="exp(-x)",
        x0="0",
        x="1",
        orden_maximo=15,
        cifras=3
    )

    print("PROYECTO DE TAYLOR - GRUPO 2")
    print("-" * 45)

    print("Valor verdadero:", resultado["valor_verdadero"])
    print("Tolerancia:", resultado["tolerancia"], "%")
    print("Orden requerido:", resultado["orden_requerido"])
    print("Términos requeridos:", resultado["terminos_requeridos"])

    print("\nTabla de resultados:")

    for fila in resultado["resultados"]:
        print(
            f"n={fila['orden']:2d} | "
            f"Pn={fila['aproximacion']:.9f} | "
            f"ea={fila['error_aproximado']}"
        )
