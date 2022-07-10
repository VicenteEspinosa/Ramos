import parametros_generales as P
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem
                             ,QProgressBar)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QObject, QTimer, QMimeData)
from PyQt5.QtGui import (QPixmap, QFont, QMovie, QIcon, QFont, QDrag, QPainter, QCursor, QImage, QMouseEvent)
import random
from Usuario import usuario
from Pixeles import Pixel

class DraggableLabel(QLabel):
    tomar = pyqtSignal(str)
    #Codigo DraggableLabel y DropLabel sacados de:
    # https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        self.tomar.emit(self.tipo)
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)
class DropLabel(QLabel):
    soltar = pyqtSignal(int)
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
    def dropEvent(self, event):
        self.soltar.emit(self.numero)
        pos = event.pos()
        text = event.mimeData().text()
        event.acceptProposedAction()
class ClickLabel(QLabel):
  clicked = pyqtSignal(int)
  def __init(self, parent):
    QLabel.__init__(self, QMouseEvent)
  def mousePressEvent(self, ev):
    self.clicked.emit(self.numero)
class Back_end_juego_1(QObject):
    drops_aleatorios = pyqtSignal(object)

    def __init__(self):
        super().__init__()
    def Cargar_mapa(yo, self): #Uso yo como self, y self como ventana
        self.timer_cultivo = QTimer(self)
        self.timer_cultivo.timeout.connect(self.actualizar_tiempo)
        self.timer_cultivo.start(1000)
        self.timer_cultivo.segs = 0
        # llevar conteo###
        self.pausado = False
        yo.dias = 0
        yo.ventana = self
        yo.tiempo = P.DURACION_DIAS
        yo.timer = QTimer(yo)
        yo.timer.timeout.connect(yo.update)
        yo.tiempo_15_min = P.DURACION_DIAS / 96
        yo.timer.start(yo.tiempo_15_min * 1000)
        yo.minutos = 0
        yo.hora = 0
        self.setWindowIcon(QIcon(P.path_azada)) #No es necesario
        self.fondo = QLabel('fondo', self)
        imagen = QPixmap(P.path_fondo)
        self.fondo.setPixmap(imagen)
        self.fondo.setScaledContents(True)
        self.inventario = QLabel('inventario', self)
        imagen_1 = QPixmap(P.path_fondo)
        self.inventario.setPixmap(imagen_1)
        self.inventario.setScaledContents(True)
        self.stats = QLabel('stats', self)
        imagen_2 = QPixmap(P.path_fondo)
        self.stats.setPixmap(imagen_2)
        self.stats.setScaledContents(True)
        self.hacha = QLabel('hacha', self)
        imagen_h = QPixmap(P.path_hacha)
        self.hacha.setPixmap(imagen_h)
        self.hacha.setScaledContents(True)
        self.azada = QLabel('azada', self)
        imagen_az = QPixmap(P.path_azada)
        self.azada.setPixmap(imagen_az)
        self.azada.setScaledContents(True)
        self.alcachofa = QLabel('alcachofa', self)
        imagen_al = QPixmap(P.path_alcachofa)
        self.alcachofa.setPixmap(imagen_al)
        self.alcachofa.setScaledContents(True)
        self.choclo = QLabel('choclo', self)
        imagen_ch = QPixmap(P.path_choclo)
        self.choclo.setPixmap(imagen_ch)
        self.choclo.setScaledContents(True)
        self.oro = QLabel('oro', self)
        imagen_or = QPixmap(P.path_oro)
        self.oro.setPixmap(imagen_or)
        self.oro.setScaledContents(True)
        self.madera = QLabel('madera', self)
        imagen_ma = QPixmap(P.path_madera)
        self.madera.setPixmap(imagen_ma)
        self.madera.setScaledContents(True)
        self.semilla_alcachofa = DraggableLabel('semilla alcachofa', self)
        imagen_s_a = QPixmap(P.path_semillas_alcachofa)
        self.semilla_alcachofa.setPixmap(imagen_s_a)
        self.semilla_alcachofa.setScaledContents(True)
        self.semilla_alcachofa.tipo = "Semilla alcachofa"
        self.semilla_choclo = DraggableLabel('semilla choclo', self)
        imagen_s_c = QPixmap(P.path_semillas_choclo)
        self.semilla_choclo.setPixmap(imagen_s_c)
        self.semilla_choclo.setScaledContents(True)
        self.semilla_choclo.tipo = "Semilla choclo"
        N = P.N
        coord_saltar_casa = []
        coord_saltar_tienda = []
        coord = []
        fil = 0
        with open(self.mapa, encoding = "utf-8") as file:
            for line in file:
                fil += 1
                line = line.replace("\n", "")
                col = len(line.split(" "))
                coord.append(line.split(" "))
        yo.fil = fil
        yo.col = col
        yo.margen = P.margen
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label_Stats = QLabel("STATS:", self)
        self.label_Stats.setFont(QFont("Times", 10,QFont.Bold))
        self.label_Stats.resize(self.label_Stats.sizeHint())
        self.label_Stats.move(N*yo.col + yo.margen*4, yo.margen*2)
        self.tiempo = QLabel(str("Tiempo: ") + str(yo.tiempo), self)
        self.tiempo.setFont(font)
        self.tiempo.resize(self.tiempo.sizeHint())
        self.tiempo.move(N * yo.col + yo.margen * 3, (N*yo.fil + yo.margen*2 + P.largo_inventario)/7 )
        self.dias = QLabel(str("Dias Transcurridos: ") + str(yo.dias), self)
        self.dias.setFont(font)
        self.dias.resize(self.dias.sizeHint())
        self.dias.move(N*yo.col + yo.margen*3, 2*(N*yo.fil + yo.margen*2 + P.largo_inventario)/7 )
        self.label_energia = QLabel("Energia:", self)
        self.label_energia.setFont(font)
        self.label_energia.resize(self.label_energia.sizeHint())
        self.label_energia.move(N*yo.col + yo.margen*3, 4*(N*yo.fil + yo.margen*2 + P.largo_inventario)/7 )
        self.energia = QProgressBar(self)
        self.energia.setGeometry(N*yo.col + yo.margen*3, 4.5*(N * yo.fil + yo.margen*2 + P.largo_inventario)/7 , yo.margen*5, yo.margen)
        self.energia.setMaximum(P.ENERGIA_JUGADOR)
        self.energia.setValue(P.ENERGIA_JUGADOR)
        self.boton_pausa = QPushButton('Pausar', self)
        self.boton_pausa.clicked.connect(yo.Pausar)
        self.boton_pausa.resize(self.boton_pausa.sizeHint())
        self.boton_pausa.move(N * yo.col + yo.margen * 3, 5.5 * (N * yo.fil + yo.margen * 2 + P.largo_inventario) / 7 )
        self.boton_salir = QPushButton('Salir', self)
        self.boton_salir.clicked.connect(yo.Salir)
        self.boton_salir.resize(self.boton_salir.sizeHint())
        self.boton_salir.move(N * yo.col + yo.margen * 3, 6 * (N * yo.fil + yo.margen * 2 + P.largo_inventario) / 7 )
        self.fondo.setGeometry(0, 0, N * col + yo.margen * 2, N * fil + yo.margen * 2)
        self.inventario.setGeometry(0, N * yo.fil + yo.margen * 2, N * yo.col + yo.margen * 2, P.largo_inventario)
        self.stats.setGeometry(N * yo.col + yo.margen * 2, 0, P.largo_inventario * 2, N * yo.fil + yo.margen * 2 + P.largo_inventario)
        self.hacha.setGeometry(yo.margen * 2, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.azada.setGeometry(yo.margen * 2 + P.largo_inventario, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.alcachofa.setGeometry(yo.margen * 2 + P.largo_inventario * 2, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.choclo.setGeometry(yo.margen * 2 + P.largo_inventario * 3, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.oro.setGeometry(yo.margen * 2 + P.largo_inventario * 4, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.madera.setGeometry(yo.margen * 2 + P.largo_inventario * 5, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.semilla_alcachofa.setGeometry(yo.margen * 2 + P.largo_inventario * 6, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.semilla_choclo.setGeometry(yo.margen * 2 + P.largo_inventario * 7, N * fil + yo.margen * 2.2, P.largo_inventario / 2, P.largo_inventario / 2)
        self.setGeometry(400, 300,  N * yo.col + yo.margen * 2 + P.largo_inventario * 2, N * yo.fil + yo.margen * 2 + P.largo_inventario)
        Roca = False
        Casa = False
        Tienda = False
        saltar = False
        columna = -1
        fila_n = -1
        self.arables = []
        self.cultivables = []
        for fila in coord:
            fila_n += 1
            for pixel in fila:
                columna += 1
                if ((columna, fila_n) in coord_saltar_casa) or ((columna, fila_n) in coord_saltar_tienda):
                    saltar = True
                elif pixel == "O" or pixel == "R":
                    tipo = "libre"
                    i = random.randint(0,3)
                    libre = ["libre", "libre2", "libre3", "libre4"]
                    path = P.celdas_mapa[libre[i]]
                elif pixel == "C":
                    tipo = "cultivable"
                    path = P.celdas_mapa["cultivable"]
                elif pixel == "H":
                    tipo = "casa"
                    Casa = True
                    path = P.path_casa
                    coord_saltar_casa.append((columna + 1, fila_n))
                    coord_saltar_casa.append((columna , fila_n + 1))
                    coord_saltar_casa.append((columna + 1, fila_n + 1))
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry((columna + 1) * N + yo.margen, fila_n * N + yo.margen, N, N)
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry(columna * N + yo.margen, fila_n * N + yo.margen, N, N)
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry(columna * N + yo.margen, (fila_n + 1) * N + yo.margen, N, N)
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry((columna + 1) * N + yo.margen, (fila_n + 1) * N + yo.margen, N, N)
                elif pixel == "T":
                    tipo = "tienda"
                    Tienda = True
                    path = P.path_tienda
                    coord_saltar_tienda.append((columna + 1, fila_n))
                    coord_saltar_tienda.append((columna , fila_n + 1))
                    coord_saltar_tienda.append((columna + 1, fila_n + 1))
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry((columna + 1) * N + yo.margen, fila_n * N + yo.margen, N, N)
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry(columna * N + yo.margen, fila_n * N + yo.margen, N, N)
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry(columna * N + yo.margen, (fila_n + 1) * N + yo.margen, N, N)
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(P.celdas_mapa["libre"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry((columna + 1) * N + yo.margen, (fila_n + 1) * N + yo.margen, N, N)
                if pixel == "R":
                    tipo = "roca"
                    Roca = True
                if (not Casa and not Tienda) and not saltar:
                    if tipo == "cultivable":
                        pixel_i_j = ClickLabel('pixel', self)
                        imagen = QPixmap(path)
                        pixel_i_j.setPixmap(imagen)
                        pixel_i_j.setScaledContents(True)
                        pixel_i_j.setGeometry(columna * N + yo.margen, fila_n * N + yo.margen, N, N)
                        n = len(self.arables)
                        self.arables.append(pixel_i_j)
                        pixel_i_j.numero = n
                        pixel_i_j = DropLabel('pixel', self)
                        imagen = QPixmap(P.celdas_mapa["cultivable_listo"])
                        pixel_i_j.setPixmap(imagen)
                        pixel_i_j.setScaledContents(True)
                        pixel_i_j.setGeometry(columna * N + yo.margen, fila_n * N + yo.margen, N, N)
                        pixel_i_j.numero = n
                        pixel_i_j.sembrado = False
                        pixel_i_j.columna = columna
                        pixel_i_j.fila = fila_n
                        self.cultivables.append(pixel_i_j)
                        pixel_i_j.hide()
                    else:
                        pixel_i_j = QLabel('pixel', self)
                        imagen = QPixmap(path)
                        pixel_i_j.setPixmap(imagen)
                        pixel_i_j.setScaledContents(True)
                        pixel_i_j.setGeometry(columna * N + yo.margen, fila_n * N + yo.margen, N, N)
                elif saltar:
                    if ((columna, fila_n) in coord_saltar_casa):
                        tipo = "casa"
                    elif ((columna, fila_n) in coord_saltar_tienda):
                        tipo = "tienda"
                else:
                    pixel_i_j = QLabel('pixel', self)
                    imagen = QPixmap(path)
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry(columna * N + yo.margen, fila_n * N + yo.margen, N*2, N*2)
                if Roca:
                    pixel_i_j = QLabel('Roca', self)
                    imagen = QPixmap(P.celdas_mapa["roca"])
                    pixel_i_j.setPixmap(imagen)
                    pixel_i_j.setScaledContents(True)
                    pixel_i_j.setGeometry(columna * N + yo.margen, fila_n * N + yo.margen, N, N)
                    tipo = "roca"
                pixel = Pixel(columna, fila_n, tipo)
                self.pixeles.append(pixel)
                Roca = False
                Casa = False
                Tienda = False
                saltar = False
            columna = -1
        self.usuario = usuario(self.pixeles)
        self.dinero = QLabel(str("Dinero: ") + str(self.usuario.dinero), self)
        self.dinero.setFont(font)
        self.dinero.resize(self.dinero.sizeHint())
        self.dinero.move(N * yo.col + yo.margen * 3, 3 * (N * yo.fil + yo.margen * 2 + P.largo_inventario) / 7 )
        self.pixeles_main.emit(self)
        yo.Cargar_inventario(self)
    def Cargar_inventario(self, ventana):
        ventana.cantidad_hacha = QLabel(str(ventana.usuario.hacha), ventana)
        ventana.cantidad_hacha.resize(ventana.cantidad_hacha.sizeHint())
        ventana.cantidad_hacha.setGeometry(self.margen * 2, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
        ventana.cantidad_azada = QLabel(str(ventana.usuario.azada), ventana)
        ventana.cantidad_azada.resize(ventana.cantidad_azada.sizeHint())
        ventana.cantidad_azada.setGeometry(self.margen * 2 + P.largo_inventario, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
        ventana.cantidad_alcachofa = QLabel(str(ventana.usuario.alcachofa), ventana)
        ventana.cantidad_alcachofa.resize(ventana.cantidad_alcachofa.sizeHint())
        ventana.cantidad_alcachofa.setGeometry(self.margen * 2 + P.largo_inventario * 2.15, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
        ventana.cantidad_choclo = QLabel(str(ventana.usuario.choclo), ventana)
        ventana.cantidad_choclo.resize(ventana.cantidad_choclo.sizeHint())
        ventana.cantidad_choclo.setGeometry(self.margen * 2 + P.largo_inventario * 3.1, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
        ventana.cantidad_oro = QLabel(str(ventana.usuario.oro), ventana)
        ventana.cantidad_oro.resize(ventana.cantidad_oro.sizeHint())
        ventana.cantidad_oro.setGeometry(self.margen * 2 + P.largo_inventario * 4.2, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
        ventana.cantidad_madera = QLabel(str(ventana.usuario.madera), ventana)
        ventana.cantidad_madera.resize(ventana.cantidad_madera.sizeHint())
        ventana.cantidad_madera.setGeometry(self.margen * 2 + P.largo_inventario * 5.2, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
        ventana.cantidad_semilla_alcachofa = QLabel(str(ventana.usuario.semilla_alcachofa), ventana)
        ventana.cantidad_semilla_alcachofa.resize(ventana.cantidad_semilla_alcachofa.sizeHint())
        ventana.cantidad_semilla_alcachofa.setGeometry(self.margen * 2 + P.largo_inventario * 6.2, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
        ventana.cantidad_semilla_choclo = QLabel(str(ventana.usuario.semilla_choclo), ventana)
        ventana.cantidad_semilla_choclo.resize(ventana.cantidad_semilla_choclo.sizeHint())
        ventana.cantidad_semilla_choclo.setGeometry(self.margen * 2 + P.largo_inventario * 7.2, P.N * self.fil + self.margen * 2.2 +  P.largo_inventario / 2, 30, 30)
    def Actualizar_inventario(self, ventana):
        ventana.cantidad_hacha.setText(str(ventana.usuario.hacha))
        ventana.cantidad_azada.setText(str(ventana.usuario.azada))
        ventana.cantidad_alcachofa.setText(str(ventana.usuario.alcachofa))
        ventana.cantidad_choclo.setText(str(ventana.usuario.choclo))
        ventana.cantidad_oro.setText(str(ventana.usuario.oro))
        ventana.cantidad_madera.setText(str(ventana.usuario.madera))
        ventana.cantidad_semilla_alcachofa.setText(str(ventana.usuario.semilla_alcachofa))
        ventana.cantidad_semilla_choclo.setText(str(ventana.usuario.semilla_choclo))
    def update(self):
        if not self.ventana.pausado:
            self.minutos += 15
        if self.minutos == 60:
            self.hora += 1
            self.minutos = 0
        if self.minutos == 0:
            self.minutos_str = "00"
        else:
            self.minutos_str = str(self.minutos)
        if self.hora == 24:
            self.pasar_dia()
        if self.hora < 9:
            self.hora_str = str("0" + str(self.hora))
        else:
            self.hora_str = str(self.hora)
        self.ventana.tiempo.setText(str("Hora: ") + str(self.hora_str + ":" + self.minutos_str))
        self.ventana.tiempo.resize(self.ventana.tiempo.sizeHint())
        self.timer.start(self.tiempo_15_min*1000)
    def pasar_dia(self):
        print("Paso un dia")
        self.dias += 1
        self.hora = 0
        self.ventana.dias.setText(str("Dias Transcurridos: ") + str(self.dias))
        self.ventana.dias.resize(self.ventana.dias.sizeHint())
        self.ventana.pasar_dia_cultivos()
        self.ventana.usuario.energia += P.ENERGIA_DORMIR
        if self.ventana.usuario.energia > P.ENERGIA_JUGADOR:
            self.ventana.usuario.energia = P.ENERGIA_JUGADOR
        self.ventana.actualizar_energia()
        self.drops_aleatorios.emit(self.ventana)
    def Salir(self):
        self.ventana.close()
    def Pausar(self):
        if self.ventana.pausado:
            self.ventana.pausado = False
            self.ventana.boton_pausa.setText("Pausar")
        else:
            self.ventana.pausado = True
            self.ventana.boton_pausa.setText("Reanudar")
