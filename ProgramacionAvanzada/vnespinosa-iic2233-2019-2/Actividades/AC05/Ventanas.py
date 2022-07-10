from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)


"""
Debes completar la clase VentanaJuego con los elementos que
estimes necesarios.

Eres libre de agregar otras clases si lo crees conveniente.
"""

class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.

    Recuerda que eviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.imagen = "images/1"
        self.palabra = "palabra"
        self.disponibles = "disponibles"
        self.usadas = "usadas"
        #enviar_letra_signal({"letra" : ""} )
        self.inicializa_gui()




    def inicializa_gui(self):
        self.letra = ""
        self.enviar_letra_signal.emit({"letra" : ""})

        self.setGeometry(200, 100, 500, 500)
        self.setWindowTitle('DCColgado 51')

        self.etiqueta = QLabel(' ', self)

        self.Palabra = QLabel(str(self.palabra), self)
        self.Palabra.resize(self.Palabra.sizeHint())
        self.Usadas = QLabel(str(self.usadas), self)
        self.Usadas.resize(self.Usadas.sizeHint())
        self.Disponibles = QLabel(str(self.disponibles), self)
        self.Disponibles.resize(self.Disponibles.sizeHint())

        self.boton_letra = QPushButton('Seleccionar Letra', self)
        self.boton_letra.clicked.connect(self.Ingresar_letra)
        self.boton_reset = QPushButton('Nuevo Juego', self)
        self.boton_reset.clicked.connect(self.reiniciar)

        self.foto = QLabel('foto', self)
        self.foto0 = QPixmap(self.imagen)
        self.foto.setPixmap(self.foto0)



        layout_izq = QVBoxLayout()
        layout_izq.addWidget(self.Palabra)
        layout_izq.addWidget(self.etiqueta)
        layout_izq.addWidget(self.boton_letra)
        layout_izq.addWidget(self.boton_reset)

        layout_der = QVBoxLayout()
        layout_der.addWidget(self.foto)

        layout_der.addWidget(self.Usadas)
        layout_der.addWidget(self.Disponibles)

        layout = QHBoxLayout()
        layout.addLayout(layout_izq)
        layout.addLayout(layout_der)
        self.setLayout(layout)






        self.show()
    def keyPressEvent(self, event):
        """
        Este método maneja el evento que se produce al presionar las teclas.
        """
        self.letra = event.text()
        self.etiqueta.setText(str(letra))
        self.etiqueta.resize(self.etiqueta.sizeHint())

    def Ingresar_letra(self):
        letra = self.letra
        self.enviar_letra_signal.emit({"letra" : letra})

    def reiniciar(self):
        self.reiniciar_signal.emit()

    def Turno(self, dic):
        self.usadas = dic["usadas"]
        self.disponibles = dic["disponibles"]
        self.palabra = dic["palabra"]
        dic["imagen"] = self.imagen
        self.Palabra.setText(self.palabra)
        self.Palabra.resize(self.Palabra.sizeHint())
        self.Usadas.setText(self.usadas)
        self.Usadas.resize(self.Usadas.sizeHint())
        self.Disponibles.setText(self.disponibles)
        self.Disponibles.resize(self.Disponibles.sizeHint())
