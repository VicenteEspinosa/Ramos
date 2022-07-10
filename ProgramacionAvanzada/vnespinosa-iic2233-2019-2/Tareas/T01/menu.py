import Clases as c
import parametros as p
import random
import funciones as f

class Menu:
    def __init__(self):
        self.opcion = None
        self.Competidor = None
    def recibir_input(self, minimo, maximo):
        malo = True
        while malo:
            entrada = str(input("- "))
            if entrada.isdigit():
                if float(entrada).is_integer():
                    if minimo <= int(entrada) <= maximo:
                        malo = False
            if malo:
                print("Input incorrecto, intentalo otra vez.")
        self.opcion = int(entrada)


    def Guardar(self, usuarios):
        header = ""
        lista = []
        with open(p.PATHS["PILOTOS"], encoding="utf-8") as archivo:
            contador = 1
            for line in archivo:
                line = line.replace("\n", "")
                if contador == 1:
                    header = line.split(",")
                    n_nombre = header.index("Nombre")
                    n_dinero = header.index("Dinero")
                    n_personalidad = header.index("Personalidad")
                    n_contextura = header.index("Contextura")
                    n_equilibrio = header.index("Equilibrio")
                    n_experiencia = header.index("Experiencia")
                    n_equipo = header.index("Equipo")
                    lista = [n_nombre, n_dinero, n_personalidad, n_contextura, n_equilibrio, n_experiencia, n_equipo]
                contador += 1
        with open(p.PATHS["PILOTOS"], "w", encoding="utf-8") as file:
            prim = ""
            for elemento in header:
                prim += str(elemento)
                prim += ","
            file.write(prim + "\n")
            lista.sort()
            for usuario in usuarios:
                contador = 1
                line = ""
                for element in lista:
                    if contador != 1:
                        line += ","
                    if element == n_dinero:
                        line += str(usuario.dinero)
                    elif element == n_nombre:
                        line += str(usuario.nombre)
                    elif element == n_personalidad:
                        line += str(usuario.personalidad)
                    elif element == n_personalidad:
                        line += str(usuario.contextura)
                    elif element == n_equilibrio:
                        line += str(usuario.equilibrio)
                    elif element == n_experiencia:
                        line += str(usuario.experiencia)
                    elif element == n_equipo:
                        line += str(usuario.equipo)
                    elif element == n_contextura:
                        line += str(usuario.contextura)
                    contador += 1
                file.write(line + "\n")
        self.Guardar_Autos()

    def Guardar_Autos(self):
        header = ""
        lista = []
        with open(p.PATHS["VEHICULOS"], encoding="utf-8") as archivo:
            contador = 1
            for line in archivo:
                line = line.replace("\n", "")
                if contador == 1:
                    header = line.split(",")
                    n_nombre = header.index("Nombre")
                    n_propietario = header.index("Dueño")
                    n_categoria = header.index("Categoría")
                    n_chasis = header.index("Chasis")
                    n_carroceria = header.index("Carrocería")
                    n_ruedas = header.index("Ruedas")
                    n_mot_zap = header.index("Motor o Zapatillas")
                    n_peso = header.index("Peso")
                    lista = [n_nombre, n_propietario, n_categoria, n_chasis, n_carroceria, n_ruedas, n_mot_zap, n_peso]
                contador += 1
        with open(p.PATHS["VEHICULOS"], "w", encoding="utf-8") as file:
            prim = ""
            cont = 1
            for elemento in header:
                if cont != 1:
                    prim += ","
                cont += 1
                prim += str(elemento)
            file.write(prim + "\n")
            lista.sort()
            for auto in self.autos:
                line = ""
                contador = 1
                for element in lista:
                    if contador != 1:
                        line += ","
                    if element == n_nombre:
                        line += str(auto.nombre)
                    elif element == n_propietario:
                        line += str(auto.propietario)
                    elif element == n_categoria:
                        line += str(auto.categoria)
                    elif element == n_chasis:
                        line += str(auto.chasis)
                    elif element == n_carroceria:
                        line += str(auto.carroceria)
                    elif element == n_ruedas:
                        line += str(auto.ruedas)
                    elif element == n_mot_zap:
                        if auto.categoria == "bicicleta" or auto.categoria == "troncomóvil":
                            line += str(auto.zapatillas)
                        else:
                            line += str(auto.motor)
                    elif element == n_peso:
                        line += str(auto.peso)
                    contador += 1
                file.write(line + "\n")

