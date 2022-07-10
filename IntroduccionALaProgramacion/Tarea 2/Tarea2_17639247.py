import sys
def turno(rol):
    global salir
    salir = False
    for linea in tablero:
            str1 = "".join(linea)
            print(str1)
    print("Es tu turno " + rol + ", ¿Cuál es tu movimiento?")
    print("¿o deseas guardar la partida y salir (G)?")
    print("¿o simplemente salir (S)?")
    movimiento = str(input())
    mal = True
    while mal:
        if len(movimiento) != 7:
            if movimiento == "S" or movimiento == "s":
                salir = True
                mal = False
                sys.exit()
            elif movimiento == "G" or movimiento == "g":
                mal = False
                file = str(input("¿Que nombre quieres darle al archivo?: "))
                file = open(file, 'w')
                for linea in guardado:
                     file.write(linea + '\n')
                file.close()
                salir = True
                sys.exit()
        elif len(movimiento) == 7:
                if (movimiento[0] != "0" and movimiento[0] != "1" and movimiento[0] != "2" and movimiento[0] != "3" and movimiento[0] != "4") or (movimiento[2] != "0" and movimiento[2] != "1" and movimiento[2] != "2"and movimiento[2] != "3" and movimiento[2] != "4") or (movimiento[4] != "0" and movimiento[4] != "1" and movimiento[4] != "2" and movimiento[4] != "3" and movimiento[4] != "4") or (movimiento[6] != "0" and movimiento[6] != "1" and movimiento[6] != "2" and movimiento[6] != "3" and movimiento[6] != "4") or (movimiento[1] != ",") or (movimiento[3] != ",") or (movimiento[5] != ","):
                    mal = True
                else:
                    mal = False
        if mal:
            movimiento = str(input("Comando incorrecto, por favor intentalo otra vez: "))
        elif not salir:
            if validar(movimiento[0],movimiento[2],movimiento[4],movimiento[6]):
                mal = False
            else:
                mal = True
                movimiento = str(input("Comando incorrecto, por favor intentalo otra vez: "))
    return movimiento
def Puede_mas():
    for x in range(x_coyote - 2, x_coyote + 3):
        for y in range(y_coyote -2, y_coyote + 3):
                if (abs(x - x_coyote) > 1) or (abs(y - y_coyote) > 1):
                    x2 = int((x - int(x_coyote))/2) + int(x_coyote)
                    y2 = int((y - int(y_coyote))/2) + int(y_coyote)
                    valido = validar(x_coyote,y_coyote,x2,y2)
                    if (x2 < 0) or (x2 > 4) or (y2 < 0) or (y2 > 4) or (x < 0) or (x > 4) or (y < 0) or (y > 4):
                        valido = False
                    if valido:
                        valide = validar(x2,y2,x,y)
                        if valide:
                            if tablero[y*2][x*2] == "N":
                                if tablero[y2*2][x2*2] == "G":
                                    return True
    return False
def MovimientoGallina(xi,yi,xf,yf):
        tablero[yi*2][xi*2] = "N"
        tablero[yf*2][xf*2] = "G"
def contar_gallinas():
    gallinas = 0
    for linea in tablero:
        for letra in linea:
            if letra == "G":
                gallinas += 1
    return gallinas
