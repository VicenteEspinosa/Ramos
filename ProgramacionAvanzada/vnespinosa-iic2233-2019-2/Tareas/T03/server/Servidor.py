import socket
import threading #Para escuchar multiples usuarios
import parametros as P

#Guardar quien esta en que sala. Ver que pasa y en que sala, y enviarlo a todos los que esten en esta.
#servidor.sala1 = [sockets]
# back end es usuario

class Servidor():

    def __init__(self):
        self.host = socket.gethostname()
        self.port = P.port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.usuarios = [] #Podria no estar en una sala
        self.sala1 = []
        self.sala2 = []
        self.sala3 = []
        self.sala4 = []
        self.sala5 = []
        print("Servidor iniciado.")

    def Escuchar(self): #Hacer threading de esto, para el maximo de usuarios
        self.socket_servidor.listen()
        socket_cliente, (host_cliente, port_cliente) = self.socket_servidor.accept()
        print(f"Conecxion recibida de {host_cliente}")
        self.usuarios.append(socket_cliente)
        self.Interacutar(socket_cliente)

    def Interacutar(self, socket_cliente):
        dia = 0
