import socket
import json
import pickle

class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        self.host = socket.gethostname()
        self.port = 9000
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Aqui deberas intentar conectar al servidor.
            self.socket_cliente.connect((self.host, self.port))
            # Completar hasta aquí
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje
        # Rayos, esto es demasiado poco

        largo_archivo = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')
        datos = bytearray()
        while len(datos) < largo_archivo:
            bytes_leer = min(4096, largo_archivo - len(datos))
            datos_recibidos = self.socket_cliente.recv(bytes_leer)
            datos.extend(datos_recibidos)
        mensaje = datos.decode('utf-8')
        continuar = bool.from_bytes(self.socket_cliente.recv(4096), byteorder='big')




        # Debe haber un string para imprimirse
        # Debe haber un boolean para saber si continuar funcionando
        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar
        if str(input_usuario) == "\juego_nuevo":  #Sin argumentos
            return str(input_usuario)
        elif str(input_usuario[:7]) == "\jugada": # Columna
            if str(input_usuario[7]) == " ": #ver que hay espacio
                if str(input_usuario[8:]).isnumeric(): #Ve que sea digito entero
                    return str(input_usuario)
        elif str(input_usuario) == "\salir": #Sin argumentos
            return str(input_usuario)
        return None

        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        mensaje_codificado = accion.encode('utf-8')
        largo = len(mensaje_codificado)
        self.socket_cliente.sendall(largo.to_bytes(4, byteorder='big'))
        self.socket_cliente.sendall(mensaje_codificado)
        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
