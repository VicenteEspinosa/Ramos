import parametros as p
import random

class Corredor:
    def __init__(self, nombre, personalidad, contextura, equilibrio, experiencia, equipo):
        self.nombre = nombre
        self.personalidad = personalidad
        self.contextura = contextura
        self.equilibrio = equilibrio
        self.equipo = equipo
        self.experiencia = int(experiencia)
        self.vehiculo_actual = None
        self.vehiculos = []

    def Recibir_golpe(self, golpe):
        vivo = self.vehiculo_actual.Recibir_golpe(golpe)


class Competidor(Corredor):
    def __init__(self, nombre, personalidad, contextura, equilibrio, equipo, experiencia, dinero):
        Corredor.__init__(self, nombre, personalidad, contextura, equilibrio, experiencia, equipo)
        self.dinero = dinero

    def Gastar_Dinero(self, cantidad):
        if int(cantidad) > self.dinero:
            return False
        else:
            self.dinero -= int(cantidad)
            return True

    def Ganar_Dinero(self, cantidad):
        self.dinero += int(cantidad)

    def Ganar_Experiencia(self, cantidad):
        self.experiencia += int(cantidad)


class Contrincante(Corredor):
    def __init__(self, nombre, personalidad, contextura, equilibrio, equipo, experiencia, nivel):
        Corredor.__init__(self, nombre, personalidad, contextura, equilibrio, experiencia, equipo)
        self.nivel = nivel



class Vehiculo:
    def __init__(self):
        self.nombre = None
        self.propietario = None
        self.categoria = None
        self.motor = None
        self.ruedas = None
        self.chasis = None
        self.carroceria = None
        self.peso = None
        self.zapatillas = None
        self.chasis_maximo = None
        self.traccion = None

    def Cargar(self, nombre, propietario, categoria, chasis, carroceria, ruedas, motor_zapa, peso):
        self.nombre = nombre
        self.propietario = propietario
        self.categoria = categoria
        self.chasis = int(chasis)
        self.carroceria = int(carroceria)
        self.traccion = int(ruedas)
        self.peso = int(peso)
        if categoria == "bicicleta" or "troncomóvil":
            self.zapatillas = int(motor_zapa)
        else:
            self.motor = int(motor_zapa)

        if categoria == "bicicleta" or "motocicleta":
            self.ruedas = 2
        else:
            self.ruedas = 4

    def Recibir_golpe(self, golpe):
        if int(golpe) >= self.chasis:
            self.chasis = 0
            print("Tu chasis ha sido destruido!!")
            return False
        else:
            self.chasis -= int(golpe)
            return True

    def Reparar_Chasis(self):
        self.chasis = int(str(self.chasis_maximo))

    def Mejorar(self, parte):
        if parte == "chasis":
            self.chasis_maximo += p.MEJORAS["CHASIS"]["EFECTO"]
            self.chasis += self.chasis_maximo - self.chasis
        elif parte == "carroceria":
            self.chasis += p.MEJORAS["CARROCERIA"]["EFECTO"]
        elif parte == "ruedas":
            self.ruedas += p.MEJORAS["RUEDAS"]["EFECTO"]
        elif parte == "motor":
            self.motor += p.MEJORAS["MOTOR"]["EFECTO"]
        elif parte == "zapatillas":
            self.zapatillas += p.MEJORAS["ZAPATILLAS"]["EFECTO"]


def Generar_Vehiculo(propietario, categoria):
    print("Debes darle un nombre a tu vehiculo")
    print("¿Que nombre quieres ponerle?")
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
    if categoria == "automóvil":
        auto = Automovil()
        auto.propietario = propietario
        auto.nombre = nombre
    elif categoria == "motocicleta":
        auto = Motocicleta()
        auto.propietario = propietario
        auto.nombre = nombre
    elif categoria == "troncomóvil":
        auto = Troncomovil()
        auto.propietario = propietario
        auto.nombre = nombre
    elif categoria == "bicicleta":
        auto = Bicicleta()
        auto.propietario = propietario
        auto.nombre = nombre
    propietario.vehiculos.append(auto)
    return auto


