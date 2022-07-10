from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem
                             ,QProgressBar)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QObject, QTimer, QMimeData)
from PyQt5.QtGui import (QPixmap, QFont, QMovie, QIcon, QFont, QDrag, QPainter, QCursor, QImage, QMouseEvent)
import parametros_generales as P
import sys
from PyQt5.QtTest import QTest


class usuario():
    def __init__(self):
        self.pausado = True #Para el lag
        pass

# P pared
# C cama
# S suelo
# D puerta
class VentanaCasa(QWidget):
    volver = pyqtSignal()
    pasar_dia = pyqtSignal()

    def keyPressEvent(self, event):
        self.procesar_letra(event.text())

    def __init__(self):
        super().__init__()
        self.pixeles = []
        self.setGui()

    def setGui(self):
        coord = []
        fil = 0
        self.N = 56
        self.setWindowIcon(QIcon(P.path_casa))
        self.setWindowTitle('Casa')
        fil = 0
        with open("mapa_casa.txt", encoding = "utf-8") as file:
            for line in file:
                fil += 1
                line = line.replace("\n", "")
                col = len(line.split(" "))
                coord.append(line.split(" "))

        self.setGeometry(550, 300 ,col *self.N ,fil *self.N) #revisar
        fila_n = -1
        columna = -1
        for fila in coord:
            fila_n += 1
            for pixel in fila:
                columna += 1
                if pixel == "P":
                    path = P.PATH_PARED
                    tipo = "pared"
                elif pixel == "S":
                    path = P.PATH_PISO
                    tipo = "piso"
                elif pixel == "D":
                    path = P.PATH_PUERTA
                    tipo = "puerta"
                    self.usuario = usuario()
                    self.usuario.fila = fila_n
                    self.usuario.columna = columna
                else:
                    path = P.PATH_CAMA
                    tipo = "cama"
                    pixel_casa = QLabel('pixel', self) #Agregar piso bajo la cama
                    imagen = QPixmap(P.PATH_PISO)
                    pixel_casa.setPixmap(imagen)
                    pixel_casa.setScaledContents(True)
                    pixel_casa.setGeometry(columna *self.N , fila_n *self.N, self.N, self.N)
                pixel_casa = QLabel('pixel', self)
                imagen = QPixmap(path)
                pixel_casa.setPixmap(imagen)
                pixel_casa.setScaledContents(True)
                pixel_casa.setGeometry(columna * self.N , fila_n * self.N, self.N, self.N)
                pixel_casa.tipo = tipo
                pixel_casa.fila = fila_n
                pixel_casa.columna = columna
                self.pixeles.append(pixel_casa)
            columna = -1
        self.png_usuario = QLabel('usuario', self)
        imagen = QPixmap(P.usuario["up_1"])
        self.png_usuario.setPixmap(imagen)
        self.png_usuario.setScaledContents(True)
        self.png_usuario.setGeometry(self.usuario.columna * self.N + self.N / 5 , self.usuario.fila * self.N + self.N / 5, 2 * self.N / 3, 2 * self.N / 3)


    def procesar_letra(self, letra):
        if not self.pausado:
            puede = False
            if letra == "w" or letra == "W":
                self.accion = "arriba"
                puede = True
            elif letra == "a" or letra == "A":
                self.accion = "izquierda"
                puede = True
            elif letra == "s" or letra == "S":
                self.accion = "abajo"
                puede = True
            elif letra == "d" or letra == "D":
                self.accion = "derecha"
                puede = True
            if puede:
                self.mover(self.accion)

    def mover(self, accion):
        puede = self.revisar_movimiento()
        if puede:
            if accion == "derecha":
                imagen_2 = QPixmap(P.usuario["right_2"])
                imagen_us = QPixmap(P.usuario["right_1"])
                fila2 = self.usuario.fila
                columna2 = int(self.usuario.columna) + P.VEL_MOVIMIENTO / 2
                self.usuario.columna += P.VEL_MOVIMIENTO
            elif accion == "izquierda":
                imagen_2 = QPixmap(P.usuario["left_2"])
                imagen_us = QPixmap(P.usuario["left_1"])
                columna2 = int(self.usuario.columna) - P.VEL_MOVIMIENTO / 2
                fila2 = self.usuario.fila
                self.usuario.columna -= P.VEL_MOVIMIENTO
            elif accion == "arriba":
                imagen_2 = QPixmap(P.usuario["up_2"])
                imagen_us = QPixmap(P.usuario["up_1"])
                columna2 = self.usuario.columna
                fila2 = int(self.usuario.fila) - P.VEL_MOVIMIENTO/2
                self.usuario.fila -= P.VEL_MOVIMIENTO
            else:
                imagen_2 = QPixmap(P.usuario["down_2"])
                imagen_us = QPixmap(P.usuario["down_1"])
                fila2 = int(self.usuario.fila) + P.VEL_MOVIMIENTO/2
                columna2 = self.usuario.columna
                self.usuario.fila += P.VEL_MOVIMIENTO
            self.png_usuario.setPixmap(imagen_2)
            self.png_usuario.move(self.N * columna2, self.N * fila2)
            QTest.qWait(100)
            #pasar tiempo
            self.png_usuario.setPixmap(imagen_us)
            self.png_usuario.move(self.N * self.usuario.columna, self.N * self.usuario.fila)
            if self.puerta:
                self.volver_campo()
            elif self.cama:
                self.dormir()

    def revisar_movimiento(self):
        self.cama = False
        self.puerta = False
        if self.accion == "arriba":
            for pixel in self.pixeles:
                if pixel.columna == self.usuario.columna:
                    if (pixel.fila < self.usuario.fila) and (pixel.fila >= (self.usuario.fila - P.VEL_MOVIMIENTO)):
                        if pixel.tipo == "piso":
                            return True
                        elif pixel.tipo == "cama":
                            self.cama = True
                            return True
                        elif pixel.tipo == "puerta":
                            self.puerta = True
                            return True
            return False
        if self.accion == "abajo":
            for pixel in self.pixeles:
                if pixel.columna == self.usuario.columna:
                    if (pixel.fila > self.usuario.fila) and (pixel.fila <= (self.usuario.fila + P.VEL_MOVIMIENTO)):
                        if pixel.tipo == "piso":
                            return True
                        elif pixel.tipo == "cama":
                            self.cama = True
                            return True
                        elif pixel.tipo == "puerta":
                            self.puerta = True
                            return True
            return False
        if self.accion == "izquierda":
            for pixel in self.pixeles:
                if pixel.fila == self.usuario.fila:
                    if (pixel.columna < self.usuario.columna) and (pixel.columna >= (self.usuario.columna - P.VEL_MOVIMIENTO)):
                        if pixel.tipo == "piso":
                            return True
                        elif pixel.tipo == "cama":
                            self.cama = True
                            return True
                        elif pixel.tipo == "puerta":
                            self.puerta = True
                            return True
            return False
        if self.accion == "derecha":
            for pixel in self.pixeles:
                if pixel.fila == self.usuario.fila:
                    if (pixel.columna > self.usuario.columna) and (pixel.columna <= self.usuario.columna + P.VEL_MOVIMIENTO):
                        if pixel.tipo == "piso":
                            return True
                        elif pixel.tipo == "cama":
                            self.cama = True
                            return True
                        elif pixel.tipo == "puerta":
                            self.puerta = True
                            return True
            return False
    def dormir(self):
        print("Te fuiste a dormir")
        self.pasar_dia.emit()
    def volver_campo(self):
        self.pausado = True
        self.hide()
        self.volver.emit()
    def entrar(self):
        self.pausado = False
        self.show()
