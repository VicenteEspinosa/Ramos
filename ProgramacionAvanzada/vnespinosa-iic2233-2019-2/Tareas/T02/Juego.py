from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
import os
import sys
import parametros_generales as P
import parametros_plantas
import parametros_acciones
from ventana_fin import VentanaFin

class VentanaJuego(QWidget):
    fin = pyqtSignal(str)
    procesar_key = pyqtSignal(object)
    revisar_tiempo_drops = pyqtSignal(object)
    actualizar_inventario = pyqtSignal(object)
    pixeles_main = pyqtSignal(object)
    Cargar = pyqtSignal(object)
    Comprar = pyqtSignal(object)
    mover = pyqtSignal(object)
    Agregar_cultivo = pyqtSignal(object)

    def __init__(self):
        self.drops = []
        self.cultivos = []
        self.keylist = []
        super().__init__()
        self.empezo = False


    def keyPressEvent(self, event):
        self.letra = event.text()
        self.firstrelease = True
        key = str(self.letra)
        self.keylist.append(key)



    def keyReleaseEvent(self,event):
        if self.firstrelease == True:
            if not self.pausado:
                self.procesar_key.emit(self)
        self.firstrelease = False

        del self.keylist[-1]

    def inicializa_gui(self, mapa):

        self.mapa = os.path.join("mapas", mapa)
        self.setWindowTitle('DCCampo')
        self.pixeles = []
        self.Cargar.emit(self)
        self.show()
        self.empezo = True
        self.Cargar_png_usuario()

    def Abrir_compra(self):
        self.hide()
        self.Comprar.emit(self.usuario)
        self.pausado = True

    def Volver_compra(self):
        self.actualizar_inventario.emit(self)
        self.Actualizar_dinero()
        self.show()
        self.actualizar_energia()
        self.pausado = False

    def Cargar_png_usuario(self):
        self.png_usuario = QLabel('usuario', self)
        imagen_us = QPixmap(P.usuario["down_1"])
        self.png_usuario.setPixmap(imagen_us)
        self.png_usuario.setScaledContents(True)
        self.png_usuario.move(P.N * self.usuario.columna + P.margen, P.N * self.usuario.fila + P.margen)
        self.png_usuario.show()

    def procesar_pixeles(ventana):
        for pixel in ventana.cultivables:
            pixel.soltar.connect(ventana.soltar)
        ventana.semilla_alcachofa.tomar.connect(ventana.tomar)
        ventana.semilla_choclo.tomar.connect(ventana.tomar)
        for pixel in ventana.arables:
            pixel.clicked.connect(ventana.click)

    def Actualizar_dinero(self):
        self.dinero.setText(str("Dinero: ") + str(self.usuario.dinero))
        self.dinero.resize(self.dinero.sizeHint())

    def tomar(self, tomado):
        self.tomado = tomado

    def soltar(self, numero):
        cultivo = self.cultivables[numero]
        if not self.pausado:
            self.usuario.energia -= P.ENERGIA_SEMBRAR
            self.actualizar_energia()
            if self.tomado == "Semilla alcachofa":
                if self.usuario.semilla_alcachofa == 0:
                    print("No tienes semillas de alcachofa")
                else:
                    self.usuario.semilla_alcachofa -= 1
                    print("Sembraste alcachofa")
                    self.actualizar_inventario.emit(self)
                    self.cultivo_col = cultivo.columna
                    self.cultivo_fil = cultivo.fila
                    self.cultivo_tipo = "alcachofa"
                    self.Agregar_cultivo.emit(self)
            elif self.tomado == "Semilla choclo":
                if self.usuario.semilla_choclo == 0:
                    print("No tienes semillas de choclo")
                else:
                    self.usuario.semilla_choclo -= 1
                    print("Sembraste choclo")
                    self.actualizar_inventario.emit(self)
                    self.cultivo_col = cultivo.columna
                    self.cultivo_fil = cultivo.fila
                    self.cultivo_tipo = "choclo"
                    self.Agregar_cultivo.emit(self)

        else:
            print("El juego esta pausado")

    def click(self, n):
        if not self.pausado:
            if self.usuario.azada == 1:
                self.arables[n].hide()
                self.cultivables[n].show()
                self.usuario.gastar_energia(parametros_acciones.ENERGIA_HERRAMIENTA)
                self.actualizar_energia()
            else:
                print("No tienes azada")
        else:
            print("El juego esta pausado...")

    def actualizar_energia(self):
        self.energia.setValue(self.usuario.energia)
        if self.usuario.energia <= 0:
            self.fin.emit("derrota")
            self.hide()
    def actualizar_tiempo(self): #Tiempo cultivos
        if not self.pausado:
            self.timer_cultivo.segs += 1
            for cultivo in self.cultivos:
                cultivo.tiempo += 1
            for drop in self.drops:
                drop.tiempo -= 1
        self.timer_cultivo.start(1000)
        self.revisar_cultivos()
        self.revisar_tiempo_drops.emit(self)

    def pasar_dia_cultivos(self):
        tiempo_faltante = P.DURACION_DIAS - self.timer_cultivo.segs
        if tiempo_faltante >= 1:
            for cultivo in self.cultivos:
                cultivo.tiempo += tiempo_faltante
            for drop in self.drops:  #TAMBIEN METI DROPS
                if drop.tiempo >= 0:
                    if drop.tiempo <= tiempo_faltante:
                        drop.tiempo = 0
                    else:
                        drop.tiempo -= tiempo_faltante
            self.revisar_tiempo_drops.emit(self)
        self.timer_cultivo.segs = 0
        self.revisar_cultivos()

    def revisar_cultivos(self):
        level_up = False
        for cultivo in self.cultivos:
            if cultivo.tiempo >= cultivo.tiempo_nivel:
                level_up = True
                cultivo.tiempo -= cultivo.tiempo_nivel
                self.subir_nivel_cultivo(cultivo)
        if level_up:
            self.revisar_cultivos()

    def subir_nivel_cultivo(self, cultivo):
        cultivo.nivel += 1
        if cultivo.tipo == "choclo":
            if cultivo.nivel == parametros_plantas.FASES_CHOCLOS:
                drop = QLabel('drop_choclo', self)
                imagen_drop = QPixmap(parametros_plantas.PATH_SPRITES_CHOCLOS + "/stage_6")
                drop.setPixmap(imagen_drop)
                drop.setScaledContents(True)
                drop.setGeometry(P.N * cultivo.columna + P.margen, P.N * cultivo.fila +
                    P.margen, P.N, P.N)
                drop.show()
                drop.padre = cultivo
                drop.columna = cultivo.columna
                drop.fila = cultivo.fila
                drop.tiempo = -1
                drop.tipo = "choclo"
                self.drops.append(drop)
                cultivo.hide()
                self.cultivos.remove(cultivo)
                #no borrar cultivo
                pass
            else:
                if cultivo.nivel == parametros_plantas.FASES_CHOCLOS - 1:
                    nivel = parametros_plantas.FASES_CHOCLOS
                else:
                    nivel = cultivo.nivel
                imagen_cultivo = QPixmap(parametros_plantas.PATH_SPRITES_CHOCLOS
                    + "/stage_" + str(nivel))
                cultivo.setPixmap(imagen_cultivo)
        else: #alcachofa
            if cultivo.nivel == parametros_plantas.FASES_ALCACHOFAS:
                drop = QLabel('drop_alcachofa', self)
                imagen_drop = QPixmap(parametros_plantas.PATH_SPRITES_ALCACHOFAS + "/stage_6")
                drop.setPixmap(imagen_drop)
                drop.setScaledContents(True)
                drop.setGeometry(P.N * cultivo.columna + P.margen, P.N * cultivo.fila +
                    P.margen, P.N, P.N)
                drop.show()
                drop.padre = cultivo #Cuando lo recoja agregar otra vez el cultivo a cultivos
                drop.columna = cultivo.columna
                drop.fila = cultivo.fila
                drop.tiempo = -1
                drop.tipo = "alcachofa"
                self.drops.append(drop)
                #soltar cosecha
                cultivo.hide()
                self.cultivos.remove(cultivo)
                #borrar cultivo
            else:
                imagen_cultivo = QPixmap(parametros_plantas.PATH_SPRITES_ALCACHOFAS
                    + "/stage_" + str(cultivo.nivel))
                cultivo.setPixmap(imagen_cultivo)

    def click_arbol(self, arbol):
        if not self.pausado:
            if self.usuario.hacha == 1:
                self.usuario.energia -= parametros_acciones.ENERGIA_HERRAMIENTA
                self.actualizar_energia()
                self.drops.remove(arbol)
                arbol.hide()
                drop = QLabel('drop', self)
                imagen_drop = QPixmap(P.path_madera)
                drop.setPixmap(imagen_drop)
                drop.setScaledContents(True)
                drop.setGeometry(P.N * arbol.columna + P.margen, P.N * arbol.fila
                    + P.margen, P.N, P.N)
                drop.show()
                drop.tiempo = P.DURACION_LENA
                drop.tipo = "madera"
                self.drops.append(drop)
                drop.fila = arbol.fila
                drop.columna = arbol.columna
                print("Cortaste arbol")
            else:
                print("No tienes hacha")
        else:
            print("El juego esta pausado")
