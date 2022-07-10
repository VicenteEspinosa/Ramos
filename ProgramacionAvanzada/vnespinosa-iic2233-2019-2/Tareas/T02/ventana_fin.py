from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem
                             ,QProgressBar)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QObject, QTimer)
from PyQt5.QtGui import (QPixmap, QFont, QMovie, QIcon, QFont)
import os
import sys
import parametros_generales as P

class VentanaFin(QWidget):

    def __init__(self):
        super().__init__()


    def setGui(self, tipo):
        self.fondo = QLabel('fondo', self)
        imagen = QPixmap(P.path_fondo)
        self.fondo.setPixmap(imagen)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 800, 600)

        self.tipo = tipo
        self.setGeometry(550, 300 ,800 ,600)
        self.setWindowTitle('FIN DEL JUEGO')
        if self.tipo == "victoria":
            mensaje = "Felicidades, ganaste el juego!!"
        elif self.tipo == "derrota":
            mensaje = "Te desmallaste, perdiste el juego"

        self.boton_salir = QPushButton('Cerrar Juego', self)
        self.boton_salir.clicked.connect(self.Cerrar)
        self.boton_salir.resize(120,80)
        self.boton_salir.move(340, 300)

        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)

        self.mensaje = QLabel(mensaje, self)
        self.mensaje.setFont(font)
        self.mensaje.resize(self.mensaje.sizeHint())
        self.mensaje.move(200, 140)
        self.show()

    def Cerrar(self):
        self.close()
