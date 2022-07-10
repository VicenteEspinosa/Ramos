from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
import os
import sys
import parametros_generales as P


class VentanaInicio(QWidget):
    revisar_mapa = pyqtSignal(str)
    iniciar_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):

        self.setGeometry(400, 300, 500, 350)
        self.setWindowTitle('Seleccionar mapa')

        self.logo = QLabel('foto', self)
        imagen = QPixmap(P.path_logo)
        self.logo.setPixmap(imagen)

        self.Ingresar_mapa = QLabel(str("Ingesar nombre del mapa a cargar:"), self)
        self.Ingresar_mapa.resize(self.Ingresar_mapa.sizeHint())

        self.mapa = QLineEdit()
        self.mapa.resize(self.mapa.sizeHint())

        self.boton_mapa = QPushButton('Jugar', self)
        self.boton_mapa.clicked.connect(self.Seleccionar_Mapa)

        self.Mensaje = QLabel(str(""), self)
        self.Mensaje.resize(self.Mensaje.sizeHint())

        layout_input= QVBoxLayout()
        layout_input.setSpacing(0)
        layout_input.addWidget(self.Ingresar_mapa)
        layout_input.addWidget(self.mapa)
        layout_input.addWidget(self.boton_mapa)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.logo)
        layout.addStretch(1)
        layout.addLayout(layout_input)
        layout.addWidget(self.Mensaje)
        layout.addStretch(1)

        layout1 = QHBoxLayout()
        layout1.addStretch(1)
        layout1.addLayout(layout)
        layout1.addStretch(1)


        self.setLayout(layout1)

    def Seleccionar_Mapa(self):
        self.texto_mapa = self.mapa.text()
        self.mapa.setText("")
        self.revisar_mapa.emit(self.texto_mapa)

    def Actualizar_mensaje(self, mensaje):
        self.Mensaje.setText(mensaje)
        if mensaje == "Cargando mapa...":
            self.iniciar_juego.emit(self.texto_mapa)
            self.close()
