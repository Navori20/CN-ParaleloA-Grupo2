"""Interfaz principal: series de Taylor y caso RC (Grupo 2)."""
import csv
import sys
import math

import sympy as sp
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QMessageBox,
    QTableWidgetItem, QVBoxLayout,
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from graficas import grafica_error, grafica_funcion, grafica_truncamiento
from metodo.taylor import taylor
from ui_ventana_principal import Ui_MainWindow


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resultado_actual = None

        # Los QWidget de Qt Designer ya están dentro de cada pestaña.
        self.figuras = []
        self.lienzos = []
        espacios = (
            self.ui.widgetGraficaTaylor,
            self.ui.widgetGraficaError,
            self.ui.widgetGraficaTruncamiento,
        )
        for espacio in espacios:
            figura = Figure(figsize=(5, 4))
            lienzo = FigureCanvasQTAgg(figura)
            disposicion = espacio.layout()
            if disposicion is None:
                disposicion = QVBoxLayout(espacio)
                disposicion.setContentsMargins(0, 0, 0, 0)
            disposicion.addWidget(lienzo)
            self.figuras.append(figura)
            self.lienzos.append(lienzo)

        self.ui.tablaResultados.setColumnCount(7)
        self.ui.tablaResultados.setHorizontalHeaderLabels([
            "Orden n", "Término", "Pₙ(x)", "Error Eₜ",
            "εₜ (%)", "εₐ (%)", "Residuo Rₙ",
        ])
        self.ui.btnCalcular.clicked.connect(self.calcular)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnExportar.clicked.connect(self.exportar_csv)
        self.ui.cmbEjemplos.currentIndexChanged.connect(self.cargar_ejemplo)
        self.cargar_ejemplo(0)

    def cargar_ejemplo(self, indice):
        ejemplos = {
            0: ("exp(-x)", "0", "1", 15, 3),
            1: ("cos(x)", "pi/4", "pi/3", 6, 3),
            2: ("exp(x)", "0", "0.5", 15, 3),
        }
        if indice not in ejemplos:
            return
        funcion, x0, x, orden, cifras = ejemplos[indice]
        self.ui.txtFuncion.setText(funcion)
        self.ui.txtX0.setText(x0)
        self.ui.txtX.setText(x)
        self.ui.spinOrden.setValue(orden)
        self.ui.spinCifras.setValue(cifras)
        self.ui.tablaResultados.setRowCount(0)
        self.ui.lblResultado.setText("Presiona Calcular Taylor para ver los resultados.")
        self.resultado_actual = None

    @staticmethod
    def convertir_numero(texto):
        valor = sp.sympify(texto, locals={"pi": sp.pi})
        if valor.free_symbols:
            raise ValueError("Los puntos de evaluación deben ser números.")
        resultado = float(sp.N(valor))
        if not (-float("inf") < resultado < float("inf")):
            raise ValueError("Se necesita un valor numérico finito.")
        return resultado

    def calcular(self):
        try:
            funcion = self.ui.txtFuncion.text().strip()
            x0 = self.ui.txtX0.text().strip()
            x = self.ui.txtX.text().strip()
            orden = self.ui.spinOrden.value()
            cifras = self.ui.spinCifras.value()
            if not funcion or not x0 or not x:
                raise ValueError("Completa la función, el punto base y el punto de evaluación.")

            # En el ejemplo RC, la variable de Taylor es x = t/(R*C).
            # Los controles de capacitancia en Qt Designer están en microfaradios.
            caso_rc = self.ui.cmbEjemplos.currentIndex() == 0
            if caso_rc:
                v0 = self.ui.spinV0.value()
                resistencia = self.ui.spinR.value()
                capacitancia_uf = self.ui.spinC.value()
                tiempo = self.ui.spinTiempo.value()
                if not all(math.isfinite(v) for v in (v0, resistencia, capacitancia_uf, tiempo)):
                    raise ValueError("Los parámetros del circuito deben ser finitos.")
                if resistencia <= 0 or capacitancia_uf <= 0:
                    raise ValueError("R y C deben ser mayores que cero.")
                if tiempo < 0:
                    raise ValueError("El tiempo no puede ser negativo.")
                capacitancia_f = capacitancia_uf * 1e-6
                constante_tiempo = resistencia * capacitancia_f
                x_rc = tiempo / constante_tiempo
                if not math.isfinite(x_rc):
                    raise ValueError("El cociente t/(RC) es demasiado grande.")
                funcion, x0, x = "exp(-x)", "0", str(x_rc)
                # Dejar visibles los datos realmente utilizados en el cálculo.
                self.ui.txtFuncion.setText(funcion)
                self.ui.txtX0.setText(x0)
                self.ui.txtX.setText(f"{x_rc:.12g}")

            x0_num = self.convertir_numero(x0)
            x_num = self.convertir_numero(x)
            resultado = taylor(
                funcion=funcion, x0=x0, x=x,
                orden_maximo=orden, cifras=cifras,
            )
            filas = resultado["resultados"]
            self.ui.tablaResultados.setRowCount(len(filas))
            for i, fila in enumerate(filas):
                valores = [
                    str(fila["orden"]),
                    f'{fila["termino"]:.9f}',
                    f'{fila["aproximacion"]:.9f}',
                    f'{fila["error_verdadero"]:.9f}',
                    self.formatear_error(fila["error_relativo_verdadero"]),
                    self.formatear_error(fila["error_aproximado"]),
                    f'{fila["residuo"]:.9f}',
                ]
                for columna, valor in enumerate(valores):
                    celda = QTableWidgetItem(valor)
                    celda.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    if i == resultado["orden_requerido"]:
                        celda.setBackground(QColor(35, 103, 71))
                    self.ui.tablaResultados.setItem(i, columna, celda)

            orden_requerido = resultado["orden_requerido"]
            if orden_requerido is None:
                mensaje = (
                    f'Valor verdadero: {resultado["valor_verdadero"]:.9f}\n'
                    f'No se alcanzó la tolerancia de {resultado["tolerancia"]} % '
                    f'con orden máximo {orden}.'
                )
            else:
                fila = filas[orden_requerido]
                mensaje = (
                    f'Valor verdadero: {resultado["valor_verdadero"]:.9f}\n'
                    f'Orden requerido: {orden_requerido}\n'
                    f'Términos necesarios: {orden_requerido + 1}\n'
                    f'Aproximación: {fila["aproximacion"]:.9f}\n'
                    f'Error aproximado: {abs(fila["error_aproximado"]):.6f} % '
                    f'| Tolerancia: {resultado["tolerancia"]} %'
                )
            if caso_rc:
                # El algoritmo aproxima e^(-x) y aquí lo convertimos a voltios.
                aproximacion_relativa = (
                    filas[orden_requerido]["aproximacion"]
                    if orden_requerido is not None
                    else filas[-1]["aproximacion"]
                )
                voltaje_real = v0 * math.exp(-x_rc)
                voltaje_taylor = v0 * aproximacion_relativa
                mensaje += (
                    f"\nCircuito RC: V0={v0:.6g} V; "
                    f"R={resistencia:.6g} Ω; C={capacitancia_uf:.6g} µF"
                    f"\nConstante de tiempo RC={constante_tiempo:.9g} s; "
                    f"t={tiempo:.9g} s; t/(RC)={x_rc:.9g}"
                    f"\nVoltaje verdadero: {voltaje_real:.9f} V"
                    f"\nVoltaje aproximado: {voltaje_taylor:.9f} V"
                )
                if abs(tiempo - constante_tiempo) <= 1e-9 * max(1.0, constante_tiempo):
                    mensaje += "\nCaso t = RC: el capacitor conserva aprox. 36.79 % de V0."
            self.ui.lblResultado.setText(mensaje)

            grafica_funcion(self.figuras[0], funcion, x0_num, x_num, orden)
            grafica_error(self.figuras[1], filas)
            grafica_truncamiento(self.figuras[2], funcion, x0_num, min(3, orden))
            for lienzo in self.lienzos:
                lienzo.draw()
            self.resultado_actual = resultado

        except Exception as error:
            QMessageBox.warning(self, "Error de cálculo", str(error))

    @staticmethod
    def formatear_error(valor):
        return "N/D" if valor is None else f"{valor:.6f}"

    def limpiar(self):
        self.ui.cmbEjemplos.setCurrentIndex(3)  # Personalizado
        self.ui.txtFuncion.clear()
        self.ui.txtX0.clear()
        self.ui.txtX.clear()
        self.ui.tablaResultados.setRowCount(0)
        self.ui.lblResultado.setText("Ingresa una función y presiona Calcular Taylor.")
        self.resultado_actual = None
        for figura, lienzo in zip(self.figuras, self.lienzos):
            figura.clear()
            lienzo.draw()

    def exportar_csv(self):
        if self.resultado_actual is None:
            QMessageBox.information(self, "Sin datos", "Primero realiza un cálculo.")
            return
        ruta, _ = QFileDialog.getSaveFileName(
            self, "Guardar resultados", "resultados_taylor.csv", "CSV (*.csv)"
        )
        if not ruta:
            return
        try:
            with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([
                    "Orden n", "Término", "P_n(x)", "Error verdadero",
                    "Error verdadero (%)", "Error aproximado (%)", "Residuo estimado",
                ])
                for fila in self.resultado_actual["resultados"]:
                    escritor.writerow([
                        fila["orden"], fila["termino"], fila["aproximacion"],
                        fila["error_verdadero"],
                        fila["error_relativo_verdadero"],
                        fila["error_aproximado"], fila["residuo"],
                    ])
            QMessageBox.information(self, "CSV guardado", f"Archivo guardado en:\n{ruta}")
        except OSError as error:
            QMessageBox.warning(self, "No se pudo exportar", str(error))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
