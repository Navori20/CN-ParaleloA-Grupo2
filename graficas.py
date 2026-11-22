"""Gráficas del proyecto de Taylor — Grupo 2.

Se usan las derivadas de SymPy, pero la suma de Taylor se construye
manualmente (sin sympy.series). Compatible con las llamadas desde main.py:
  grafica_funcion(figura, funcion, x0, x_eval, orden)
  grafica_error(figura, resultados)
  grafica_truncamiento(figura, funcion, x0, orden)
"""

import math
import numpy as np
import sympy as sp


def preparar_funcion(funcion):
    x = sp.Symbol("x")
    expresion = sp.sympify(funcion, locals={"x": x})
    if expresion.free_symbols - {x}:
        raise ValueError("La función solo puede contener la variable x.")
    return x, expresion


def polinomio_taylor(funcion, x0, orden):
    """Polinomio de Taylor calculado término a término."""
    x, expresion = preparar_funcion(funcion)
    x0 = sp.sympify(x0)
    polinomio = sp.Integer(0)
    derivada = expresion
    for k in range(int(orden) + 1):
        polinomio += derivada.subs(x, x0) * (x - x0) ** k / math.factorial(k)
        derivada = sp.diff(derivada, x)
    return sp.expand(polinomio)


def _estilo(figura, titulo, xlabel, ylabel):
    """Estilo compacto para un gráfico incrustado en Qt Designer."""
    figura.clear()
    figura.set_facecolor("#fafafa")
    ax = figura.add_subplot(111)
    ax.set_facecolor("#ffffff")
    ax.set_title(titulo, fontsize=9, pad=9, fontweight="semibold")
    ax.set_xlabel(xlabel, fontsize=8, labelpad=3)
    ax.set_ylabel(ylabel, fontsize=8, labelpad=3)
    ax.tick_params(axis="both", labelsize=7)
    ax.grid(True, which="major", alpha=0.22)
    # Márgenes generosos para evitar cortar títulos o ejes en pestañas pequeñas.
    figura.subplots_adjust(left=0.18, right=0.96, top=0.79, bottom=0.22)
    return ax


def _evaluar(funcion_np, valores_x):
    """Convierte resultados constantes o vectorizados a un vector real."""
    con_errores = np.asarray(funcion_np(valores_x), dtype=float)
    return np.broadcast_to(con_errores, np.shape(valores_x))


def grafica_funcion(figura, funcion, x0, x_eval, orden):
    """Función exacta y polinomios P0,...,Pn en torno a x0."""
    x0, x_eval = float(x0), float(x_eval)
    ax = _estilo(figura, "Función y aproximaciones de Taylor", "x", "f(x)")
    x, expresion = preparar_funcion(funcion)
    distancia = max(abs(x_eval - x0), 0.5)
    valores_x = np.linspace(min(x0, x_eval) - 0.35 * distancia,
                            max(x0, x_eval) + 0.35 * distancia, 300)

    exacta = sp.lambdify(x, expresion, "numpy")
    y_real = _evaluar(exacta, valores_x)
    ax.plot(valores_x, y_real, linewidth=2.4, color="#1674bc", label="f(x)", zorder=5)

    # Construir cada polinomio manualmente; derivadas calculadas con SymPy.
    derivada = expresion
    polinomio = sp.Integer(0)
    for n in range(int(orden) + 1):
        polinomio += derivada.subs(x, sp.Float(x0)) * (x - sp.Float(x0)) ** n / math.factorial(n)
        aprox = sp.lambdify(x, polinomio, "numpy")
        y_aprox = _evaluar(aprox, valores_x)
        ax.plot(valores_x, y_aprox, linestyle="--", linewidth=0.9,
                alpha=0.55, label=f"P{n}" if n in (0, 1, 2, 3, int(orden)) else "_nolegend_")
        derivada = sp.diff(derivada, x)

    ax.axvline(x0, color="#666666", linestyle=":", linewidth=1, label="x₀")
    ax.axvline(x_eval, color="#b05a22", linestyle=":", linewidth=1, label="x eval.")
    ax.legend(loc="best", fontsize=6, ncol=2, framealpha=0.85)

    # Priorizar el intervalo relevante, sin perder los polinomios que deben graficarse.
    reales_finitos = y_real[np.isfinite(y_real)]
    if len(reales_finitos) > 1:
        qmin, qmax = np.percentile(reales_finitos, [0, 100])
        margen = max((qmax - qmin) * 0.35, 0.1)
        ax.set_ylim(qmin - margen, qmax + margen)


def grafica_error(figura, resultados):
    """Magnitud del error verdadero (%) contra orden n, semilog-y."""
    ax = _estilo(figura, "Error verdadero vs. orden", "Orden n", "|εt| (%)")
    ordenes, errores = [], []
    for fila in resultados:
        error = fila.get("error_relativo_verdadero")
        if error is not None and np.isfinite(error) and abs(error) > 0:
            ordenes.append(fila["orden"])
            errores.append(abs(error))
    if ordenes:
        ax.semilogy(ordenes, errores, "o-", linewidth=1.7, markersize=3.5,
                    color="#1674bc")
        ax.grid(True, which="both", alpha=0.22)
    else:
        ax.text(0.5, 0.5, "Sin errores relativos graficables",
                ha="center", va="center", fontsize=9, transform=ax.transAxes)


def grafica_truncamiento(figura, funcion, x0, orden):
    """Error absoluto vs |h| (log-log) y pendiente experimental."""
    ax = _estilo(figura, f"Truncamiento: orden n = {orden}", "|h|", "|Et|")
    x0 = float(x0)
    x, expresion = preparar_funcion(funcion)
    polinomio = polinomio_taylor(funcion, x0, orden)
    f = sp.lambdify(x, expresion, "numpy")
    p = sp.lambdify(x, polinomio, "numpy")

    valores_h = np.logspace(-2, -0.3, 35)
    valores = x0 + valores_h
    reales = _evaluar(f, valores)
    aproximados = _evaluar(p, valores)
    errores = np.abs(reales - aproximados)
    validos = np.isfinite(errores) & (errores > 1e-14)

    if np.count_nonzero(validos) >= 2:
        pendiente = np.polyfit(np.log10(valores_h[validos]),
                               np.log10(errores[validos]), 1)[0]
        ax.loglog(valores_h[validos], errores[validos], "o-", color="#1674bc",
                  linewidth=1.7, markersize=3.2, label=f"Pendiente ≈ {pendiente:.2f}")
        ax.legend(fontsize=7, loc="upper left")
        ax.grid(True, which="both", alpha=0.22)
    else:
        ax.text(0.5, 0.5, "Error muy pequeño para estimar pendiente",
                ha="center", va="center", fontsize=8, transform=ax.transAxes)
