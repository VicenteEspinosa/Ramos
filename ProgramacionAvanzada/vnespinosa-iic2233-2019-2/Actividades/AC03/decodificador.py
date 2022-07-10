from itertools import chain


def decodificar(string):
    arquetipos = "arquetipos"
    numeros = "0123456789"
    resultado = str("")
    for caracter in str(string):
        if caracter in arquetipos:
            caracter = numeros[arquetipos.index(caracter)]
        elif caracter in numeros:
            caracter = arquetipos[numeros.index(caracter)]
        resultado += caracter

    return resultado

if __name__ == "__main__":
    tests = [
        "66cqquu",
        "P18g10m0c68n 0v0nz0d0 qaro-q",
        "E950 49 3n0 7134b0 d4l d4c8d6f6c0d81",
        "S6 734d49 l441 4958, 58d8 h0 90l6d8 m3y b64n!!"]


    print("  ---  PRUEBA DE DECODIFICADO ---  ")
    for test in tests:
        print(decodificar(test), "\n")