class Automovil(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self)
        self.categoria = "automóvil"
        self.motor = random.randint(p.AUTOMOVIL["MOTOR"]["MIN"], p.AUTOMOVIL["MOTOR"]["MAX"])
        self.ruedas = 4
        self.chasis = random.randint(p.AUTOMOVIL["CHASIS"]["MIN"], p.AUTOMOVIL["CHASIS"]["MAX"])
        self.carroceria = random.randint(p.AUTOMOVIL["CARROCERIA"]["MIN"], p.AUTOMOVIL["CARROCERIA"]["MAX"])
        self.peso = random.randint(p.AUTOMOVIL["PESO"]["MIN"], p.AUTOMOVIL["PESO"]["MAX"])
        self.zapatillas = None
        self.chasis_maximo = int(str(self.chasis))
        self.traccion = random.randint(p.AUTOMOVIL["RUEDAS"]["MIN"], p.AUTOMOVIL["RUEDAS"]["MAX"])


class Motocicleta(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self)
        self.categoria = "motocicleta"
        self.motor = random.randint(p.MOTOCICLETA["MOTOR"]["MIN"], p.MOTOCICLETA["MOTOR"]["MAX"])
        self.ruedas = 2
        self.chasis = random.randint(p.MOTOCICLETA["CHASIS"]["MIN"], p.MOTOCICLETA["CHASIS"]["MAX"])
        self.carroceria = random.randint(p.MOTOCICLETA["CARROCERIA"]["MIN"], p.MOTOCICLETA["CARROCERIA"]["MAX"])
        self.peso = random.randint(p.MOTOCICLETA["PESO"]["MIN"], p.MOTOCICLETA["PESO"]["MAX"])
        self.zapatillas = None
        self.chasis_maximo = int(str(self.chasis))
        self.traccion = random.randint(p.MOTOCICLETA["RUEDAS"]["MIN"], p.MOTOCICLETA["RUEDAS"]["MAX"])


class Troncomovil(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self)
        self.categoria = "troncomóvil"
        self.motor = None
        self.ruedas = 4
        self.chasis = random.randint(p.TRONCOMOVIL["CHASIS"]["MIN"], p.TRONCOMOVIL["CHASIS"]["MAX"])
        self.carroceria = random.randint(p.TRONCOMOVIL["CARROCERIA"]["MIN"], p.TRONCOMOVIL["CARROCERIA"]["MAX"])
        self.peso = random.randint(p.TRONCOMOVIL["PESO"]["MIN"], p.TRONCOMOVIL["PESO"]["MAX"])
        self.zapatillas = random.randint(p.TRONCOMOVIL["ZAPATILLAS"]["MIN"], p.TRONCOMOVIL["ZAPATILLAS"]["MAX"])
        self.chasis_maximo = int(str(self.chasis))
        self.traccion = random.randint(p.TRONCOMOVIL["RUEDAS"]["MIN"], p.TRONCOMOVIL["RUEDAS"]["MAX"])


class Bicicleta(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self)
        self.categoria = "bicicleta"
        self.motor = None
        self.ruedas = 2
        self.chasis = random.randint(p.BICICLETA["CHASIS"]["MIN"], p.BICICLETA["CHASIS"]["MAX"])
        self.carroceria = random.randint(p.BICICLETA["CARROCERIA"]["MIN"], p.BICICLETA["CARROCERIA"]["MAX"])
        self.peso = random.randint(p.BICICLETA["PESO"]["MIN"], p.BICICLETA["PESO"]["MAX"])
        self.zapatillas = random.randint(p.BICICLETA["ZAPATILLAS"]["MIN"], p.BICICLETA["ZAPATILLAS"]["MAX"])
        self.chasis_maximo = int(str(self.chasis))
        self.traccion = random.randint(p.BICICLETA["RUEDAS"]["MIN"], p.BICICLETA["RUEDAS"]["MAX"])


class Pista():
    def __init__(self, Nombre, Tipo, Hielo, Rocas, Dificultad, Vueltas, Vuelta, Contrincantes, Largo):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.hielo = int(Hielo)
        self.rocas = int(Rocas)
        self.Dificultad = int(Dificultad)
        self.Vueltas = int(Vueltas)
        self.Vuelta = int(Vuelta)
        self.Contrincantes = Contrincantes
        self.Largo = int(Largo)
        if self.Tipo == "pista hielo":
            self.Rocas = 0
        elif self.Tipo == "pista rocosa":
            self.Hielo = 0
