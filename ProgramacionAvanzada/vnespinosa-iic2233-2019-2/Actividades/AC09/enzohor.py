import pickle
import re


class Piloto:
    def __init__(self, nombre, alma, edad, *args, **kwargs):
        self.nombre = nombre
        self.alma = alma
        self.edad = edad

    def __setstate__(self, state):
        aumentar_sincronizacion(state)
        self.__dict__ = state

def cargar_almas(ruta):
    with open(ruta, 'rb') as file:
        lista = pickle.load(file)
    return lista

def aumentar_sincronizacion(estado):
    for alma in estado["alma"]:
        borrar = []
        cont = 0
        E = False
        G = False
        for letra in str(alma):
            if letra == "E":
                E = True
                inicio = int(cont)
                G = False
            elif letra == "G":
                G = True
            elif letra == "O":
                if E and G:
                    borrar.append([inicio, int(cont)])
                E = False
                G = False
            cont += 1
    for ptos in borrar:
        print(ptos)
        primer = alma[0:ptos[0]]
        segunda = alma[ptos[1]:]
        alma = primer + segunda
    estado.update({"alma" : alma})


if __name__ == '__main__':
    try:
        pilotos = cargar_almas('pilotos.magi')
        if pilotos:
            print("ENZOHOR200: Sincronizacion de los pilotos ESTABLE.")

    except Exception as error:
        print(f'Error: {error}')
        print("ENZOHOR501: CRITICO Sincronizacion de los pilotos INESTABLE")
