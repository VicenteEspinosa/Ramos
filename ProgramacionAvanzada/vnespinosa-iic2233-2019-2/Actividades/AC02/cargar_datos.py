"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""

from collections import deque, defaultdict

"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    # Usar cola
    #quizas diccionario para la cocina
    alumnos = deque()
    comidas = dict()
    with open(ruta_archivo_alumnos, encoding="utf-8") as file:
        for alumno in file:
            alumno.replace("/n", "")
            elementos = alumno.split(";")
            alumnos.append(elementos[0])
            for comida in elementos[1].split(","):
                comidas[elementos[0]] = comida[:len(comida) - 1]
    return alumnos, comidas




def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    # Usar Stack
    piso1 = [] #Stack
    piso2 = []
    piso3 = []
    piso4 = []
    pisos = dict()
    debilidades = dict()
    with open(ruta_archivo_ayudantes, encoding= "utf-8") as file:
        for ayudante in file:
            ayudante.replace("/n", "")
            elementos = ayudante.split(";")
            nombre = elementos[0]
            piso = DICT_PISOS[elementos[1]]
            debilidad = elementos[2]
            if piso == 'Piso -1':
                piso1.append(nombre)
            elif piso == 'Piso -2':
                piso2.append(nombre)
            elif piso == 'Piso -3':
                piso3.append(nombre)
            elif piso == 'Piso -4':
                piso4.append(nombre)
            debilidades[nombre] = debilidad
    pisos["Piso -1"] = piso1
    pisos["Piso -2"] = piso2
    pisos["Piso -3"] = piso3
    pisos["Piso -4"] = piso4

    return pisos, debilidades
