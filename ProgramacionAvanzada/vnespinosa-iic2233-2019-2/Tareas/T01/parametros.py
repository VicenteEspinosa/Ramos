# Valores máximos y mínimos de las partes y el peso de los vehículos
import random #Es para la personalidad de los hibridos

def funcion():
    a = random.randint(1,2)
    if a == 1:
        return "osado"
    else:
        return "precavido"


AUTOMOVIL = {
    'CHASIS': {
        'MIN': 23,
        'MAX': 35
    },
    'CARROCERIA': {
        'MIN': 19,
        'MAX': 32
    },
    'RUEDAS': {
        'MIN': 19,
        'MAX': 36
    },
    'MOTOR': {
        'MIN': 46,
        'MAX': 60
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': 20,
        'MAX': 33
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 26,
        'MAX': 34
    },
    'CARROCERIA': {
        'MIN': 23,
        'MAX': 40
    },
    'RUEDAS': {
        'MIN': 12,
        'MAX': 19
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': 32,
        'MAX': 48
    },
    'PESO': {
        'MIN': 36,
        'MAX': 55
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 15,
        'MAX': 23
    },
    'CARROCERIA': {
        'MIN': 18,
        'MAX': 27
    },
    'RUEDAS': {
        'MIN': 17,
        'MAX': 23
    },
    'MOTOR': {
        'MIN': 40,
        'MAX': 59
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': 28,
        'MAX': 40
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 12,
        'MAX': 18
    },
    'CARROCERIA': {
        'MIN': 15,
        'MAX': 21
    },
    'RUEDAS': {
        'MIN': 20,
        'MAX': 28
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': 26,
        'MAX': 37
    },
    'PESO': {
        'MIN': 18,
        'MAX': 30
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 100,
        'EFECTO': 15
    },
    'CARROCERIA': {
        'COSTO': 50,
        'EFECTO': 12
    },
    'RUEDAS': {
        'COSTO': 120,
        'EFECTO': 8
    },
    'MOTOR': {
        'COSTO': 270,
        'EFECTO': 9
    },
    'ZAPATILLAS': {
        'COSTO': 270,
        'EFECTO':10
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': "precavido"
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': funcion()
         #50/50 para precavido u osado
         #funcion() definida al principio
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': "osado"
    }
}


# Las constantes de las formulas

#Velocidad recomendada
POND_EFECT_HIELO = 0.6
POND_EfECT_ROCAS = 0.8
POND_EFECT_DIFICULTAD = 0.1

# Velocidad real
VELOCIDAD_MINIMA = 1

# Velocidad intencional
EFECTO_OSADO = 1.5
EFECTO_PRECAVIDO = 0.9

# Dificultad de control del vehículo
PESO_MEDIO = 30
EQUILIBRIO_PRECAVIDO = 1.5

# Tiempo pits
TIEMPO_MINIMO_PITS = 10
VELOCIDAD_PITS = 1.6

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 1.1
BONIFICACION_OSADO = 1.4


# Paths de los archivos

PATHS = {
    'PISTAS': "pistas.csv",
    'CONTRINCANTES': "contrincantes.csv",
    'PILOTOS': "pilotos.csv",
    'VEHICULOS': "vehículos.csv",
}


# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