def validar(xi,yi,xf,yf):
    valido = True
    if xi == 0:
        if yi == 0:
            if xf > 1:
                valido = False
            if yf > 1:
                valido = False
            if (xf == 0) and (yf == 0):
                valido = False
        if yi == 1:
            if xf == 1:
                if yf != 1:
                    valido = False
            elif xf == 0:
                if (yf != 0) and (yf != 2):
                    valido = False
            else: 
                valido = False
        if yi == 2:
            if xf == 0:
                if (yf != 1) and (yf != 3):
                    valido = False
            elif xf == 1:
                if (yf != 1) and (yf != 2) and (xf != 3):
                    valido = False
            else:
                valido = False
        if yi == 3:
            if xf == 0:
                if (yf != 2) and (yf != 4):
                    valido = False
            elif xf == 1:
                if (yf != 3):
                    valido = False
            else:
                valido = False
        if yi == 4:
            if xf == 0:
                if yf != 3:
                    valido = False
            elif xf == 1:
                if (yf != 3) and (yf != 4):
                    valido = False
            else:
                valido = False
    elif xi == 1:
        if yi == 0:
            if xf == 0:
                if (yf != 0):
                    valido = False
            elif xf == 1:
                if (yf != 1):
                    valdo = False
            elif xf == 2:
                if (yf != 0):
                    valido = False
            else:
                valido = False
        elif yi == 1:
            if (abs(yf - yi) > 1) or (abs(xf - xi) > 1):
                valido = False
            if (yf == yi) and (xf == xi):
                valido = False
        elif yi == 2:
            if xf == 1:
                if (yf != 1) and (yf != 3):
                    valido = False
            elif yf == 2:
                if (xf != 0) and (xf != 2):
                    valido = False
            else:
                valido = False
        elif yi == 3:
            if (abs(yf - yi) > 1) or (abs(xf - xi) > 1):
                valido = False
            if (xf == xi) and (yi == yf):
                valido = False
        elif yi == 4:
            if yf == 4:
                if (xf != 0) and (xf != 2):
                    valido = False
            elif yf == 3:
                if (xf != 1):
                    valido = False
            else:
                valido = False
    elif xi == 2:
        if yi == 0:
            if yf == 0:
                if (xf != 1) and (xf != 3):
                    valido = False
            elif yf == 1:
                if (xf != 1) and (xf != 2) and (xf != 3):
                    valido = False
            else:
                valido = False
        elif yi == 1:
            if xf == 2:
                if (yf != 0) and (xf != 2):
                    valido = False
            elif yf == 1:
                if (xf != 1) and (xf != 3):
                    valido = False
            else:
                valido = False
        elif yi ==  2:
            if (abs(yf - yi) > 1) or (abs(xf - xi) > 1):
                valido = False
            if (yf == yi) and (xf == xi):
                valido = False
        elif yi == 3:
            if yf == 3:
                if (xf != 1) and (xf != 3):
                    valido = False
            elif xf == 2:
                if (yf != 2) and (yf != 4):
                    valido = False
            else:
                valido = False
        elif yi == 4:
            if yf == 3:
                if (xf != 1) and (xf != 2) and (xf != 3):
                    valido = False
            elif yf == 4:
                if (xf != 1) and (xf != 3):
                    valido = False
            else:
                valido = False
    elif xi == 3:
        if yi == 0:
            if yf == 0:
                if (xf != 2) and (xf != 4):
                    valido = False
            elif yf == 1:
                if (xf != 2) and (xf != 3) and (xf != 4):
                    valido = False
            else:
                valido = False
        elif yi == 1:
            if (abs(yf - yi) > 1) or (abs(xf - xi) > 1):
                valido = False
            if (yf == yi) and (xf == xi):
                valido = False
        elif yi == 2:
            if xf == 3:
                if (yf != 1) and (yf != 3):
                     valido = False
            elif yf == 2:
                if (xf != 2) and (xf != 4):
                     valido = False
            else:
                 valido = False
        elif yi == 3:
            if (abs(yf - yi) > 1) or (abs(xf - xi) > 1):
                valido = False
            if (yf == yi) and (xf == xi):
                valido = False
        elif yi == 4:
            if yf == 4:
                if (xf != 2) and (xf != 4):
                    valido = False
            elif yf == 3:
                if xf != 3:
                    valido = False
                else:
                    valido = False
    elif xi == 4:
        if yi == 0:
            if yf == 0:
                if xf != 3:
                    valido = False
            elif yf == 1:
                if xf != 4:
                    valido = False
            else:
                valido = False
        elif yi == 1:
            if xf == 4:
                if (yf != 0) and (yf != 2):
                    valido = False
            elif xf == 3:
                if yf != 1:
                    valido = False
            else:
                valido = False
        elif yi == 2:
            if xf == 3:
                if (yf != 1) and (xf != 2) and (xf != 3):
                    valido = False
            elif xf == 4:
                if (yf != 1) and (yf != 3):
                    valido = False
            else:
                valido = False
        elif yi == 3:
            if xf == 3:
                if yf != 3:
                    valido = False
            elif xf == 4:
                if (yf != 2) and (yf != 4):
                    valido = False
            else:
                valido = False
        elif yi == 4:
            if xf == 4:
                if yf != 3:
                    valido = False
            elif xf == 3:
                if (yf != 3) and (yf != 4):
                    valido = False
            else:
                valido = False
    return valido
