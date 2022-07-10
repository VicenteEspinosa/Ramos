import socket
import json
import pickle
from juego import Juego


class Servidor:

    def __init__(self):
        '''Inicializador de servidor.

        Crea socket de servidor, lo vincula a un puerto.'''
        # Completar y agregar argumentos desde aquí

        self.host = socket.gethostname()
        self.port = 9000
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Aqui deberas preparar el socket para que escuche una conexion
        self.socket_servidor.bind((self.host, self.port))
        #self.socket_servidor.listen() creo que va despues?
        # Completar y agregar argumentos hasta aquí
        # -----------------------------------------
        print("Servidor iniciado.")
        self.juego = None  # Juego comienza nulo.
        self.socket_cliente = None  # Aún no hay cliente.

    def esperar_conexion(self):
        '''Espera a la conectarse con un cliente y obtiene su socket.'''
        print("Esperando cliente...")
        # --------------------
        # Completar desde aquí
        if not self.socket_cliente:
            self.socket_servidor.listen()
            self.socket_cliente, (host_cliente, port_cliente) = self.socket_servidor.accept()
        # Debes actualizar el valor de self.socket_cliente al conectar

        # Completar hasta aquí
        # --------------------
        print("¡Servidor conectado a cliente!")
        self.interactuar_con_cliente()

    def interactuar_con_cliente(self):
        '''Comienza ciclo de interacción con cliente.

        Recibe un acción y responde apropiadamente.'''
        self.enviar_estado('', True)
        while self.socket_cliente:
            accion = self.recibir_accion()
            self.manejar_accion(accion)

    def enviar_estado(self, mensaje, continuar):
        '''Envia estado del juego en el servidor.'''
        acciones = ""
        if continuar:
            if self.juego is not None:
                mensaje = f'{self.juego.tablero_string()}\n{mensaje}\n'
            acciones = ("¿Qué deseas hacer?\n"
                        "Para jugar nuevo juego: \\juego_nuevo\n"
                        "Para jugar en una columna: \\jugada columna\n"
                        "Para salir: \\salir\n")
        mensaje_final = mensaje + acciones
        # -----------------------------------------------------
        # Completar y usar un metodo para todo largo de mensaje
        mensaje_codificado = mensaje_final.encode("utf-8")
        largo = len(mensaje_codificado) #aaaaaa
        self.socket_cliente.sendall(largo.to_bytes(4, byteorder='big'))
        self.socket_cliente.sendall(mensaje_codificado)
        self.socket_cliente.sendall(continuar.to_bytes(4096, byteorder='big'))

        # Completar hasta aquí
        # --------------------

    def recibir_accion(self):
        '''Recibe mensaje desde el cliente y lo decodifica.'''
        # -----------------------------------------------------
        # Completar y usar un metodo para todo largo de mensaje





        largo_archivo = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')
        datos = bytearray()
        while len(datos) < largo_archivo:
            bytes_leer = min(4096, largo_archivo - len(datos))
            datos_recibidos = self.socket_cliente.recv(bytes_leer)
            datos.extend(datos_recibidos)
        accion = datos.decode('utf-8')


        # Completar hasta aquí
        # --------------------
        return accion

    def manejar_accion(self, accion):
        #'''Maneja la acción recibida del cliente.'''
        print(f'Acción recibida: {accion}')
        # --------------------
        # Completar desde aquí
        if str(accion) == "\juego_nuevo":
            tipo = '\\juego_nuevo'
        elif str(accion) == "\salir":
            tipo = '\\salir'  # Obtener el tipo de acción que envió el cliente.
        else:
            tipo = '\\jugada'


        # Completar hasta aquí
        # --------------------
        if tipo == '\\juego_nuevo':
            self.juego = Juego()
            self.juego.crear_tablero()
            self.enviar_estado('', True)
        elif tipo == '\\salir':
            self.enviar_estado('¡Adios!', False)
            self.juego = None
            self.socket_cliente.close()
            print('Cliente desconectado.\n')
            self.socket_cliente = None
        elif tipo == '\\jugada':
            if self.juego is None:
                self.enviar_estado('Ningún juego ha iniciado.', True)
            else:
                # --------------------
                # Completar desde aquí
                # Obtener la jugada que envió el cliente.
                jugada = int(accion[8:])


                # Completar hasta aquí
                # --------------------
                if not self.juego.es_jugada_valida(jugada):
                    self.enviar_estado('Jugada inválida.', True)
                else:
                    gano = self.juego.turno_jugador(jugada)
                    if gano:
                        self.enviar_estado('¡Ganaste! Se acabó el juego.', True)
                        self.juego = None
                    else:
                        perdio = self.juego.turno_cpu()
                        if perdio or self.juego.empate():
                            self.enviar_estado('No ganaste :( Se acabó el juego.', True)
                            self.juego = None
                        else:
                            self.enviar_estado('', True)


if __name__ == "__main__":
    servidor = Servidor()
    while True:
        try:
            servidor.esperar_conexion()
        except KeyboardInterrupt:
            print("\nServidor interrumpido")
            break
