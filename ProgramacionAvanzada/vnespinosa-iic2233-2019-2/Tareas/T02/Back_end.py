from PyQt5.QtCore import (QObject, pyqtSignal, pyqtSignal, Qt, QRect)
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
import os
import sys


#Para la pantalla de incio
class Procesos(QObject):
    Respuesta_select_mapa = pyqtSignal(str)
    Respuesta_cargar_mapa = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def check_mapa(self, mapa):
        if mapa.replace(" ","") == "":
             Mensaje = "Por favor ingresa un nombre"
        else:
            if not os.path.isfile(os.path.join("mapas", mapa)):
                Mensaje = "No existe un archivo con ese nombre, por favor ingresa uno existente"
            else:
                Mensaje = "Cargando mapa..."
        self.Respuesta_cargar_mapa.emit(Mensaje)


    def Cargar_mapa(self, mapa):
        coord = []
        fil = 0
        with open(self.mapa, encoding="utf-8") as file:
            for line in file:
                fil += 1
                line = line.replace("\n", "")
                col = len(line.split(" "))
                coord.append(line.split(" "))
        dict = {"fil": fil,
            "col": col,
            "coord": coord}
        self.Respuesta_select_mapa.emit(coord)
