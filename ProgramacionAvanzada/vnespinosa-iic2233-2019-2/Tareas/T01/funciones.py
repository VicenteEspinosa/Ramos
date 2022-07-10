import parametros as p
import Clases as c

def Velocidad_Recomendada(Vehiculo, Pista, Piloto):
    if Vehiculo.categoria == "motocicleta" or Vehiculo.categoria == "automóvil":
        velocidad_base = Vehiculo.motor

    else:
        velocidad_base = Vehiculo.zapatillas
    a = int(velocidad_base) + (Vehiculo.traccion - Pista.hielo) * p.POND_EFECT_HIELO
    a += (Vehiculo.chasis - int(Pista.rocas)) * p.POND_EfECT_ROCAS
    a += (Piloto.experiencia - Pista.Dificultad) * p.POND_EFECT_DIFICULTAD
    return a

def Velocidad_Intencional(Velocidad_Recomendada, personalidad):
    if personalidad == "osado":
        return p.EFECTO_OSADO * Velocidad_Recomendada
    else:
        return p.EFECTO_PRECAVIDO * Velocidad_Recomendada

def Velocidad_Real(Vehiculo, Pista, Piloto):
    Velocidad_Rec = Velocidad_Recomendada(Vehiculo, Pista, Piloto)
    Velocidad_Int = Velocidad_Intencional(Velocidad_Rec, Piloto.personalidad)
    a = Velocidad_Int
    a += Dificultad_Control(Piloto.equilibrio, Vehiculo.peso, Piloto.personalidad, Vehiculo.ruedas)
    a += Hipotermia(Pista.Vuelta, Piloto.contextura, Pista.hielo)
    return max(p.VELOCIDAD_MINIMA, a)




def Dificultad_Control(equilibrio, peso_vehiculo, personalidad, ruedas):
    if ruedas == 4:
        return 0
    if personalidad == "osado":
        return min(0, int(equilibrio) - int(p.PESO_MEDIO / int(peso_vehiculo)))
    else:
        return min(0, int(equilibrio) * int(p.EQUILIBRIO_PRECAVIDO) - int(p.PESO_MEDIO / peso_vehiculo))

def Hipotermia(vuelta, contextura, hielo):
    return min(0, int(vuelta) * (int(contextura) - int(hielo)))

#Sucesos durante carroceria

def Golpe_Recibido_por_vuelta(rocas, defensa):
    return max(0, rocas - defensa)

def Tiempo_Pits(Vehiculo):
    return p.TIEMPO_MINIMO_PITS + (Vehiculo.chasis_maximo - Vehiculo.chasis) * p.VELOCIDAD_PITS

def Dinero_Por_Vuelta(Pista):
    return Pista.Vuelta * Pista.Dificultad

def Probabilidad_accidente(Vehiculo, Pista, Piloto):
    v_real = Velocidad_Real(Vehiculo, Pista, Piloto)
    v_recomendada = Velocidad_Recomendada(Vehiculo, Pista, Piloto)
    a = max(0, (v_real - v_recomendada) / v_recomendada)
    a += (Vehiculo.chasis_maximo - Vehiculo.chasis) / Vehiculo.chasis_maximo
    return min(1, a)

def Tiempo_Vuelta(Vehiculo, Pista, Piloto):
    return Pista.largo / Velocidad_Real(Vehiculo, Pista, Piloto)

# Ganador de la carroceria

def Dinero_Ganador(Pista):
    return Pista.Vueltas * (Pista.Dificultad + Pista.hielo + Pista.rocas)

def Ventaja_ultimo_lugar(tiempo_ultimo, tiempo_primero):
    return tiempo_ultimo - tiempo_primero

def Experiencia_ganador(tiempo_ultimo, tiempo_primero, Pista, Piloto):
    if Piloto.personalidad == "precavido":
        Bonificacion = p.BONIFICACION_PRECAVIDO
    else:
        Bonificacion = p.BONIFICACION_OSADO
    return (Ventaja_ultimo_lugar(tiempo_ultimo, tiempo_primero) + Pista.Dificultad) * Bonificacion

def Cargar_Contrincantes():
    contador = 1
    todos_los_contrincantes = []
    with open(p.PATHS["CONTRINCANTES"], encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", "")
            if contador == 1:
                header = line.split(",")
                n_nombre = header.index("Nombre")
                n_nivel = header.index("Nivel")
                n_personalidad = header.index("Personalidad")
                n_contextura = header.index("Contextura")
                n_equilibrio = header.index("Equilibrio")
                n_experiencia = header.index("Experiencia")
                n_equipo = header.index("Equipo")
                n_experiencia = header.index("Experiencia")
            else:
                line = line.split(",")
                nombre = line[n_nombre]
                nivel = line[n_nivel]
                personalidad = line[n_personalidad]
                contextura = line[n_contextura]
                equilibrio = line[n_equilibrio]
                experiencia = line[n_experiencia]
                equipo = line[n_equipo]
                experiencia = line[n_experiencia]
                todos_los_contrincantes.append(c.Contrincante(nombre, personalidad, contextura, equilibrio, equipo, experiencia, nivel))

            contador += 1
    return todos_los_contrincantes



def Cargar_Pistas():
    contador = 0
    pistas = []
    with open(p.PATHS["PISTAS"], encoding="utf-8") as archivo: #Cargar
        for line in archivo:
            line = line.replace("\n", "")
            line = line.split(",")
            if contador == 0:
                header = line
                n_nombre = header.index("Nombre")
                n_tipo = header.index("Tipo")
                n_hielo = header.index("Hielo")
                n_rocas = header.index("Rocas")
                n_dificultad = header.index("Dificultad")
                n_vueltas = header.index("NúmeroVueltas")
                n_contrincantes = header.index("Contrincantes")
                n_largo = header.index("LargoPista")

            else:
                Nombre = line[n_nombre]
                Tipo = line[n_tipo]
                Hielo = line[n_hielo]
                Rocas = line[n_rocas]
                Dificultad = line[n_dificultad]
                Vueltas = line[n_vueltas]
                Vuelta = 0
                Contrincantes = line[n_contrincantes].split(";") #Hay que buscar el contrincante que corresponda con el nombre
                Largo = line[n_largo]
                pistas.append(c.Pista(Nombre, Tipo, Hielo, Rocas, Dificultad, Vueltas, Vuelta, Contrincantes, Largo))

            contador += 1
    return pistas


def Cargar_Contrincantes_Pista(pista, Contrincantes_totales):
    Contrincantes = []
    for contrincante in Contrincantes_totales:
        if contrincante.nombre in pista.Contrincantes:
            Contrincantes.append(contrincante)
    return Contrincantes
