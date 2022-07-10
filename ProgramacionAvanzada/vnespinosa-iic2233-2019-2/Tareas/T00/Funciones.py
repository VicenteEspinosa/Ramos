import random
import os.path
from parametros import POND_PUNT, PROB_LEGO
from tablero import print_tablero

def Entre_3_15(e):
  x = False
  N = str(input("Ingrese el numero de " + str(e) + ": "))
  while x == False:
    if not N.isdigit():
      N = str(input(("Ingrese un numero por favor: ")))
    if N.isdigit():
      if int(N)<= 15 and int(N)>=3:
        x = True
      else:
          N = str(input("El numero debe ser entre 3 y 15, intentalo otra vez: "))
  return N
if __name__ == "__Entre_3_15__":
    Entre_3_15()

def inicio():
    print("Seleccione una opción:")
    print("[1] Crear partida")
    print("[2] Cargar partida")
    print("[3] Ver ranking")
    print("[0] Salir")
    opcion = str(input("- "))
    x = False
    while not x:
        if not opcion.isdigit():
            print("Por favor ingrese un numero")
            opcion = str(input())
        else:
            if  0 <= int(opcion) <= 3 :
                x = True
            else:
                print("Ingrese uno de los numeros indicados:")
                opcion = str(input())
    if opcion == "0":
        exit()

    elif opcion == "1":
        print("Ingrese su nombre: ")
        print("Por favor no uses 'espacios'")
        nombre = str(input("- "))
        filas = int(Entre_3_15("filas"))
        columnas = int(Entre_3_15("columnas"))
        lista_solucion = gen_tablero(int(filas),int(columnas))
        lista_visible = gen_lista_visible(lista_solucion,filas,columnas)
        lista_marcadas = []
        listaa = []
        for i in lista_visible:
            for j in i:
                listaa.append(" ")
            lista_marcadas.append(listaa)
            listaa = []
        todo = [lista_visible,lista_solucion,lista_marcadas,[columnas,filas],nombre,"0"]
    elif opcion == "2":
        todo =  Cargar_partida()

    elif opcion == "3":
        file = open("puntajes.txt")
        lista1 = []
        lista2 = []
        for line in file:
            for categoria in line.split("],"):
                for lista in categoria.split(","):
                    for caracter in lista:
                        if caracter not in (["]","[","'",","," "]):
                            lista1.append(caracter)
                    lista2.append(lista1)
                    lista1 = []
        nombres = []
        palabra = ""
        l = len(lista2)
        for num in range(0,int(l/2)):
            nombre = lista2[num]
            for caracter in nombre:
                if caracter not in ["]", "," ," ", '\"']:
                    palabra += str(caracter)
            nombres.append(palabra)
            palabra = ""
        puntajes = []
        for num in range(int(l/2),int(l)):
            punt = lista2[num]
            for caracter in punt:
                if caracter not in ["]", "," ," ", '\"']:
                    palabra += str(caracter)
            puntajes.append(palabra)
            palabra = ""
        print(" ")
        print("Ranking:")
        for i in range(len(nombres)):
            print( str(int(i) + 1) + "° " + str(nombres[i]) + " --- " + str(puntajes[i]) )
        print(" ")
        todo = inicio()
    return todo

if __name__ == "__inicio__":
    inicio()

def turno(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre,turnos):
    print("")
    print("¿Que quieres hacer ahora?:")
    print("[1] Descubrir una baldosa")
    print("[2] Guardar partida")
    print("[3] Salir y guardar")
    print("[0] Salir sin guardar")
    opcion = str(input("- "))
    x = False
    while not x:
        if not opcion.isdigit():
            print("Por favor ingrese un numero")
            opcion = str(input("- "))
        else:
            if  0 <= int(opcion) <= 3 :
                x = True
            else:
                print("Ingrese uno de los numeros indicados:")
                opcion = str(input("- "))
    if int(opcion) == 0:
        exit()

    if int(opcion) == 1:
        todo = Revelar_baldosa(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre)

    if int(opcion) == 2:
        Guardar_partida(lista_visible,lista_marcadas,lista_solucion,columnas,filas,nombre,str(turnos))
        todo = [lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre,False]

    if int(opcion) == 3:
        Guardar_partida(lista_visible,lista_marcadas,lista_solucion,columnas,filas,nombre,str(turnos))
        exit()
    return todo


if __name__ == "__turno__":
    turno()


