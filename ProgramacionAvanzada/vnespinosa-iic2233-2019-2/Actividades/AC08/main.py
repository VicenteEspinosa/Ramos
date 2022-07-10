from cargar import cargar_archivos
from os import path


class Usuario: #Nodo
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = []
        # self.seguidores = [] # almacenar a los seguidores es opcional.

    #def __repr__(self):
    #    return self.id


class Pintogram: #Grafo
    def __init__(self):
        self.seguidores = dict()
        self.ids = dict()

    def nuevo_usuario(self, id_usuario, nombre):
        usuario = Usuario(id_usuario, nombre)
        self.ids[id_usuario] = usuario

    def follow(self, id_seguidor, id_seguido):
        if id_seguidor in self.ids:
            self.ids[id_seguidor].seguidos.append(id_seguido)

    def cargar_red(self, ruta_red):
        with open(ruta_red, encoding="utf-8") as file:
            for line in file:
                line = line.replace("\n", "")
                if ";" in line:
                    comilla = True
                else:
                    comilla = False
                line = line.split(";")
                info = str(line[0]).split(",")
                if comilla:
                    seguidos = line[1]
                self.nuevo_usuario(info[0], info[1])
                self.follow(info[0], info[2])
                if comilla:
                    for seguido in seguidos:
                        self.follow(info[0], seguido)
    def unfollow(self, id_seguidor, id_seguido):
        if id_seguido in self.ids[id_seguidor].seguidos:
            self.ids[id_seguidor].seguidos.remove(id_seguido)

    def mis_seguidos(self, id_usuario):
        return len(self.ids[id_usuario].seguidos)

    def distancia(self, id_usuario1, id_usuario2, n, revisados):
        Usuario1 = self.ids[id_usuario1]
        por_ver = Usuario1.seguidos
        if id_usuario2 in Usuario1.seguidos:
            return n + 1
        for Usuario in revisados:
            if Usuario in por_ver:
                por_ver.remove(Usuario)
        if len(por_ver) > 0:
            n += 1
            dist = []
            for seguido in por_ver:
                revisados.append(seguido)
            numeros = []
            for seguido in por_ver:
                j = self.distancia(seguido, id_usuario2, n, revisados)
                dist.append(j)
            for j in dist:
                if type(j) == int:
                    numeros.append(j)
            if len(numeros) > 0:
                numeros.sort()
                return numeros[0]
            else:
                return "infinito"
        return "infinito"

    def distancia_social(self, id_usuario_1, id_usuario_2):
        lista = []
        lista.append(id_usuario_1)
        lista.append(id_usuario_2)
        return self.distancia(id_usuario_1, id_usuario_2, 0, lista)



if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "simple.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
    print(pintogram.distancia_social("3", "5"))

# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
