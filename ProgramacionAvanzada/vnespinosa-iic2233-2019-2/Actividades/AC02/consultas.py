"""
Aquí debes completar las funciones de las consultas
"""


def resumen_actual(ayudantes, alumnos):
    pisos = ayudantes[0]
    print(f"Alumnos restantes: {len(alumnos[0])}")
    cantidad = len(pisos['Piso -1']) + len(pisos['Piso -2']) + len(pisos['Piso -3']) + len(pisos['Piso -4'])
    print(f"Ayudantes restantes: {cantidad}")
    print(f"Ayudantes Piso -1: {len(pisos['Piso -1'])}")
    print(f"Ayudantes Piso -2: {len(pisos['Piso -2'])}")
    print(f"Ayudantes Piso -3: {len(pisos['Piso -3'])}")
    print(f"Ayudantes Piso -4: {len(pisos['Piso -4'])}")

def stock_comida(alumnos):
    comida_contada = dict()
    comidas = alumnos[1]
    for alumno in alumnos[0]:
        if comidas[alumno] in comida_contada:
            comida_contada[comidas[alumno]] = comida_contada[comidas[alumno]] + 1
        else:
            comida_contada[comidas[alumno]] = 1
    elemento = []
    for comida in comida_contada:
        elemento.append((comida, comida_contada[comida]))
    return(elemento)