def gen_tablero(columnas,filas):
    l = float(int(columnas) * int(filas) * float(PROB_LEGO))
    legos = 0
    while l > 0:
        legos += 1
        l -= 1
    lista = []
    for i in range(int(columnas)):
        list = []
        for i in range(int(filas)):
            list.append("v")
        lista.append(list)
    while legos > 0:
        c = random.randint(0,int(columnas))
        f = random.randint(0,int(filas))
        while lista[c - 1][f - 1] == "L":
            c = random.randint(0,int(columnas))
            f = random.randint(0,int(filas))
        lista[c - 1][f - 1] ="L"
        legos -= 1
    return lista

if __name__ == "__gen_tablero(a,b)__":
    gen_tablero(a,b)

def Cargar_partida():
    lista1 = []
    lista2 = []
    lista3 = []
    conta = 0
    print("¿Como se llama el archivo que desea cargar?")
    print("(No incluya en .txt al final)")
    carg = str(input("- "))
    carga = str(carg) + ".txt"
    path = os.listdir("Partidas")
    while (not os.path.exists("Partidas/" + carga)):
        print("No se encuentra ningun archivo con ese nombre")
        print("Recuerda que deben estar en la misma carpeta del programa")
        print("¿Como se llama el archivo que desa cargar?")
        carg = str(input())
        carga = str(carg) + ".txt"
    file = open("Partidas/" + carga)
    for i in file:
        j = i
    for categoria in j.split("]], "):
        for lista in categoria.split("], "):
            if conta == 2:
                lista = lista.replace(", ","")
            for caracter in lista:
                if caracter not in (["]","[","'",","," "]) and (not conta ==2) :
                    lista1.append(caracter)
                elif conta == 2:
                    if caracter not in (["]","[","'",","]):
                        lista1.append(caracter)
            lista2.append(lista1)
            lista1 = []
        lista3.append(lista2)
        lista2 = []
        conta += 1
    lista_visible = lista3[0]
    lista_solucion = lista3[1]
    lista_marcadas = lista3[2]
    columna_fila = lista3[3][0]
    nombre = ""
    turnos = lista3[3][2]
    for i in lista3[3][1]:
        if i not in [","," ","'"]:
            nombre += str(i)

    return [lista_visible,lista_solucion,lista_marcadas,columna_fila,nombre,turnos]

if __name__ == "__Cargar_partida()__":
    Cargar_partida()


def gen_lista_visible(lista_solucion, columnas,filas):
    lista1 = []
    lista2 = []
    contador = 0
    for c in range(int(columnas)):
        for f in range(int(filas)):
            if lista_solucion[c][f] == "v":
                for i in range(-1,2):
                    for j in range(-1,2):
                        if ((f + i) >= 0) and ((c + j) >= 0) and ((f + i) <= int(filas) - 1) and ((c + j) <= int(columnas) - 1):
                             if lista_solucion[c + j][f + i] == "L":
                                 contador += 1
                lista1.append(contador)
                contador = 0
            else:
                lista1.append("L")
        lista2.append(lista1)
        lista1 = []
    return lista2


def Guardar_partida(lista_visible, lista_marcadas, lista_solucion, columnas, filas, nombre, turno):
    print("Su archivo se guardara en la carpeta 'Partidas' ")
    print("El nombre sera el nombre que ingreso al principio")
    f = open("Partidas/" + str(nombre) + ".txt","w")
    f.write(str([lista_visible,lista_solucion,lista_marcadas,[columnas,filas],[nombre],[turno]]))
    f.close()

