from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem
                             ,QProgressBar)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QObject, QTimer)
from PyQt5.QtGui import (QPixmap, QFont, QMovie, QIcon, QFont)
import os
import sys
import parametros_generales as P
import parametros_precios as precios

class VentanaCompra(QWidget):
    volver_juego = pyqtSignal()
    fin = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGui()

    def setGui(self):
        self.setGeometry(550, 300 ,800 ,600)
        self.setWindowTitle('Compra')
        self.setWindowIcon(QIcon(P.path_logo_inventario))
        self.fondo = QLabel('fondo', self)
        imagen = QPixmap(P.path_fondo)
        self.fondo.setPixmap(imagen)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 800, 600)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.titulo = QLabel(str("Menu de compra"), self)
        self.titulo.setFont(font)
        self.titulo.resize(self.titulo.sizeHint())
        self.titulo.move(300, 50)
        font2 = QFont()
        font2.setFamily("Times New Roman")
        font2.setPointSize(13)
        font2.setWeight(50)
        self.font2 = font2
        self.item_1 = QLabel(str("Item"), self)
        self.item_1.setFont(font2)
        self.item_1.resize(self.item_1.sizeHint())
        self.item_1.move(40, 100)
        self.hacha = QLabel('hacha', self)
        imagen_ha = QPixmap(P.path_hacha)
        self.hacha.setPixmap(imagen_ha)
        self.hacha.resize(self.hacha.sizeHint())
        self.hacha.move(40, 140)
        self.azada = QLabel('azada', self)
        imagen_az = QPixmap(P.path_azada)
        self.azada.setPixmap(imagen_az)
        self.azada.resize(self.azada.sizeHint())
        self.azada.move(40, 230)
        self.semilla_choclo = QLabel('semilla choclo', self)
        imagen_s_c = QPixmap(P.path_semillas_choclo)
        self.semilla_choclo.setPixmap(imagen_s_c)
        self.semilla_choclo.resize(self.semilla_choclo.sizeHint())
        self.semilla_choclo.move(40, 320)
        self.semilla_alcachofa = QLabel('semilla alcachofa', self)
        imagen_s_a = QPixmap(P.path_semillas_alcachofa)
        self.semilla_alcachofa.setPixmap(imagen_s_a)
        self.semilla_alcachofa.resize(self.semilla_alcachofa.sizeHint())
        self.semilla_alcachofa.move(40, 410)
        self.precio_1 = QLabel(str("Precio"), self)
        self.precio_1.setFont(font2)
        self.precio_1.resize(self.precio_1.sizeHint())
        self.precio_1.move(140, 100)
        self.precio_hacha = QLabel("$ " + str(precios.PRECIO_HACHA), self)
        self.precio_hacha.setFont(font2)
        self.precio_hacha.resize(self.precio_hacha.sizeHint())
        self.precio_hacha.move(140, 140)
        self.precio_azada = QLabel("$ " + str(precios.PRECIO_AZADA), self)
        self.precio_azada.setFont(font2)
        self.precio_azada.resize(self.precio_azada.sizeHint())
        self.precio_azada.move(140, 240)
        self.precio_semilla_choclo = QLabel("$ " + str(precios.PRECIO_SEMILLA_CHOCLOS), self)
        self.precio_semilla_choclo.setFont(font2)
        self.precio_semilla_choclo.resize(self.precio_semilla_choclo.sizeHint())
        self.precio_semilla_choclo.move(140, 330)
        self.precio_semilla_alcachofa = QLabel("$ " + str(precios.PRECIO_SEMILLA_ALCACHOFAS), self)
        self.precio_semilla_alcachofa.setFont(font2)
        self.precio_semilla_alcachofa.resize(self.precio_semilla_alcachofa.sizeHint())
        self.precio_semilla_alcachofa.move(140, 420)
        self.accion_1 = QLabel("Accion", self)
        self.accion_1.setFont(font2)
        self.accion_1.resize(self.accion_1.sizeHint())
        self.accion_1.move(240, 100)
        self.boton_compra_hacha = QPushButton('Comprar', self)
        self.boton_compra_hacha.clicked.connect(self.Comprar_hacha)
        self.boton_compra_hacha.resize(90,25)
        self.boton_compra_hacha.move(240, 130)
        self.boton_compra_hacha.activado = True
        self.boton_venta_hacha = QPushButton('Vender', self)
        self.boton_venta_hacha.clicked.connect(self.Vender_hacha)
        self.boton_venta_hacha.resize(90,20)
        self.boton_venta_hacha.move(240, 160)
        self.boton_venta_hacha.activado = True
        self.boton_compra_azada = QPushButton('Comprar', self)
        self.boton_compra_azada.clicked.connect(self.Comprar_azada)
        self.boton_compra_azada.resize(90,25)
        self.boton_compra_azada.move(240, 230)
        self.boton_compra_azada.activado = True
        self.boton_venta_azada = QPushButton('Vender', self)
        self.boton_venta_azada.clicked.connect(self.Vender_azada)
        self.boton_venta_azada.resize(90,20)
        self.boton_venta_azada.move(240, 260)
        self.boton_venta_azada.activado = True
        self.boton_compra_s_c = QPushButton('Comprar', self)
        self.boton_compra_s_c.clicked.connect(self.Comprar_s_c)
        self.boton_compra_s_c.resize(90,25)
        self.boton_compra_s_c.move(240, 315)
        self.boton_compra_s_c.activado = True
        self.boton_venta_s_c = QPushButton('Vender', self)
        self.boton_venta_s_c.clicked.connect(self.Vender_s_c)
        self.boton_venta_s_c.resize(90,20)
        self.boton_venta_s_c.move(240, 345)
        self.boton_venta_s_c.activado = True
        self.boton_compra_s_a = QPushButton('Comprar', self)
        self.boton_compra_s_a.clicked.connect(self.Comprar_s_a)
        self.boton_compra_s_a.resize(90,25)
        self.boton_compra_s_a.move(240, 410)
        self.boton_compra_s_a.activado = True
        self.boton_venta_s_a = QPushButton('Vender', self)
        self.boton_venta_s_a.clicked.connect(self.Vender_s_a)
        self.boton_venta_s_a.resize(90,20)
        self.boton_venta_s_a.move(240, 440)
        self.boton_venta_s_a.activado = True
        self.item_2 = QLabel(str("Item"), self)
        self.item_2.setFont(font2)
        self.item_2.resize(self.item_2.sizeHint())
        self.item_2.move(430, 100)
        self.alcachofa = QLabel('alcachofa', self)
        imagen_al = QPixmap(P.path_alcachofa)
        self.alcachofa.setPixmap(imagen_al)
        self.alcachofa.resize(self.azada.sizeHint())
        self.alcachofa.move(430, 140)
        self.choclo = QLabel('choclo', self)
        imagen_ch = QPixmap(P.path_choclo)
        self.choclo.setPixmap(imagen_ch)
        self.choclo.resize(self.choclo.sizeHint())
        self.choclo.move(430, 230)
        self.madera = QLabel('madera', self)
        imagen_ma = QPixmap(P.path_madera)
        self.madera.setPixmap(imagen_ma)
        self.madera.resize(self.madera.sizeHint())
        self.madera.move(430, 320)
        self.oro = QLabel('oro', self)
        imagen_or = QPixmap(P.path_oro)
        self.oro.setPixmap(imagen_or)
        self.oro.resize(self.oro.sizeHint())
        self.oro.move(430, 410)
        self.precio_2 = QLabel(str("Precio"), self)
        self.precio_2.setFont(font2)
        self.precio_2.resize(self.precio_2.sizeHint())
        self.precio_2.move(530, 100)
        self.precio_alcachofa = QLabel("$ " + str(precios.PRECIO_ALACACHOFAS), self)
        self.precio_alcachofa.setFont(font2)
        self.precio_alcachofa.resize(self.precio_alcachofa.sizeHint())
        self.precio_alcachofa.move(530, 140)
        self.precio_choclo = QLabel("$ " + str(precios.PRECIO_CHOCLOS), self)
        self.precio_choclo.setFont(font2)
        self.precio_choclo.resize(self.precio_choclo.sizeHint())
        self.precio_choclo.move(530, 240)
        self.precio_madera = QLabel("$ " + str(precios.PRECIO_LEÑA), self)
        self.precio_madera.setFont(font2)
        self.precio_madera.resize(self.precio_madera.sizeHint())
        self.precio_madera.move(530, 330)
        self.precio_oro = QLabel("$ " + str(precios.PRECIO_ORO), self)
        self.precio_oro.setFont(font2)
        self.precio_oro.resize(self.oro.sizeHint())
        self.precio_oro.move(530, 410)
        self.accion_2 = QLabel("Accion", self)
        self.accion_2.setFont(font2)
        self.accion_2.resize(self.accion_2.sizeHint())
        self.accion_2.move(630, 100)
        self.boton_venta_alcachofa = QPushButton('Vender', self)
        self.boton_venta_alcachofa.clicked.connect(self.Vender_alcachofa)
        self.boton_venta_alcachofa.resize(90,20)
        self.boton_venta_alcachofa.move(630, 140)
        self.boton_venta_alcachofa.activado = True

        self.boton_venta_choclo = QPushButton('Vender', self)
        self.boton_venta_choclo.clicked.connect(self.Vender_choclo)
        self.boton_venta_choclo.resize(90,20)
        self.boton_venta_choclo.move(630, 240)
        self.boton_venta_choclo.activado = True

        self.boton_venta_madera = QPushButton('Vender', self)
        self.boton_venta_madera.clicked.connect(self.Vender_madera)
        self.boton_venta_madera.resize(90,20)
        self.boton_venta_madera.move(630, 330)
        self.boton_venta_madera.activado = True

        self.boton_venta_oro = QPushButton('Vender', self)
        self.boton_venta_oro.clicked.connect(self.Vender_oro)
        self.boton_venta_oro.resize(90,20)
        self.boton_venta_oro.move(630, 420)
        self.boton_venta_oro.activado = True

        self.boton_salir = QPushButton('Volver al juego', self)
        self.boton_salir.clicked.connect(self.Cerrar)
        self.boton_salir.move(670, 530)

        self.ticket = QLabel('ticket', self)
        imagen_ti = QPixmap(P.path_ticket)
        self.ticket.setPixmap(imagen_ti)
        self.ticket.resize(self.ticket.sizeHint())
        self.ticket.move(40, 500)

        self.precio_ticket = QLabel("$ " + str(precios.PRECIO_TICKET), self)
        self.precio_ticket.setFont(font2)
        self.precio_ticket.resize(self.precio_ticket.sizeHint())
        self.precio_ticket.move(120, 510)

        self.boton_ticket = QPushButton('Comprar', self)
        self.boton_ticket.clicked.connect(self.Comprar_ticket)
        self.boton_ticket.resize(90,25)
        self.boton_ticket.move(240, 510)



    def Comprar_hacha(self):
        if self.boton_compra_hacha.activado:
            self.usuario.hacha = 1
            self.usuario.dinero -= precios.PRECIO_HACHA
            print("Compraste hacha")
            self.Actualizar_botones()
            self.Actualizar_dinero()


    def Vender_hacha(self):
        if self.boton_venta_hacha.activado:
            self.usuario.hacha = 0
            self.usuario.dinero += precios.PRECIO_HACHA
            print("Vendiste hacha")
            self.Actualizar_botones()
            self.Actualizar_dinero()

    def Comprar_azada(self):
        if self.boton_compra_azada.activado:
            self.usuario.azada = 1
            self.usuario.dinero -= precios.PRECIO_AZADA
            print("Compraste azada")
            self.Actualizar_botones()
            self.Actualizar_dinero()

    def Vender_azada(self):
        if self.boton_venta_azada.activado:
            self.usuario.azada = 0
            self.usuario.dinero += precios.PRECIO_AZADA
            print("Vendiste azada")
            self.Actualizar_botones()
            self.Actualizar_dinero()

    def Comprar_s_c(self):
        if self.boton_compra_s_c.activado:
            self.usuario.semilla_choclo += 1
            self.usuario.dinero -= precios.PRECIO_SEMILLA_CHOCLOS
            print("Compraste semilla choclo")
            self.Actualizar_botones()
            self.Actualizar_dinero()

    def Vender_s_c(self):
        if self.boton_venta_s_c.activado:
            self.usuario.semilla_choclo -= 1
            self.usuario.dinero += precios.PRECIO_SEMILLA_CHOCLOS
            print("Vendiste semilla choclo")
            self.Actualizar_botones()
            self.Actualizar_dinero()

    def Comprar_s_a(self):
        if self.boton_compra_s_a.activado:
            self.usuario.semilla_alcachofa += 1
            self.usuario.dinero -= precios.PRECIO_SEMILLA_ALCACHOFAS
            print("Compraste semilla alcachofa")
            self.Actualizar_botones()
            self.Actualizar_dinero()
    def Vender_s_a(self):
        if self.boton_venta_s_a.activado:
            self.usuario.semilla_alcachofa -= 1
            self.usuario.dinero += precios.PRECIO_SEMILLA_ALCACHOFAS
            print("Vendiste semilla alcachofa")
            self.Actualizar_botones()
            self.Actualizar_dinero()
    def Vender_alcachofa(self):
        if self.boton_venta_alcachofa.activado:
            self.usuario.alcachofa -= 1
            self.usuario.dinero += precios.PRECIO_ALACACHOFAS
            print("Vendista alcachofa")
            self.Actualizar_botones()
            self.Actualizar_dinero()
    def Vender_choclo(self):
        if self.boton_venta_choclo.activado:
            self.usuario.choclo -= 1
            self.usuario.dinero += precios.PRECIO_CHOCLOS
            print("Vendista choclo")
            self.Actualizar_botones()
            self.Actualizar_dinero()
    def Vender_madera(self):
        if self.boton_venta_madera.activado:
            self.usuario.madera -= 1
            self.usuario.dinero += precios.PRECIO_LEÑA
            print("Vendista madera")
            self.Actualizar_botones()
            self.Actualizar_dinero()
    def Vender_oro(self):
        if self.boton_venta_oro.activado:
            self.usuario.oro -= 1
            self.usuario.dinero += precios.PRECIO_ORO
            print("Vendista oro")
            self.Actualizar_botones()
            self.Actualizar_dinero()
    def Comprar_ticket(self):
        if self.boton_ticket.activado:
            self.usuario.dinero -= precios.PRECIO_TICKET
            print("Compraste ticket")
            self.fin.emit("victoria")
            self.hide()
    def Desactivar_boton(self, boton):
        boton.setStyleSheet('QPushButton {color: gray;}')
        boton.activado = False
    def Activar_boton(self,boton):
        boton.setStyleSheet('QPushButton {color: black;}')
        boton.activado = True
    def Actualizar_dinero(self):
        self.dinero_actual.setText("Dinero Actual: $ " + str(self.usuario.dinero))
        self.dinero_actual.resize(self.dinero_actual.sizeHint())
    def Abrir(self, usuario):
        if hasattr(self, 'usuario'):
            self.Actualizar_dinero()
        else:
            self.usuario = usuario
            self.dinero_actual = QLabel("Dinero Actual: $ " + str(self.usuario.dinero), self)
            self.dinero_actual.setFont(self.font2)
            self.dinero_actual.resize(self.dinero_actual.sizeHint())
            self.dinero_actual.move(400, 510)
            self.dinero_actual.setStyleSheet('QLabel {color: blue;}')
        self.Actualizar_botones()
        self.show()
    def Cerrar(self):
        self.hide()
        self.volver_juego.emit()
    def Actualizar_botones(self):
        dinero = self.usuario.dinero
        if self.usuario.hacha == 1:
            self.Desactivar_boton(self.boton_compra_hacha)
            self.Activar_boton(self.boton_venta_hacha)
        else:
            self.Desactivar_boton(self.boton_venta_hacha)
            self.Activar_boton(self.boton_compra_hacha)
            if dinero < precios.PRECIO_HACHA:
                self.Desactivar_boton(self.boton_compra_hacha)
        if self.usuario.azada == 1:
            self.Desactivar_boton(self.boton_compra_azada)
            self.Activar_boton(self.boton_venta_azada)
        else:
            self.Desactivar_boton(self.boton_venta_azada)
            self.Activar_boton(self.boton_compra_azada)
            if dinero < precios.PRECIO_AZADA:
                self.Desactivar_boton(self.boton_compra_azada)
        if dinero < precios.PRECIO_SEMILLA_CHOCLOS:
            self.Desactivar_boton(self.boton_compra_s_c)
        else:
            self.Activar_boton(self.boton_compra_s_c)
        if self.usuario.semilla_choclo == 0:
            self.Desactivar_boton(self.boton_venta_s_c)
        else:
            self.Activar_boton(self.boton_venta_s_c)
        if dinero < precios.PRECIO_SEMILLA_ALCACHOFAS:
            self.Desactivar_boton(self.boton_compra_s_a)
        else:
            self.Activar_boton(self.boton_compra_s_a)
        if self.usuario.semilla_alcachofa == 0:
            self.Desactivar_boton(self.boton_venta_s_a)
        else:
            self.Activar_boton(self.boton_venta_s_a)
        if dinero < precios.PRECIO_TICKET:
            self.Desactivar_boton(self.boton_ticket)
        else:
            self.Activar_boton(self.boton_ticket)
        if self.usuario.alcachofa == 0:
            self.Desactivar_boton(self.boton_venta_alcachofa)
        else:
            self.Activar_boton(self.boton_venta_alcachofa)
        if self.usuario.choclo == 0:
            self.Desactivar_boton(self.boton_venta_choclo)
        else:
            self.Activar_boton(self.boton_venta_choclo)
        if self.usuario.madera == 0:
            self.Desactivar_boton(self.boton_venta_madera)
        else:
            self.Activar_boton(self.boton_venta_madera)
        if self.usuario.oro == 0:
            self.Desactivar_boton(self.boton_venta_oro)
        else:
            self.Activar_boton(self.boton_venta_oro)
