# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QScrollArea, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1320, 880)
        self.scrollPrincipal = QScrollArea(MainWindow)
        self.scrollPrincipal.setObjectName(u"scrollPrincipal")
        self.scrollPrincipal.setWidgetResizable(True)
        self.scrollPrincipal.setFrameShape(QFrame.Shape.NoFrame)
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutPrincipal = QVBoxLayout(self.centralwidget)
        self.layoutPrincipal.setSpacing(9)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutPrincipal.addWidget(self.lblTitulo)

        self.lblSubtitulo = QLabel(self.centralwidget)
        self.lblSubtitulo.setObjectName(u"lblSubtitulo")
        self.lblSubtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutPrincipal.addWidget(self.lblSubtitulo)

        self.layoutEntradas = QHBoxLayout()
        self.layoutEntradas.setObjectName(u"layoutEntradas")
        self.grupoMetodo = QGroupBox(self.centralwidget)
        self.grupoMetodo.setObjectName(u"grupoMetodo")
        self.gridMetodo = QGridLayout(self.grupoMetodo)
        self.gridMetodo.setObjectName(u"gridMetodo")
        self.spinOrden = QSpinBox(self.grupoMetodo)
        self.spinOrden.setObjectName(u"spinOrden")
        self.spinOrden.setMaximum(15)
        self.spinOrden.setValue(15)

        self.gridMetodo.addWidget(self.spinOrden, 4, 1, 1, 1)

        self.lblOrden = QLabel(self.grupoMetodo)
        self.lblOrden.setObjectName(u"lblOrden")

        self.gridMetodo.addWidget(self.lblOrden, 4, 0, 1, 1)

        self.txtFuncion = QLineEdit(self.grupoMetodo)
        self.txtFuncion.setObjectName(u"txtFuncion")

        self.gridMetodo.addWidget(self.txtFuncion, 1, 1, 1, 1)

        self.label_txtX0 = QLabel(self.grupoMetodo)
        self.label_txtX0.setObjectName(u"label_txtX0")

        self.gridMetodo.addWidget(self.label_txtX0, 2, 0, 1, 1)

        self.lblCifras = QLabel(self.grupoMetodo)
        self.lblCifras.setObjectName(u"lblCifras")

        self.gridMetodo.addWidget(self.lblCifras, 5, 0, 1, 1)

        self.label_txtX = QLabel(self.grupoMetodo)
        self.label_txtX.setObjectName(u"label_txtX")

        self.gridMetodo.addWidget(self.label_txtX, 3, 0, 1, 1)

        self.label_txtFuncion = QLabel(self.grupoMetodo)
        self.label_txtFuncion.setObjectName(u"label_txtFuncion")

        self.gridMetodo.addWidget(self.label_txtFuncion, 1, 0, 1, 1)

        self.txtX0 = QLineEdit(self.grupoMetodo)
        self.txtX0.setObjectName(u"txtX0")

        self.gridMetodo.addWidget(self.txtX0, 2, 1, 1, 1)

        self.spinCifras = QSpinBox(self.grupoMetodo)
        self.spinCifras.setObjectName(u"spinCifras")
        self.spinCifras.setMinimum(1)
        self.spinCifras.setMaximum(15)
        self.spinCifras.setValue(3)

        self.gridMetodo.addWidget(self.spinCifras, 5, 1, 1, 1)

        self.txtX = QLineEdit(self.grupoMetodo)
        self.txtX.setObjectName(u"txtX")

        self.gridMetodo.addWidget(self.txtX, 3, 1, 1, 1)

        self.lblEjemplos = QLabel(self.grupoMetodo)
        self.lblEjemplos.setObjectName(u"lblEjemplos")

        self.gridMetodo.addWidget(self.lblEjemplos, 0, 0, 1, 1)

        self.cmbEjemplos = QComboBox(self.grupoMetodo)
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.setObjectName(u"cmbEjemplos")

        self.gridMetodo.addWidget(self.cmbEjemplos, 0, 1, 1, 1)


        self.layoutEntradas.addWidget(self.grupoMetodo)

        self.grupoRC = QGroupBox(self.centralwidget)
        self.grupoRC.setObjectName(u"grupoRC")
        self.gridRC = QGridLayout(self.grupoRC)
        self.gridRC.setObjectName(u"gridRC")
        self.lbl_spinV0 = QLabel(self.grupoRC)
        self.lbl_spinV0.setObjectName(u"lbl_spinV0")

        self.gridRC.addWidget(self.lbl_spinV0, 0, 0, 1, 1)

        self.spinV0 = QDoubleSpinBox(self.grupoRC)
        self.spinV0.setObjectName(u"spinV0")
        self.spinV0.setDecimals(6)
        self.spinV0.setMinimum(0.000000000000000)
        self.spinV0.setMaximum(1000000000.000000000000000)
        self.spinV0.setValue(12.000000000000000)

        self.gridRC.addWidget(self.spinV0, 0, 1, 1, 1)

        self.lbl_spinR = QLabel(self.grupoRC)
        self.lbl_spinR.setObjectName(u"lbl_spinR")

        self.gridRC.addWidget(self.lbl_spinR, 1, 0, 1, 1)

        self.spinR = QDoubleSpinBox(self.grupoRC)
        self.spinR.setObjectName(u"spinR")
        self.spinR.setDecimals(6)
        self.spinR.setMinimum(0.000000000000000)
        self.spinR.setMaximum(1000000000.000000000000000)
        self.spinR.setValue(1000.000000000000000)

        self.gridRC.addWidget(self.spinR, 1, 1, 1, 1)

        self.lbl_spinC = QLabel(self.grupoRC)
        self.lbl_spinC.setObjectName(u"lbl_spinC")

        self.gridRC.addWidget(self.lbl_spinC, 2, 0, 1, 1)

        self.spinC = QDoubleSpinBox(self.grupoRC)
        self.spinC.setObjectName(u"spinC")
        self.spinC.setDecimals(6)
        self.spinC.setMinimum(0.000000000000000)
        self.spinC.setMaximum(1000000000.000000000000000)
        self.spinC.setValue(1000.000000000000000)

        self.gridRC.addWidget(self.spinC, 2, 1, 1, 1)

        self.lbl_spinTiempo = QLabel(self.grupoRC)
        self.lbl_spinTiempo.setObjectName(u"lbl_spinTiempo")

        self.gridRC.addWidget(self.lbl_spinTiempo, 3, 0, 1, 1)

        self.spinTiempo = QDoubleSpinBox(self.grupoRC)
        self.spinTiempo.setObjectName(u"spinTiempo")
        self.spinTiempo.setDecimals(6)
        self.spinTiempo.setMinimum(0.000000000000000)
        self.spinTiempo.setMaximum(1000000000.000000000000000)
        self.spinTiempo.setValue(1.000000000000000)

        self.gridRC.addWidget(self.spinTiempo, 3, 1, 1, 1)

        self.lblRCInfo = QLabel(self.grupoRC)
        self.lblRCInfo.setObjectName(u"lblRCInfo")
        self.lblRCInfo.setWordWrap(True)

        self.gridRC.addWidget(self.lblRCInfo, 4, 0, 1, 2)


        self.layoutEntradas.addWidget(self.grupoRC)


        self.layoutPrincipal.addLayout(self.layoutEntradas)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnCalcular = QPushButton(self.centralwidget)
        self.btnCalcular.setObjectName(u"btnCalcular")

        self.layoutBotones.addWidget(self.btnCalcular)

        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.layoutBotones.addWidget(self.btnLimpiar)

        self.btnExportar = QPushButton(self.centralwidget)
        self.btnExportar.setObjectName(u"btnExportar")

        self.layoutBotones.addWidget(self.btnExportar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.grupoResumen = QGroupBox(self.centralwidget)
        self.grupoResumen.setObjectName(u"grupoResumen")
        self.layoutResumen = QVBoxLayout(self.grupoResumen)
        self.layoutResumen.setObjectName(u"layoutResumen")
        self.lblResultado = QLabel(self.grupoResumen)
        self.lblResultado.setObjectName(u"lblResultado")
        self.lblResultado.setWordWrap(True)

        self.layoutResumen.addWidget(self.lblResultado)


        self.layoutPrincipal.addWidget(self.grupoResumen)

        self.layoutDatosGraficas = QVBoxLayout()
        self.layoutDatosGraficas.setObjectName(u"layoutDatosGraficas")
        self.grupoTabla = QGroupBox(self.centralwidget)
        self.grupoTabla.setObjectName(u"grupoTabla")
        self.layoutTabla = QVBoxLayout(self.grupoTabla)
        self.layoutTabla.setObjectName(u"layoutTabla")
        self.tablaResultados = QTableWidget(self.grupoTabla)
        if (self.tablaResultados.columnCount() < 7):
            self.tablaResultados.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tablaResultados.setObjectName(u"tablaResultados")
        self.tablaResultados.setRowCount(0)
        self.tablaResultados.setColumnCount(7)

        self.tablaResultados.setMinimumHeight(300)
        self.layoutTabla.addWidget(self.tablaResultados)


        self.layoutDatosGraficas.addWidget(self.grupoTabla)

        self.grupoGraficas = QGroupBox(self.centralwidget)
        self.grupoGraficas.setObjectName(u"grupoGraficas")
        self.layoutGraficas = QVBoxLayout(self.grupoGraficas)
        self.layoutGraficas.setObjectName(u"layoutGraficas")
        self.tabsGraficas = QTabWidget(self.grupoGraficas)
        self.tabsGraficas.setObjectName(u"tabsGraficas")
        self.tabTaylor = QWidget()
        self.tabTaylor.setObjectName(u"tabTaylor")
        self.layout_tabTaylor = QVBoxLayout(self.tabTaylor)
        self.layout_tabTaylor.setObjectName(u"layout_tabTaylor")
        self.widgetGraficaTaylor = QWidget(self.tabTaylor)
        self.widgetGraficaTaylor.setObjectName(u"widgetGraficaTaylor")
        self.widgetGraficaTaylor.setMinimumHeight(475)

        self.layout_tabTaylor.addWidget(self.widgetGraficaTaylor)

        self.tabsGraficas.addTab(self.tabTaylor, "")
        self.tabError = QWidget()
        self.tabError.setObjectName(u"tabError")
        self.layout_tabError = QVBoxLayout(self.tabError)
        self.layout_tabError.setObjectName(u"layout_tabError")
        self.widgetGraficaError = QWidget(self.tabError)
        self.widgetGraficaError.setObjectName(u"widgetGraficaError")
        self.widgetGraficaError.setMinimumHeight(475)

        self.layout_tabError.addWidget(self.widgetGraficaError)

        self.tabsGraficas.addTab(self.tabError, "")
        self.tabTruncamiento = QWidget()
        self.tabTruncamiento.setObjectName(u"tabTruncamiento")
        self.layout_tabTruncamiento = QVBoxLayout(self.tabTruncamiento)
        self.layout_tabTruncamiento.setObjectName(u"layout_tabTruncamiento")
        self.widgetGraficaTruncamiento = QWidget(self.tabTruncamiento)
        self.widgetGraficaTruncamiento.setObjectName(u"widgetGraficaTruncamiento")
        self.widgetGraficaTruncamiento.setMinimumHeight(475)

        self.layout_tabTruncamiento.addWidget(self.widgetGraficaTruncamiento)

        self.tabsGraficas.addTab(self.tabTruncamiento, "")

        self.tabsGraficas.setMinimumHeight(550)
        self.layoutGraficas.addWidget(self.tabsGraficas)


        self.layoutDatosGraficas.addWidget(self.grupoGraficas)


        self.layoutPrincipal.addLayout(self.layoutDatosGraficas)

        self.lblNotaErrores = QLabel(self.centralwidget)
        self.lblNotaErrores.setObjectName(u"lblNotaErrores")
        self.lblNotaErrores.setWordWrap(True)

        self.layoutPrincipal.addWidget(self.lblNotaErrores)

        self.scrollPrincipal.setWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.scrollPrincipal)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1320, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabsGraficas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Taylor RC - Grupo 2 | C\u00e1lculo Num\u00e9rico", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"SERIES DE TAYLOR Y ERROR DE TRUNCAMIENTO", None))
        self.lblSubtitulo.setText(QCoreApplication.translate("MainWindow", u"C\u00e1lculo Num\u00e9rico \u00b7 Proyecto A \u00b7 Grupo 2 \u2014 Descarga de capacitor RC", None))
        self.grupoMetodo.setTitle(QCoreApplication.translate("MainWindow", u"Par\u00e1metros de Taylor", None))
        self.lblOrden.setText(QCoreApplication.translate("MainWindow", u"Orden m\u00e1ximo n:", None))
        self.txtFuncion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej. exp(-x), cos(x), sin(x)", None))
        self.label_txtX0.setText(QCoreApplication.translate("MainWindow", u"Punto base x\u2080:", None))
        self.lblCifras.setText(QCoreApplication.translate("MainWindow", u"Cifras significativas (s):", None))
        self.label_txtX.setText(QCoreApplication.translate("MainWindow", u"Evaluar en x:", None))
        self.label_txtFuncion.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n f(x):", None))
        self.txtX0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej. 0 o pi/4", None))
        self.txtX.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej. 1 o pi/3", None))
        self.lblEjemplos.setText(QCoreApplication.translate("MainWindow", u"Ejemplo precargado:", None))
        self.cmbEjemplos.setItemText(0, QCoreApplication.translate("MainWindow", u"Descarga RC (grupo 2)", None))
        self.cmbEjemplos.setItemText(1, QCoreApplication.translate("MainWindow", u"Ejemplo del libro: cos(x)", None))
        self.cmbEjemplos.setItemText(2, QCoreApplication.translate("MainWindow", u"Scarborough: exp(x)", None))
        self.cmbEjemplos.setItemText(3, QCoreApplication.translate("MainWindow", u"Personalizado", None))

        self.grupoRC.setTitle(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n f\u00edsica: descarga del capacitor RC", None))
        self.lbl_spinV0.setText(QCoreApplication.translate("MainWindow", u"Voltaje inicial V\u2080:", None))
        self.spinV0.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.lbl_spinR.setText(QCoreApplication.translate("MainWindow", u"Resistencia R:", None))
        self.spinR.setSuffix(QCoreApplication.translate("MainWindow", u" \u03a9", None))
        self.lbl_spinC.setText(QCoreApplication.translate("MainWindow", u"Capacitancia C:", None))
        self.spinC.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b5F", None))
        self.lbl_spinTiempo.setText(QCoreApplication.translate("MainWindow", u"Tiempo t:", None))
        self.spinTiempo.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.lblRCInfo.setText(QCoreApplication.translate("MainWindow", u"En el caso obligatorio, t = RC y f(x) = exp(-x), con x = t/(RC).", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular Taylor", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnExportar.setText(QCoreApplication.translate("MainWindow", u"Exportar CSV", None))
        self.grupoResumen.setTitle(QCoreApplication.translate("MainWindow", u"Resultado y criterio de parada", None))
        self.lblResultado.setText(QCoreApplication.translate("MainWindow", u"Selecciona un ejemplo y presiona Calcular para ver resultados.", None))
        self.grupoTabla.setTitle(QCoreApplication.translate("MainWindow", u"Tabla de iteraciones de Taylor", None))
        ___qtablewidgetitem = self.tablaResultados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Orden n", None))
        ___qtablewidgetitem1 = self.tablaResultados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00e9rmino", None))
        ___qtablewidgetitem2 = self.tablaResultados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"P\u2099(x)", None))
        ___qtablewidgetitem3 = self.tablaResultados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Error E\u209c", None))
        ___qtablewidgetitem4 = self.tablaResultados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u03b5\u209c (%)", None))
        ___qtablewidgetitem5 = self.tablaResultados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u03b5\u2090 (%)", None))
        ___qtablewidgetitem6 = self.tablaResultados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Residuo R\u2099", None))
        self.grupoGraficas.setTitle(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficas del m\u00e9todo", None))
        self.tabTaylor.setProperty(u"title", QCoreApplication.translate("MainWindow", u"Funci\u00f3n y Taylor", None))
        self.tabsGraficas.setTabText(self.tabsGraficas.indexOf(self.tabTaylor), "Función y Taylor")
        self.tabError.setProperty(u"title", QCoreApplication.translate("MainWindow", u"Error vs. orden", None))
        self.tabsGraficas.setTabText(self.tabsGraficas.indexOf(self.tabError), "Error vs. orden")
        self.tabTruncamiento.setProperty(u"title", QCoreApplication.translate("MainWindow", u"Truncamiento", None))
        self.tabsGraficas.setTabText(self.tabsGraficas.indexOf(self.tabTruncamiento), "Truncamiento")
        self.lblNotaErrores.setText(QCoreApplication.translate("MainWindow", u"Truncamiento: error por cortar la serie. Redondeo: error por precisi\u00f3n finita en los c\u00e1lculos.", None))
    # retranslateUi