def Revelar_baldosa(lista_visible, lista_solucion, lista_marcadas, columnas, filas, nombre):
    perdio = False
    print("Ingresa las coordenas de la baldosa que quieres revelar:")
    print("Por ejemplo: A0")
    print("Si quieres retroceder al menu anterior ingresa 'r' ")
    coord = str(input("- "))
    if coord.lower() == "r":
        return [lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre,False]
    posib = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posib2 = ""
    posib3 = ""
    for i in range(int(columnas)):
        posib2 += str(posib[i])
    for i in range(int(filas)):
        posib3 += str(i)
    if not len(coord) == 2:
        bueno = False
        print("Coordenadas incorrectas ")
    elif (coord[0].upper() not in posib2) or (coord[1] not in posib3):
        bueno = False
        print("Coodenadas incorrectas ")
    elif len(coord) == 2:
        for i in range(len(posib2)):
            if posib2[i] == coord[0].upper():
                letra = i
        if lista_marcadas[int(coord[1])][int(letra)] == " ":
            bueno = True
        else:
            bueno = False
            print("Esa baldosa ya esta descubierta")
    else:
        print("Por favor, ingrese solo dos caracteres")
        bueno = False
    while not bueno:
        print("intentalo otra vez:")
        coord = str(input("- "))
        if coord.lower() == "r":
            return [lista_visible,lista_marcadas,lista_solucion,columnas,filas,nombre]
        if (coord[0].upper() not in posib2) or (coord[1] not in posib3):
            bueno = False
            print("Coodenadas incorrectas ")
        elif len(coord) == 2:
            for i in range(len(posib2)):
                if posib2[i] == coord[0].upper():
                    letra = i
            if lista_marcadas[int(coord[1])][int(letra)] == " ":
                bueno = True
            else:
                bueno = False
                print("Esa baldosa ya esta descubierta")
    lista_marcadas[int(coord[1])][int(letra)] = lista_visible[int(coord[1])][int(letra)]
    perdio = Perdio(coord, letra, lista_solucion)
    if perdio:
        print("Lo siento, destapaste un Lego, perdiste")
    return [lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre,perdio]

def Perdio(coord, letra, lista_solucion):
    if lista_solucion[int(coord[1])][int(letra)] == "L":
        perdio = True
    else:
        perdio = False
    return perdio

def Revelar_todo(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre):
    for i in range(len(lista_solucion)):
        for j in range(len(lista_solucion[i])):
            if lista_solucion[i][j] == "L":
                lista_marcadas[i][j] = "L"
    return [lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre]

def Gano(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre):
    gano = True
    for i in range(len(lista_solucion)):
        for j in range(len(lista_solucion[i])):
            if (lista_solucion[i][j] == "v") and (lista_marcadas[i][j] == " "):
                gano = False
    return gano

def Actualizar_Puntajes(puntaje,nombre1):
    file = open("puntajes.txt")
    lista1 = []
    lista2 = []
    for line in file:
        for categoria in line.split("],"):
            for lista in categoria.split(","):
                for caracter in lista:
                    if caracter not in (["]","[","'",","," "]):
                        lista1.append(caracter)
                lista2.append(lista1)
                lista1 = []
    file.close()
    nombres = []
    palabra = ""
    l = len(lista2)
    for num in range(0,int(l/2)):
        nombre = lista2[num]
        for caracter in nombre:
            if caracter not in ["]", "," ," ", '\"']:
                palabra += str(caracter)
        nombres.append(palabra)
        palabra = ""
    puntajes = []
    for num in range(int(l/2),int(l)):
        punt = lista2[num]
        for caracter in punt:
            if caracter not in ["]", "," ," ", '\"']:
                palabra += str(caracter)
        puntajes.append(palabra)
        palabra = ""
    l = len(nombres)
    mayor = False
    for i in range(l):
        if int(puntaje) > int(puntajes[i]):
            mayor = True
            resultado = str(puntaje)
            index = i
            puntaje = -1
    if mayor:
        nombres.insert(index,nombre1)
        puntajes.insert(index,resultado)
    elif len(puntajes) < 10:
            nombres.insert(len(puntajes),nombre1)
            puntajes.insert(len(puntajes),puntaje)
    if len(puntajes) > 10:
        del nombres[len(puntajes) - 1]
        del puntajes[len(puntajes) - 1]
    f = open("puntajes.txt","w")
    lista1 = []
    lista2 = []
    for i in nombres:
        lista1.append(str(i))
    lista3 = "[" + str(lista1)
    for j in puntajes:
        lista2.append(str(j))
    lista4 = (lista3 + "," + str(lista2) + "]")
    lista4 = str(lista4.replace(" ",""))
    f.write(str(lista4))
    f.close()

def Revisar_ceros(lista_visible,lista_marcadas,columnas,filas):
    contador = 1
    while contador == 1:
        contador = 0
        for c in range(int(columnas)):
            for f in range(int(filas)):
                if str(lista_marcadas[c][f]) == "0":
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if ((f + i) >= 0) and ((c + j) >= 0) and ((f + i) <= int(filas) - 1) and ((c + j) <= int(columnas) - 1):
                                if (lista_marcadas[c + j][f + i] == " "):
                                    lista_marcadas[c + j][f +i] = lista_visible[c + j][f + i]
                                    contador = 1
    return lista_marcadas