class MenuInicio(Menu):
    def __init__(self):
        Menu.__init__(self)
        usuarios = [] #Solo nombres
        print("Bienvenido a 'Initial P', por favor escoge una opcion: ")
        print("[1] Crear nueva partida")
        print("[2] Cargar una partida")
        print("[3] Cerrar el juego")
        contador = 1
        with open(p.PATHS["PILOTOS"], encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.replace("\n", "")
                if contador == 1:
                    posicion = linea.split(",").index("Nombre")
                    contador += 1
                else:
                    usuarios.append(linea.split(",")[posicion])
        self.usuarios_nombres = usuarios
        self.recibir_input()


    def recibir_input(self): #Es distinto por que llega hasta 3
        a = Menu()
        a.recibir_input(1, 3)
        self.opcion = int(str(a.opcion))
        self.Cargar_Usuarios()
        self.Hacer_accion()


    def Hacer_accion(self): #Primero se usa recibir_input
        if self.opcion == 1:
            self.Usuario = self.Nueva_partida()
            print("")
            vehiculo = random.choice(["automóvil", "motocicleta", "troncomóvil", "bicicleta"])
            print(f"Se te dara un vehiculo al azar para empezar: '{vehiculo}'")
            print("")
            c.Generar_Vehiculo(self.Usuario, vehiculo)
            #-------------
        elif self.opcion == 2:
            self.Usuario = self.Cargar_partida()
        elif self.opcion == 3:
            exit()


    def Nueva_partida(self):
        print("Por favor, ingrese un nombre de usuario")
        malo = True
        while malo:
            malo = False
            nombre = str(input("- "))
            for caracter in nombre:
                if (not caracter.isalnum() ) and (caracter != " "):
                    malo = True
            if malo:
                print("El nombre solo acepta caracteres alfanumericos o espacios.")
                print("Intentalo otra vez:")
            elif nombre in self.usuarios_nombres:
                print("Ese nombre ya esta en uso, pruea con otro distinto")
                malo = True
        print("Ahora debes escoger tu equipo")
        print("Hay 3 opciones:")
        print("[1] Tareos")
        print("[2] Híbridos")
        print("[3] Docencios")
        malo = True
        while malo:
            entrada = str(input("- "))
            if entrada.isdigit():
                if float(entrada).is_integer():
                    if 1 <= int(entrada) <= 3:
                        malo = False
            if malo:
                print("Input incorrecto, intentalo otra vez.")
        if int(entrada) == 1:
            equipo = "TAREOS"
        elif int(entrada) == 2:
            equipo = "HIBRIDOS"
        elif int(entrada) == 3:
            equipo = "DOCENCIOS"
        personalidad = p.EQUIPOS[equipo]["PERSONALIDAD"]
        contextura = random.randint(p.EQUIPOS[equipo]["CONTEXTURA"]["MIN"], p.EQUIPOS[equipo]["CONTEXTURA"]["MAX"])
        equilibrio = random.randint(p.EQUIPOS[equipo]["EQUILIBRIO"]["MIN"], p.EQUIPOS[equipo]["EQUILIBRIO"]["MAX"])
        Usuario = c.Competidor(nombre, personalidad, contextura, equilibrio, equipo, 0, 0)
        self.usuarios.append(Usuario)
        return Usuario

    def Cargar_Usuarios(self):
        with open(p.PATHS["PILOTOS"], encoding='utf-8') as archivo:
            contador = 1
            self.usuarios = []
            for line in archivo:
                line = line.replace("\n", "")
                if contador == 1:
                    header = line.split(",")
                    n_nombre = header.index("Nombre")
                    n_dinero = header.index("Dinero")
                    n_personalidad = header.index("Personalidad")
                    n_contextura = header.index("Contextura")
                    n_equilibrio = header.index("Equilibrio")
                    n_experiencia = header.index("Experiencia")
                    n_equipo = header.index("Equipo")
                else:
                    datos = line.split(",")
                    nombre = datos[n_nombre]
                    dinero = datos[n_dinero]
                    personalidad = datos[n_personalidad]
                    contextura = datos[n_contextura]
                    equilibrio = datos[n_equilibrio]
                    experiencia = datos[n_experiencia]
                    equipo = datos[n_equipo]
                    self.usuarios.append(c.Competidor(nombre, personalidad, contextura, equilibrio, equipo, experiencia, dinero))
                contador += 1


    def Cargar_partida(self):
        print("¿Que usuario desea cargar?")
        for opcion in self.usuarios_nombres:
            print("+ " + str(opcion))
        print(" ")
        nombre = str(input("- "))
        while nombre not in self.usuarios_nombres:
            print("Nombre incorrecto, por favor ingresa una de las opciones anteriores")
            nombre = str(input("- "))
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                self.Usuario = usuario
                return usuario


class MenuPrincipal(Menu):
    def __init__(self, Usuario, Pistas, Usuarios, Contrincantes):
        Menu.__init__(self)
        self.Usuario = Usuario
        self.Pistas = Pistas
        self.usuarios = Usuarios
        self.contrincantes = Contrincantes
        self.pista = random.choice(Pistas) #Por mientras, despues se selecciona
        self.Cargar_Autos()
        self.recibir_input()

    def Cargar_Autos(self):
        corredores = []
        corredores.append(self.Usuario)
        self.autos = []
        for contrincante in self.contrincantes:
            corredores.append(contrincante)
        autos_sin_guardar = []
        for auto in self.Usuario.vehiculos:
            autos_sin_guardar.append(auto)
        with open(p.PATHS["VEHICULOS"], encoding="utf-8") as file:
            contador = 1
            for line in file:
                line = line.replace("\n", "")
                if contador == 1:
                    header = line.split(",")
                    n_nombre = header.index("Nombre")
                    n_propietario = header.index("Dueño")
                    n_categoria = header.index("Categoría")
                    n_chasis = header.index("Chasis")
                    n_carroceria = header.index("Carrocería")
                    n_ruedas = header.index("Ruedas")
                    n_mot_zap = header.index("Motor o Zapatillas")
                    n_peso = header.index("Peso")
                else:
                    line = line.split(",")
                    nombre = line[n_nombre]
                    propietario = line[n_propietario]
                    categoria = line[n_categoria]
                    chasis = line[n_chasis]
                    carroceria = line[n_carroceria]
                    ruedas = line[n_ruedas]
                    motor_zapa = line[n_mot_zap]
                    peso = line[n_peso]
                    for auto1 in autos_sin_guardar:
                        if nombre == auto1.nombre:
                            autos_sin_guardar.remove(auto1)
                    for persona in corredores:
                        if str(persona.nombre) == str(propietario):
                            if categoria == "bicicleta":
                                auto = c.Bicicleta()
                            elif categoria == "troncomóvil":
                                auto = c.Troncomovil()
                            elif categoria == "motocicleta":
                                auto = c.Motocicleta()
                            else:
                                auto = c.Automovil()
                            auto.Cargar(nombre, propietario, categoria, chasis, carroceria, ruedas, motor_zapa, peso)
                            persona.vehiculos.append(auto)
                            persona.vehiculo_actual = random.choice(persona.vehiculos) #Para los contrincantes
                            self.autos.append(auto)
                contador += 1
        for auto2 in autos_sin_guardar:
            self.autos.append(auto2)


    def recibir_input(self):
        print(" ")
        print("Por favor escoge una de las siguientes opciones:")
        print("[0] Volver al menu de inicio (Cerrar sesión)")
        print("[1] Comprar nuevos vehículos")
        print("[2] Iniciar una carrera")
        print("[3] Guardar partida")
        print("[4] Salir del programa")
        print("")
        a = Menu()
        a.recibir_input(0,4)
        self.opcion = a.opcion
        self.Hacer_accion()
        return self.Usuario

    def Hacer_accion(self):
        if self.opcion == 0:
            a = MenuInicio()
            self.Usuario = a.Usuario
            self.usuarios = a.usuarios
            b = MenuPrincipal(self.Usuario, self.Pistas, self.usuarios, self.contrincantes)
            self.Usuario = b.Usuario
            self.Pistas = b.Pistas
            self.usuarios = b.usuarios
        if self.opcion == 1:
            a = MenuCompra(self.Usuario)
            self.Usuario = a.Usuario
            self.recibir_input()
        elif self.opcion == 2:
            a = Menu_Preparacion_Carrera(self.Usuario, self.Pistas)
            self.pista = a.pista
        elif self.opcion == 3:
            super().Guardar(self.usuarios)
            self.recibir_input()
        elif self.opcion == 4:
            exit()
        return self.Usuario


class MenuCompra(Menu):
    def __init__(self, Usuario):
        Menu.__init__(self)
        self.Usuario = Usuario
        self.Vehiculos = ["automóvil",  'motocicleta', 'troncomóvil', 'bicicleta']
        self.precios = [550, 370, 900, 1050]
        self.recibir_input()

    def recibir_input(self):
        print(" ")
        print(f"Dinero actual: ${self.Usuario.dinero}")
        print("Vehiculos disponibles para comprar:")
        print("")
        contador = 0
        poseidos = []
        for autos_poseidos in self.Usuario.vehiculos:
            poseidos.append(autos_poseidos.categoria)
        for auto in self.Vehiculos:
            if auto not in poseidos:
                contador += 1
                print(f"{contador})  {auto}     ${self.precios[self.Vehiculos.index(auto)]}")
        if contador == 0:
            print("Ya has comprado todos los vehiculos !!")
            print("No puedes comprar más!")
            self.opcion = 0
        else:
            print("")
            print("Ingrese el número del vehículo que desea comprar (ingrese 0 para regresar)")
            a = Menu()
            a.recibir_input(0, contador)
            self.opcion = a.opcion
            self.Hacer_accion()

        return self.Usuario

    def Hacer_accion(self): #Primero se usa recibir_input
        if self.opcion == 0:
            return self.Usuario

        elif (self.opcion == 1) and (self.Usuario.Gastar_Dinero(self.precios[0])): #Automovil
            self.Usuario.vehiculos.append(c.Generar_Vehiculo(self.Usuario, "automóvil"))
            self.recibir_input()
            return self.Usuario
        elif (self.opcion == 2) and (self.Usuario.Gastar_Dinero(self.precios[1])): #Motocicleta
            self.Usuario.vehiculos.append(c.Generar_Vehiculo(self.Usuario, "motocicleta"))
            self.recibir_input()
            return self.Usuario
        elif (self.opcion == 3) and (self.Usuario.Gastar_Dinero(self.precios[2])): #Troncomovil
            self.Usuario.vehiculos.append(c.Generar_Vehiculo(self.Usuario, "troncomóvil"))
            self.recibir_input()
            return self.Usuario
        elif (self.opcion == 4) and (self.Usuario.Gastar_Dinero(self.precios[3])): #Bicicleta
            self.Usuario.vehiculos.append(c.Generar_Vehiculo(self.Usuario, "bicicleta"))
            self.recibir_input()
            return self.Usuario
        print("")
        print("No tienes suficiente dinero para ese vehiculo :(")
        print("")
        self.recibir_input()

class Menu_Preparacion_Carrera(Menu):
    def __init__(self, Usuario, Pistas):
        Menu.__init__(self)
        self.Usuario = Usuario
        self.pistas = Pistas
        self.pista = None
        self.recibir_input()

    def recibir_input(self):
        print("")
        print("Selecciona que pista deseas jugar:")
        print("")
        contador = 1
        for pista in self.pistas:
            print(f"{contador}) {pista.Nombre}")
            contador += 1
        a = Menu()
        a.recibir_input(1, contador - 1)
        self.opcion = a.opcion
        self.pista = self.pistas[self.opcion - 1]
        print("")
        print("Ahora debes escoger que vehiculo usaras en la carrera:")
        contador = 1
        for auto in self.Usuario.vehiculos:
            print(f"[{contador}] {auto.nombre}")
            contador += 1
        a.recibir_input(1, contador)
        self.opcion = a.opcion
        self.Usuario.vehiculo_actual = self.Usuario.vehiculos[self.opcion - 1]

class Menu_Carrera(Menu):
    def __init__(self, Usuario, Pista, Contrincantes):
        Menu.__init__(self)
        self.Usuario = Usuario
        self.Pista = Pista
        self.Pista.Vuelta = 0
        self.Contrincantes = Contrincantes
        self.salio = False
        self.dinero_ganador = f.Dinero_Ganador(self.Pista)
        self.Corredores = []
        self.Corredores.append(self.Usuario)
        self.descalificados = []
        for i in self.Contrincantes:
            self.Corredores.append(i)
        for j in self.Corredores:
            j.vehiculo_actual.Reparar_Chasis()
            j.tiempo_vuelta = 0
            j.tiempo_total = 0
        self.recibir_input()


    def Calcular_tiempos(self):
        tiempos = []
        for corredor in self.Corredores:
            if corredor not in self.descalificados:
                prob = f.Probabilidad_accidente(corredor.vehiculo_actual, self.Pista, corredor)
                if prob > random.random():
                    print(f"EL VEHICULO DE {corredor.nombre} HA EXPLOTADO!!")
                    print(f"{corredor.nombre} ha sido descalificado")
                    self.descalificados.append(corredor)
                tiempo = f.Velocidad_Real(corredor.vehiculo_actual, self.Pista, corredor)
            tiempo = round(tiempo, 2)
            if corredor not in self.descalificados:
                tiempos.append(tiempo)
            corredor.tiempo_vuelta = float(tiempo)
            corredor.tiempo_total += float(tiempo)
        if self.Usuario not in self.descalificados:
            tiempos.sort()
            tiempos = tiempos[::-1]
            contador = 1
            for tiempo in tiempos:
                for corredor in self.Corredores :
                    if (float(corredor.tiempo_vuelta) == float(tiempo)) and (corredor not in self.descalificados):
                        print(f"{contador}°  {corredor.nombre} con un tiempo de {corredor.tiempo_vuelta}")
                        contador += 1
            if float(tiempos[0]) == float(self.Usuario.tiempo_vuelta):
                print("")
                print("HAS GANADO LA VUELTA, FELICIDADES")
                print(f"Ganaste ${f.Dinero_Por_Vuelta(self.Pista)}")
                self.Usuario.Ganar_Dinero(f.Dinero_Por_Vuelta(self.Pista))
            if self.Pista.Vuelta == self.Pista.Vueltas -1:
                self.tiempos_totales = []
                for corredor in self.Corredores:
                    if corredor not in self.descalificados:
                        self.tiempos_totales.append(corredor.tiempo_total)

    def recibir_input(self):
        while (self.Pista.Vuelta < int(self.Pista.Vueltas))  and (self.salio == False):
            if self.Pista.Vuelta != 0 and (self.Usuario not in self.descalificados):
                self.dinero_vuelta = f.Dinero_Por_Vuelta(self.Pista)
                print("")
                print(f"Estas en la vuelta {self.Pista.Vuelta} de {self.Pista.Vueltas}")
                print("¿Deseas entrar a los pits?")
                print("[1] Si")
                print("[2] No")
                print("[3] Salir de la carrera")
                print("")
                a = Menu()
                a.recibir_input(1, 3)
                self.opcion = a.opcion
                self.Hacer_accion()
                self.Calcular_tiempos() #--------------------
            self.Pista.Vuelta += 1
            if self.Usuario in self.descalificados:
                print("")
                print("TU VEHICULO HA EXPLOTADO, NO PUEDES SEGUIR EN LA CARRERA")
                print("Ahora volverás al menu principal")
                print("")
                self.salio = True
        if self.salio == False:
            print("")
            print("La carrera ha terminado")
            self.tiempos_totales.sort()
            if self.Usuario.tiempo_total == self.tiempos_totales[0]:
                print("HAS GANADO LA CARRERA")
                print(f"Ganaste ${f.Dinero_Ganador(self.Pista)}")
                self.Usuario.Ganar_Dinero(f.Dinero_Ganador(self.Pista))


    def Hacer_accion(self):
        if self.opcion == 1:
            b = MenuPits(self.Usuario)
        elif self.opcion == 2:
            pass #No se hace nada, y sigue vuelta siguientes
        elif self.opcion == 3:
            self.salio = True #Volver al MenuInicio

class MenuPits(Menu):
    def __init__(self, Usuario):
        Menu.__init__(self)
        self.Usuario = Usuario
        self.recibir_input()

    def recibir_input(self):
        print(f"Dinero actual: ${self.Usuario.dinero}")
        print("Partes a mejorar:")
        print(f"1) Chasis        ${p.MEJORAS['CHASIS']['COSTO']}")
        print(f"2) Carroceria        ${p.MEJORAS['CARROCERIA']['COSTO']}")
        print(f"3) Ruedas        ${p.MEJORAS['RUEDAS']['COSTO']}")
        if (self.Usuario.vehiculo_actual.categoria == "automóvil") or (self.Usuario.vehiculo_actual.categoria == "motocicleta"):
            print(f"4) Motor        ${p.MEJORAS['MOTOR']['COSTO']}")
        else:
            print(f"4) zapatillas        ${p.MEJORAS['ZAPATILLAS']['COSTO']}")
        print("")
        print("Ingresa 0 para salir de los pits")

        a = Menu()
        a.recibir_input(0,4)
        self.opcion = a.opcion
        if self.Hacer_accion():
            self.recibir_input()


    def Hacer_accion(self):
        if (self.Usuario.vehiculo_actual.categoria == "automóvil") or (self.Usuario.vehiculo_actual.categoria == "motocicleta"):
            mot_zap = "MOTOR"
            mej = "motor"
        else:
            mot_zap = "ZAPATILLAS"
            mej = "zapatillas"
        if self.opcion == 0:
            return False #Volver a la carrera
        elif (self.opcion == 1) and (self.Usuario.Gastar_Dinero(p.MEJORAS["CHASIS"]["COSTO"])):
            self.Usuario.vehiculo_actual.Mejorar("chasis")
        elif (self.opcion == 2) and (self.Usuario.Gastar_Dinero(p.MEJORAS["CARROCERIA"]["COSTO"])):
            self.Usuario.vehiculo_actual.Mejorar("carroceria")
        elif (self.opcion == 3) and (self.Usuario.Gastar_Dinero(p.MEJORAS["RUEDAS"]["COSTO"])):
            self.Usuario.vehiculo_actual.Mejorar("ruedas")
        elif (self.opcion == 4) and (self.Usuario.Gastar_Dinero(p.MEJORAS[mot_zap]["COSTO"])):
            self.Usuario.vehiculo_actual.Mejorar(mej)
        else:
            print("")
            print("No tienes suficiente dinero para eso")
            print("")

        return True
