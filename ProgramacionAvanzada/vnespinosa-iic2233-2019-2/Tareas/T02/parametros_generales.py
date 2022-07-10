import os
import random
path_logo = os.path.join("sprites", "otros", "logo")
path_fondo = os.path.join("sprites", "otros", "window_template")
path_casa = os.path.join("sprites", "mapa", "house")
path_tienda = os.path.join("sprites", "mapa", "store")
path_inventario = os.path.join("sprites", "otros", "invetary_template") #Esta mal escrtio inventary
path_hacha = os.path.join("sprites", "otros", "axe")
path_azada = os.path.join("sprites", "otros", "hoe")
path_alcachofa = os.path.join("sprites", "recursos", "artichoke")
path_choclo = os.path.join("sprites", "recursos", "corn")
path_oro = os.path.join("sprites", "recursos", "gold")
path_madera = os.path.join("sprites", "recursos", "wood")
path_arbol = os.path.join("sprites", "otros", "tree")
path_semillas_alcachofa = os.path.join("sprites", "cultivos", "alcachofa", "seeds")
path_semillas_choclo = os.path.join("sprites", "cultivos", "choclo", "seeds")
path_ticket = os.path.join("sprites", "otros", "ticket")
path_logo_inventario = os.path.join("sprites", "otros", "inventary")
path_inicial_alcachofa = os.path.join("sprites", "cultivos", "alcachofa", "stage_1")
path_inicial_choclo = os.path.join("sprites", "cultivos", "choclo", "stage_1")
VEL_MOVIMIENTO = 1 #En pixeles
ENERGIA_JUGADOR = 100
ENERGIA_DORMIR = 80
MONEDAS_INICIALES = 150
DURACION_DIAS = 50 #En segundos
DINERO_TRAMPA = 500
PROB_ARBOL = 1  #0.7
PROB_ORO = 1 #0.6
DURACION_LENA = 30
DURACION_ORO = 30
ENERGIA_SEMBRAR = 5

N = 32 #tamaño celdas
largo_inventario = 75
margen = 17 #Para que se vea el borde del tablero

celdas_mapa = {
    "libre": "sprites/mapa/tile000",
    "libre2": "sprites/mapa/tile001",
    "libre3": "sprites/mapa/tile002",
    "libre4": "sprites/mapa/tile006",
    "cultivable": "sprites/mapa/tile020",
    "cultivable_listo": "sprites/mapa/tile044",
    "ibre_arriba": "sprites/mapa/tile035",
    "libre_arriba_derecha": "sprites/mapa/tile039",
    "libre_arriba_izquierda": "sprites/mapa/tile036",
    "libre_izquierda": "sprites/mapa/tile042",
    "libre_derecha": "sprites/mapa/tile045",
    "libre_abajo": "sprites/mapa/tile047",
    "libre_abajo_izquierda": "sprites/mapa/tile048",
    "libre_abajo_derecha": "sprites/mapa/tile051",
    "roca": "sprites/otros/stone"
    }

usuario = {
    "down_1": "sprites/personaje/down_1",
    "down_2": "sprites/personaje/down_2",
    "down_3": "sprites/personaje/down_3",
    "down_4": "sprites/personaje/down_4",
    "left_1": "sprites/personaje/left_1",
    "left_2": "sprites/personaje/left_2",
    "left_3": "sprites/personaje/left_3",
    "left_4": "sprites/personaje/left_4",
    "right_1": "sprites/personaje/right_1",
    "right_2": "sprites/personaje/right_2",
    "right_3": "sprites/personaje/right_3",
    "right_4": "sprites/personaje/right_4",
    "up_1": "sprites/personaje/up_1",
    "up_2": "sprites/personaje/up_2",
    "up_3": "sprites/personaje/up_3",
    "up_4": "sprites/personaje/up_4",
    }


PATH_CAMA = os.path.join("sprites_casa", "cama")
PATH_PISO = os.path.join("sprites_casa", "piso_madera")
PATH_PUERTA = os.path.join("sprites_casa", "puerta")
PATH_PARED = os.path.join("sprites_casa", "pared")
