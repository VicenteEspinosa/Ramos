from tablero import print_tablero
from Funciones import Entre_3_15, inicio, turno, gen_tablero, Cargar_partida, Revelar_todo, Gano, Actualizar_Puntajes, Revisar_ceros
from parametros import POND_PUNT,PROB_LEGO
gano = False
turnos = 0

todo = inicio()
lista_visible = todo[0]
lista_solucion = todo[1]
lista_marcadas = todo[2]
columnas = todo[3][0]
filas = todo[3][1]
nombre = todo[4]
turnos = int(todo[5][0])
print(" ")
print("Este es tu tablero: ")
print(" ")
print_tablero(lista_marcadas)
todo = turno(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre,str(turnos))
lista_visible = todo[0]
lista_solucion = todo[1]
lista_marcadas = todo[2]
columnas = todo[3]
filas = todo[4]
nombre = todo[5]
perdio = todo[6]
lista_marcadas = Revisar_ceros(lista_visible,lista_marcadas,columnas,filas)
gano = Gano(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre)
while (not perdio) and (not gano):
    turnos += 1
    print_tablero(lista_marcadas)
    todo = turno(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre,str(turnos))
    lista_marcadas = todo[2]
    lista_marcadas = Revisar_ceros(lista_visible,lista_marcadas,columnas,filas)
    perdio = todo[6]
    gano = Gano(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre)
lego = float(int(columnas) * int(filas) * float(PROB_LEGO))
legos = 0
while lego > 0:
    legos += 1
    lego -= 1
descubiertas = 0
for col in lista_marcadas:
    for baldosa in col:
        if (not baldosa == " ") and (not baldosa == "L"):
            descubiertas += 1
puntaje = legos * descubiertas * POND_PUNT
if perdio:
    todo = Revelar_todo(lista_visible,lista_solucion,lista_marcadas,columnas,filas,nombre)
    lista_marcadas = todo[2]
    print_tablero(lista_marcadas)
    print("Tu puntaje final fue de " + str(puntaje))
if gano:
    print_tablero(lista_visible)
    print("GANASTE!!")
    print("Tu puntaje fue de " + str(puntaje))

Actualizar_Puntajes(puntaje,nombre)
print(" ")
str(input("Presiona 'Entrer' para salir"))
