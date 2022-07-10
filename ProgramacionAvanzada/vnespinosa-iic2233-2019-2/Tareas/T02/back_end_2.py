import parametros_generales as P
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem
                             ,QProgressBar)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QObject, QTimer, QMimeData)
from PyQt5.QtGui import (QPixmap, QFont, QMovie, QIcon, QFont, QDrag, QPainter, QCursor, QImage, QMouseEvent)
import random
from Usuario import usuario
from Pixeles import Pixel
import parametros_plantas
import parametros_acciones
from PyQt5.QtTest import QTest

class ClickMadera(QLabel):
  clicked = pyqtSignal(object)
  def __init(self, parent):
    QLabel.__init__(self, QMouseEvent)
  def mousePressEvent(self, ev):
      self.clicked.emit(self)


class Back_end_juego_2(QObject):
    entrar_casa = pyqtSignal()
    abrir_tienda = pyqtSignal()
    pasar_dia = pyqtSignal()

    def __init__(self):
        super().__init__()

    def mover_usuario(self, ventana):
        self.tienda = False
        self.casa = False
        puede = self.revisar_movimiento(ventana)
        if puede:
            if ventana.direccion == "arriba":
                imagen_2 = QPixmap(P.usuario["up_2"])
                imagen_us = QPixmap(P.usuario["up_1"])
                columna2 = ventana.usuario.columna
                fila2 = int(ventana.usuario.fila) - P.VEL_MOVIMIENTO/2
                ventana.usuario.fila -= P.VEL_MOVIMIENTO
            elif ventana.direccion == "abajo":
                imagen_2 = QPixmap(P.usuario["down_2"])
                imagen_us = QPixmap(P.usuario["down_1"])
                fila2 = int(ventana.usuario.fila) + P.VEL_MOVIMIENTO/2
                columna2 = ventana.usuario.columna
                ventana.usuario.fila += P.VEL_MOVIMIENTO
            elif ventana.direccion == "izquierda":
                imagen_2 = QPixmap(P.usuario["left_2"])
                imagen_us = QPixmap(P.usuario["left_1"])
                columna2 = int(ventana.usuario.columna) - P.VEL_MOVIMIENTO / 2
                fila2 = ventana.usuario.fila
                ventana.usuario.columna -= P.VEL_MOVIMIENTO
            elif ventana.direccion == "derecha":
                imagen_2 = QPixmap(P.usuario["right_2"])
                imagen_us = QPixmap(P.usuario["right_1"])
                fila2 = ventana.usuario.fila
                columna2 = int(ventana.usuario.columna) + P.VEL_MOVIMIENTO / 2
                ventana.usuario.columna += P.VEL_MOVIMIENTO
            ventana.png_usuario.setPixmap(imagen_2)
            ventana.png_usuario.move(P.N * columna2 + P.margen, P.N * fila2 + P.margen)
            QTest.qWait(100)
            #pasar tiempo
            ventana.png_usuario.setPixmap(imagen_us)
            ventana.png_usuario.move(P.N * ventana.usuario.columna + P.margen, P.N
                * ventana.usuario.fila + P.margen)
            self.revisar_pisar_drop(ventana)
        else:
            print("No te puedes mover hacia alla!")
        if self.casa:
            print("Entraste a la casa")
            ventana.hide()
            self.entrar_casa.emit()
            pass
        elif self.tienda:
            self.abrir_tienda.emit()
            print("Entraste tienda")
            pass

    def revisar_movimiento(self, ventana):
        if ventana.direccion == "arriba":
            for pixel in ventana.pixeles:
                if pixel.columna == ventana.usuario.columna:
                    if (pixel.fila < ventana.usuario.fila) and (pixel.fila
                        >= (ventana.usuario.fila - P.VEL_MOVIMIENTO)):
                        if pixel.tipo == "libre" or pixel.tipo == "cultivable" or pixel.tipo == "arable":
                            puede = True
                            for drop in ventana.drops:
                                if drop.fila == pixel.fila:
                                    if drop.columna == pixel.columna:
                                        if drop.tipo == "arbol":
                                            puede = False
                            return puede
                        elif pixel.tipo == "tienda":
                            self.tienda = True
                            return True
                        elif pixel.tipo == "casa":
                            self.casa = True
                            return True
            return False

        if ventana.direccion == "abajo":
            for pixel in ventana.pixeles:
                if pixel.columna == ventana.usuario.columna:
                    if (pixel.fila > ventana.usuario.fila) and (pixel.fila
                        <= (ventana.usuario.fila + P.VEL_MOVIMIENTO)):
                        if pixel.tipo == "libre" or pixel.tipo == "cultivable" or pixel.tipo == "arable":
                            puede = True
                            for drop in ventana.drops:
                                if drop.fila == pixel.fila:
                                    if drop.columna == pixel.columna:
                                        if drop.tipo == "arbol":
                                            puede = False
                            return puede
                        elif pixel.tipo == "tienda":
                            self.tienda = True
                            return True
                        elif pixel.tipo == "casa":
                            self.casa = True
                            return True
            return False

        if ventana.direccion == "izquierda":
            for pixel in ventana.pixeles:
                if pixel.fila == ventana.usuario.fila:
                    if (pixel.columna < ventana.usuario.columna) and (pixel.columna
                        >= (ventana.usuario.columna - P.VEL_MOVIMIENTO)):
                        if pixel.tipo == "libre" or pixel.tipo == "cultivable" or pixel.tipo == "arable":
                            puede = True
                            for drop in ventana.drops:
                                if drop.fila == pixel.fila:
                                    if drop.columna == pixel.columna:
                                        if drop.tipo == "arbol":
                                            puede = False
                            return puede
                        elif pixel.tipo == "tienda":
                            self.tienda = True
                            return True
                        elif pixel.tipo == "casa":
                            self.casa = True
                            return True
            return False

        if ventana.direccion == "derecha":
            for pixel in ventana.pixeles:
                if pixel.fila == ventana.usuario.fila:
                    if (pixel.columna > ventana.usuario.columna) and (pixel.columna
                        <= ventana.usuario.columna + P.VEL_MOVIMIENTO):
                        if pixel.tipo == "libre" or pixel.tipo == "cultivable" or pixel.tipo == "arable":
                            puede = True
                            for drop in ventana.drops:
                                if drop.fila == pixel.fila:
                                    if drop.columna == pixel.columna:
                                        if drop.tipo == "arbol":
                                            puede = False
                            return puede
                        elif pixel.tipo == "tienda":
                            self.tienda = True
                            return True
                        elif pixel.tipo == "casa":
                            self.casa = True
                            return True
            return False

    def procesar_key(self, ventana):
        key = ventana.keylist
        truco_1 = False
        truco_2 = False
        if len(key) == 3:
            if ("k" in key or "K" in key) and ("i" in key or "I" in key) and ("p" in key or "P" in key):
                truco_1 = True
            elif ("m" in key or "M" in key) and ("n" in key or "N" in key) and ("y" in key or "Y" in key):
                truco_2 = True
            if truco_1:
                print("Ejecutar truco energia")
                ventana.usuario.energia = int(P.ENERGIA_JUGADOR)
                ventana.actualizar_energia()
            elif truco_2:
                print("Ejecutar truco dinero")
                ventana.usuario.dinero += P.DINERO_TRAMPA
                ventana.Actualizar_dinero()
        elif len(key) == 1:
            if key[0] == "w" or key[0] == "W":
                ventana.direccion = "arriba"
                ventana.mover.emit(ventana)
            elif key[0] == "a" or key[0] == "A":
                ventana.direccion = "izquierda"
                ventana.mover.emit(ventana)
            elif key[0] == "s" or key[0] == "S":
                ventana.direccion = "abajo"
                ventana.mover.emit(ventana)
            elif key[0] == "d" or key[0] == "D":
                ventana.direccion = "derecha"
                ventana.mover.emit(ventana)

    def Agregar_cultivo(self, ventana):
        if ventana.cultivo_tipo == "alcachofa":
            path = P.path_inicial_alcachofa
            tiempo_nivel = parametros_plantas.TIEMPO_ALCACHOFAS
            tipo = "alcachofa"

        else:
            path = P.path_inicial_choclo
            tiempo_nivel = parametros_plantas.TIEMPO_CHOCLOS
            tipo = "choclo"
        cultivo =  QLabel('cultivo', ventana)
        imagen_cultivo = QPixmap(path)
        cultivo.setPixmap(imagen_cultivo)
        cultivo.setScaledContents(True)
        cultivo.setGeometry(ventana.cultivo_col * P.N + P.margen, ventana.cultivo_fil * P.N
            + P.margen, P.N, P.N)
        cultivo.tiempo_nivel = tiempo_nivel
        cultivo.tiempo = 0
        cultivo.nivel = 1
        cultivo.tipo = tipo
        cultivo.columna = int(ventana.cultivo_col)
        cultivo.fila = int(ventana.cultivo_fil)
        ventana.cultivos.append(cultivo)
        cultivo.show()

    def revisar_tiempo_drops(self, ventana):
        for drop in ventana.drops:
            if drop.tiempo == 0:
                drop.hide()
                ventana.drops.remove(drop)

    def revisar_pisar_drop(self, ventana):
        for drop in ventana.drops:
            if drop.fila == ventana.usuario.fila:
                if drop.columna == ventana.usuario.columna:
                    self.pisar_drop(ventana, drop)
                    #SEGUIR
    def pisar_drop(self, ventana, drop):
        ventana.usuario.energia -= parametros_acciones.ENERGIA_RECOGER
        ventana.actualizar_energia()
        if drop.tipo == "alcachofa":
            ventana.usuario.alcachofa += 1
        elif drop.tipo == "choclo":
            ventana.usuario.choclo += 1
            ventana.cultivos.append(drop.padre) #Reparar choclo
            drop.padre.tiempo = 0
            drop.padre.nivel = 6
            drop.padre.show()

        elif drop.tipo == "madera":
            ventana.usuario.madera += 1
        elif drop.tipo == "oro":
            ventana.usuario.oro += 1
        print("Recogiste " + str(drop.tipo))
        drop.hide()
        ventana.drops.remove(drop)
        ventana.actualizar_inventario.emit(ventana)

    def generar_drops_aleatorios(self, ventana):
        opciones = []
        n_arbol = random.random()
        n_oro = random.random()
        madera = False
        oro = False

        if P.PROB_ARBOL > n_arbol:
            madera = True
        if P.PROB_ORO > n_oro:
            oro = True
        if oro and madera:
            if (n_oro - P.PROB_ORO) > (n_arbol - P.PROB_ARBOL):
                madera = False
            else:
                oro = False
            for pixel in ventana.pixeles:
                funciona = False
                if pixel.tipo == "libre":
                    funciona = True
                    if pixel.columna == ventana.usuario.columna:
                        if pixel.fila == ventana.usuario.fila:
                            funciona = False
                if funciona:
                    for drop in ventana.drops:
                        if drop.columna == pixel.columna:
                            if drop.fila == pixel.fila:
                                funciona = False
                if funciona:
                    opciones.append(pixel)
            if len(opciones) > 0:
                pixel = random.choice(opciones)
                if oro:
                    self.generar_drop(ventana, "oro", pixel.columna, pixel.fila)
                    return True
                elif madera:
                    arbol = ClickMadera('arbol', ventana)
                    imagen = QPixmap(P.path_arbol)
                    arbol.setPixmap(imagen)
                    arbol.setScaledContents(True)
                    arbol.setGeometry(pixel.columna * P.N + P.margen, pixel.fila * P.N + P.margen, P.N, P.N)
                    arbol.clicked.connect(ventana.click_arbol)
                    arbol.tiempo = -1
                    ventana.drops.append(arbol)
                    arbol.fila = pixel.fila
                    arbol.columna = pixel.columna
                    arbol.tipo = "arbol"
                    arbol.show()
                    return True
    def generar_drop(self, ventana, tipo, columna, fila):
        if tipo == "choclo":
            drop = QLabel('drop', ventana)
            imagen_drop = QPixmap(parametros_plantas.PATH_SPRITES_CHOCLOS + "/stage_6")
            drop.setPixmap(imagen_drop)
            drop.setScaledContents(True)
            drop.setGeometry(P.N * columna + P.margen, P.N * fila + P.margen, P.N, P.N)
            drop.tipo = "choclo"
            drop.show()
            drop.tiempo = -1
        elif tipo == "oro":
            drop = QLabel('drop', ventana)
            imagen_drop = QPixmap(P.path_oro)
            drop.setPixmap(imagen_drop)
            drop.setScaledContents(True)
            drop.setGeometry(P.N * columna + P.margen, P.N * fila + P.margen, P.N, P.N)
            drop.show()
            drop.tiempo = P.DURACION_ORO
            drop.tipo = "oro"
        drop.fila = fila
        drop.columna = columna
        ventana.drops.append(drop)
