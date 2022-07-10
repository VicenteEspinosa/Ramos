import parametros_generales as P
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QObject)
from PyQt5.QtGui import (QPixmap, QFont, QMovie, QIcon)

class usuario(QObject):
    def __init__(self, pixeles):
        super().__init__()
        self.hacha = 0
        self.azada = 0
        self.alcachofa = 0
        self.choclo = 0
        self.oro = 0
        self.madera = 0
        self.semilla_alcachofa = 0
        self.semilla_choclo = 0
        self.dinero = P.MONEDAS_INICIALES
        self.energia = P.ENERGIA_JUGADOR
        self.cargar_ubicacion_inicial(pixeles)

    def cargar_ubicacion_inicial(self, pixeles):
        for pixel in pixeles:
            if pixel.tipo == "libre":
                self.columna = int(pixel.columna)
                self.fila = int(pixel.fila)
                break

    def gastar_energia(self, energia):
        self.energia -= energia
        if self.energia < 0:
            self.energia = 0
