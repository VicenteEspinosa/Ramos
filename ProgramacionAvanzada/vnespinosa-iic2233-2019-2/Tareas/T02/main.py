from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem
                             ,QProgressBar)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
import os
import sys
import parametros_generales as P
from Pantalla_inicio import VentanaInicio
from Back_end import Procesos
from Juego import VentanaJuego
from Back_end_juego_1 import Back_end_juego_1
from Usuario import usuario
from Compra import VentanaCompra
from back_end_2 import Back_end_juego_2
from ventana_fin import VentanaFin
import random
from Casa import VentanaCasa

def hook(type, value, traceback):
    print(type)
    print(traceback)
sys.__excepthook__ = hook

app = QApplication(sys.argv)
proceso = Procesos()
Back_end_juego_1 = Back_end_juego_1()
back_end_2 = Back_end_juego_2()

casa = VentanaCasa()
ventana = VentanaInicio()
VentanaFin = VentanaFin()
ventana.show()

ventana_2 = VentanaJuego()

VentanaCompra = VentanaCompra()

back_end_2.entrar_casa.connect(casa.entrar)
casa.pasar_dia.connect(Back_end_juego_1.pasar_dia)
casa.volver.connect(ventana_2.Volver_compra)
ventana_2.Agregar_cultivo.connect(back_end_2.Agregar_cultivo)
ventana_2.mover.connect(back_end_2.mover_usuario)
ventana.revisar_mapa.connect(proceso.check_mapa)
proceso.Respuesta_cargar_mapa.connect(ventana.Actualizar_mensaje)
ventana.iniciar_juego.connect(ventana_2.inicializa_gui)
ventana_2.procesar_key.connect(back_end_2.procesar_key)
ventana_2.fin.connect(VentanaFin.setGui)
back_end_2.pasar_dia.connect(Back_end_juego_1.pasar_dia)
ventana_2.revisar_tiempo_drops.connect(back_end_2.revisar_tiempo_drops)
Back_end_juego_1.drops_aleatorios.connect(back_end_2.generar_drops_aleatorios)
VentanaCompra.fin.connect(VentanaFin.setGui)

back_end_2.abrir_tienda.connect(ventana_2.Abrir_compra)
ventana_2.Cargar.connect(Back_end_juego_1.Cargar_mapa)
ventana_2.Comprar.connect(VentanaCompra.Abrir)
ventana_2.actualizar_inventario.connect(Back_end_juego_1.Actualizar_inventario)

VentanaCompra.volver_juego.connect(ventana_2.Volver_compra)

ventana_2.pixeles_main.connect(ventana_2.procesar_pixeles)




sys.exit(app.exec())