## ---------------------------------------------------------------------------------------------------------------------------
## -------------------------- EMPIEZA PROGRAMA  ------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------------
salir = False
saltar = False
while not salir:
    perdedor = False
    while not perdedor:
        perdedor = False
        guardado = []
        tablero = [["G","-","G","-","G","-","G","-","G"],["|\|/|\|/|"], ["G","-","G","-","G","-","G","-","G"],["|/|\|/|\|"],["G","-","N","-","C","-","N","-","G"],["|\|/|\|/|"],["N","-","N","-","N","-","N","-","N"],["|/|\|/|\|"],
                   ["N","-","N","-","N","-","N","-","N"]]
        print("¡Bienvenido al juego del coyote y las gallinas!")
        empezar = str(input("¿Quieres cargar una partida (1) o empezar de nuevo (2)? "))
        while empezar != "1" and empezar != "2":
            empezar = str(input("Debes responder con 1 o 2, por favor intentalo otra vez: "))
        if empezar == "1":
            file = str(input("¿Cual es el nombre del archivo?: "))
            file = open(file)
            contador = 0
            for line in file:
                print(line.rstrip())
                guardado += [line.rstrip()]
                if contador == 0:
                    line = line.split(",")
                    coyote = line[0]
                    gallina = line[1]
                if contador != 0:
                    if line[0] == "G":
                        MovimientoGallina(int(line[2]),int(line[4]),int(line[6]),int(line[8]))
                        ultimo = "G"
                    elif line[0] == "C":
                        ultimo = "C"
                        xi = int(line[2])
                        yi = int(line[4])
                        xf = int(line[6])
                        yf = int(line[8])
                        if (abs(xi - xf) > 1) or (abs(yi - yf) > 1):
                            x2 = int((xf - xi)/2 + xi)
                            y2 = int((yf - yi)/2 + yi)
                            tablero[yi*2][xi*2] = "N"
                            tablero[y2*2][x2*2] = "N"
                            tablero[yf*2][xf*2] = "C"
                        else:
                            tablero[yf*2][xf*2] = "C"
                            tablero[yi*2][xi*2] = "N"
                contador += 1
            for linea in tablero:
                if "C" in linea:
                    x_coyote = linea.index("C")
                    if x_coyote != 0:
                        x_coyote /= 2
                        x_coyote = int(x_coyote)
                    y_coyote = tablero.index(linea)
                    if y_coyote != 0:
                        y_coyote /= 2
                        y_coyote = int(y_coyote)
            posicion_coyote = (x_coyote,y_coyote)
            perdio_coyote = True
            perdedor = False
            for x in range(x_coyote - 1, x_coyote + 2):
                for y in range(y_coyote -1, y_coyote + 2):
                    if (x,y) != posicion_coyote:
                        valido = validar(x_coyote,y_coyote,x,y)
                        if valido:
                            if tablero[y*2][x*2] == "N":
                                perdio_coyote = False
            if perdio_coyote:
                for x in range(x_coyote - 2, x_coyote + 3):
                    for y in range(y_coyote -2, y_coyote + 3):
                            if (x,y) != posicion_coyote:
                                x2 = ((x - x_coyote)/2) + x_coyote
                                y2 = ((y - y_coyote)/2) + y_coyote
                                valido = validar(x_coyote,y_coyote,x2,y2)
                                if valido:
                                    valido = validar(x2,y2,x,y)
                                    if valido:
                                        if tablero[y*2][x*2] == "N":
                                            perdio_coyote = False
            if perdio_coyote:
                perdedor = True
            if ultimo == "G":
                saltar = True
        elif empezar == "2":
            coyote = str(input("¡Perfecto! Dime el nombre del jugador que será el coyote: "))
            gallina = str(input("Dime el nombre del jugador que será las gallinas: "))
            while coyote == gallina:
                print("No puede ser la misma persona ambos roles, por favor intentalo otra vez")
                coyote = str(input("Dime el nombre del jugador que será el coyote: "))
                gallina = str(input("Dime el nombre del jugador que será las gallinas: "))
            print("¡Comencemos!")
            guardado += [coyote + "," + gallina]
        while perdedor == False:
            gallina_perdio = True
            if contar_gallinas() > 10:
                gallina_perdio = False
            if gallina_perdio:
                for linea in tablero:
                        str1 = "".join(linea)
                        print(str1)
                print("El juego termino!")
                print("Ganó el coyote!")
                print("¿Deseas guardar la partida ? (G)")
                print("Salir del juego (S)")
                respuesta = str(input("¿O quieres empezar de nuevo? (E)"))
                while (respuesta != "S") and (respuesta != "s") and (respuesta != "G") and (respuesta != "g") and (respuesta != "E") and (respuesta != "e"):
                    respuesta = str(input("Por favor, responde con alguna de las opciones dadas: "))
            if (gallina_perdio == False) and (saltar == False) and (salir == False):
                movimiento = turno(gallina)
                if movimiento == "S" or movimiento == "s" or movimiento == "g" or movimiento == "G":
                    salir = True
                    perdedor = True
                    respuesta = "S"
                valido = False
                while (valido == False) and (salir == False):
                    # Revisar si es str o int primero
                    valido = validar(int(movimiento[0]),int(movimiento[2]),int(movimiento[4]),int(movimiento[6]))
                    if valido:
                        xi = int(movimiento[0])
                        yi = int(movimiento[2])
                        xf = int(movimiento[4])
                        yf = int(movimiento[6])
                        valido = validar(xi,yi,xf,yf)

                    # VALIDAR GALLINAS Y Moverla

                        if tablero[yi*2][xi*2] != "G":
                            valido = False
                        if tablero[yf*2][xf*2] != "N":
                            valido = False

                    if valido:
                        MovimientoGallina(xi,yi,xf,yf)
                        guardado += ["G," + movimiento]
                    else:
                        movimiento = str(input("Movimiento invalido, intentalo otra vez: "))

            # Encontrar coyote
            for linea in tablero:
                if "C" in linea:
                    x_coyote = linea.index("C")
                    if x_coyote != 0:
                        x_coyote /= 2
                        x_coyote = int(x_coyote)
                    y_coyote = tablero.index(linea)
                    if y_coyote != 0:
                        y_coyote /= 2
                        y_coyote = int(y_coyote)
            posicion_coyote = (x_coyote,y_coyote)

            # REvisar si se puede mover el coyote
            perdio_coyote = True
            for x in range(x_coyote - 1, x_coyote + 2):
                for y in range(y_coyote -1, y_coyote + 2):
                    if (x,y) != posicion_coyote:
                        valido = validar(x_coyote,y_coyote,x,y)
                        if valido:
                            if tablero[y*2][x*2] == "N":
                                perdio_coyote = False
            if perdio_coyote:
                for x in range(x_coyote - 2, x_coyote + 3):
                    for y in range(y_coyote -2, y_coyote + 3):
                            if (x,y) != posicion_coyote:
                                x2 = ((x - x_coyote)/2) + x_coyote
                                y2 = ((y - y_coyote)/2) + y_coyote
                                valido = validar(x_coyote,y_coyote,x2,y2)
                                if valido:
                                    valido = validar(x2,y2,x,y)
                                    if valido:
                                        if tablero[y*2][x*2] == "N":
                                            perdio_coyote = False
            if perdio_coyote:
                for linea in tablero:
                        str1 = "".join(linea)
                        print(str1)
                print("El juego termino!")
                print("Ganaron las gallinas!")
                print("¿Deseas guardar la partida ? (G)")
                print("Salir del juego (S)")
                respuesta = str(input("¿O quieres empezar de nuevo? (E)"))
                while (respuesta != "S") and (respuesta != "s") and (respuesta != "G") and (respuesta != "g") and (respuesta != "E") and (respuesta != "e"):
                    respuesta = str(input("Por favor, responde con alguna de las opciones dadas: "))
                ganador = True
            if (perdio_coyote == False) and (gallina_perdio == False) and (salir == False):
                movimiento = turno(coyote)
                if movimiento == "S" or movimiento == "s" or movimiento == "g" or movimiento == "G":
                    salir = True
                    perdedor = True
                    respuesta = "S"
                saltar == False
                comio = False
                if (len(movimiento) != 1) and (salir == False):
                    valido = False
                    while valido == False:
                        xi = int(movimiento[0])
                        yi = int(movimiento[2])
                        xf = int(movimiento[4])
                        yf = int(movimiento[6])
                        if ((abs(xi - xf)) == 2) or ((abs(yi - yf)) == 2):
                            x2 = int(((xf - xi)/2 ) + xi)
                            y2 = int(((yf - yi)/2) + yi )
                            valide = validar(xi,yi,x2,y2)
                            if valide:
                                if tablero[y2*2][x2*2] == "G":
                                    valide = validar(x2,y2,xf,yf)
                                    if valide:
                                        if tablero[yf*2][xf*2] == "N":
                                            valido = True
                                            tablero[yi*2][xi*2] = "N"
                                            tablero[y2*2][x2*2] = "N"
                                            tablero[yf*2][xf*2] = "C"
                                            comio = True
                                            guardado += ["C," + movimiento]
                        else:
                            valide = validar(xi,yi,xf,yf)
                            if valide:
                                if tablero[yf*2][xf*2] == "N":
                                    valido = True
                                    tablero[yf*2][xf*2] = "C"
                                    tablero[yi*2][xi*2] = "N"
                                    guardado += ["C," + movimiento]
                        if valido == False :
                            movimiento = str(input("Movimiento invalido, intentalo otra vez: "))
            # Ver si se puede comer mas gallinas
            for linea in tablero:
                if "C" in linea:
                    x_coyote = linea.index("C")
                    if x_coyote != 0:
                        x_coyote /= 2
                        x_coyote = int(x_coyote)
                    y_coyote = tablero.index(linea)
                    if y_coyote != 0:
                        y_coyote /= 2
                        y_coyote = int(y_coyote)
            posicion_coyote = (x_coyote,y_coyote)
            puede = Puede_mas()
            while puede and comio and (salir == False):
                movimiento = str(input(coyote, "tienes la posibilidad de comer otra gallina, ingresa las coordenadas para hacerlo: "))
                valido = False
                while valido == False:    
                    if (abs(xi - xf) > 1) or (abs(yi - yf) > 1):
                        x2 = (xf - xi)/2 + xi
                        y2 = (yf - yi)/2 + yi
                        validar = validar(xi,yi,x2,y2)
                        if validar:
                            if tablero[y2*2][x2*2] == "G":
                                validar = validar(x2,y2,xf,yf)
                                if validar:
                                    if tablero[yf*2][xf*2] == "N":
                                        valido = True
                                        tablero[yi*2][xi*2] = "N"
                                        tablero[y2*2][x2*2] = "N"
                                        tablero[yf*2][xf*2] = "C"
                puede = Puede_mas()
                for linea in tablero:
                    if "C" in linea:
                        x_coyote = linea.index("C")
                        if x_coyote != 0:
                            x_coyote /= 2
                            x_coyote = int(x_coyote)
                        y_coyote = tablero.index(linea)
                        if y_coyote != 0:
                            y_coyote /= 2
                            y_coyote = int(y_coyote)
                posicion_coyote = (x_coyote,y_coyote)
            perdedor = False
            if gallina_perdio or perdio_coyote:
                perdedor = True
    if respuesta == "S" or respuesta == "s":
        salir = True
        perdedor = True
        sys.exit()
    if not salir:
        if respuesta == "E" or respuesta == "e":
               perdedor = False
        if respuesta == "G" or respuesta == "g":
            file = str(input("¿Que nombre quieres darle al archivo?: "))
            file = open(file, 'w')
            for linea in guardado:
                file.write(linea + '\n')
                file.close()
            salir = True
            sys.exit()