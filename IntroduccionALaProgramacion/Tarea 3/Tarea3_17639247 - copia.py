class Simulacion:
	def __init__(self,objetos,equipos,pruebas,personaje):
		self.objetos = objetos
		self.equipos = equipos
		self.pruebas = pruebas
		self.personaje = personaje

	def empezar(self):
		print("Muy bien {}, te informo que posees:".format(usuario.nombre))
		print("{} puntos de Vida base".format(usuario.vida))
		print("{} puntos de Tiempo".format(usuario.tiempo))
		print("{} puntos para gastar en stats iniciales".format(usuario.puntos))
		print("¿Cómo quieres repartir tus {} puntos?".format(usuario.puntos))
		x = usuario.puntos + 1
		while x > usuario.puntos:
			x = 0
			v = int(input("Vida: "))
			x += v
			if x <= usuario.puntos:
				d = int(input("Destreza: "))
				x += d
			if x <= usuario.puntos:
				r = int(input("Resistencia: "))
				x += r
			if x <= usuario.puntos:
				i = int(input("Inteligencia: "))
				x += i
			if x <= usuario.puntos:
				s = int(input("Suerte: "))
				x += s
			if x > usuario.puntos:
				print("Lo siento, esa cantidad excede lo que tienes disponible.")
				print("Empezaremos de nuevo por si te equivocaste al repartir.")
		if x < usuario.puntos:
			print("¡Te sobran puntos! Dadas tus malas matemáticas, te las asignaremos a Suerte (puede que la necesites).")
			s += (usuario.puntos - x)
		usuario.vida += v
		usuario.destreza += d
		usuario.resistencia += r
		usuario.inteligencia += i
		usuario.suerte += s
		print("Tus stats iniciales son:")
		print("Vida: {} Destreza: {} Resistencia: {} Inteligencia: {} Suerte: {}".format(usuario.vida,usuario.destreza,usuario.resistencia,usuario.inteligencia,usuario.suerte))
		print()
		print()
		print("Aquí está el listado de todos los equipamientos que hay, elige un número para equiparlo. En caso de que ya no quieras equiparte más ingresa -1.")
		for equipo in self.equipos:
			print("{}.- {}: Bonificador {} a {}").format(int(equipos.index(equipo)) + 1, equipo.nombre, equipo.bonificador, equipo.atributo)
		n = int(input())


class Personaje:
	def __init__(self,nombre):
		self.nombre = nombre
		self.vida = 0
		self.destreza = 0 
		self.resistencia = 0
		self.inteligencia = 0
		self.suerte = 0
		self.puntos = 0
		self.tiempo = 0



class Prueba:
	def __init__(self, nombre, vida, destreza, resistencia, inteligencia, suerte, debilidad):
		self.nombre = nombre
		self.vida = vida
		self.destreza = destreza
		self.resistencia = resistencia
		self.inteligencia = inteligencia
		self.suerte = suerte
		self.debilidad = debilidad



class Consumible:
	def __init__(self,nombre,stock,stat,cuanto,costo):
		self.nombre = nombre
		self.stock = stock
		self.stat = stat
		self.cuanto = cuanto
		self.costo = costo

class Equipamiento:
	def __init__(self,nombre, atributo, bonificador):
		self.nombre = nombre
		self.atributo = atributo
		self.bonificador = bonificador
#########################################################################
###-----------------------------------------------------------------###
##########################################################################


consumibles = []
equipamientos = []
pruebas = []
print("¡Bienvenido a la simulación de pruebas! ")
nombre = str(input("Por favor escribe el nombre de tu personaje: "))
usuario = Personaje(nombre)
file = open("base.txt")
x = 0
for line in file:
	line = line.strip()
	line = line.split(",")
	if x == 0:
		usuario.vida = int(line[0])
		usuario.tiempo = int(line[1])
		usuario.puntos = int(line[2])
	elif x == 1:
		cons = int(line[0])
		equi = int(line[1])
	elif (x > 1) and (x <= cons + 1):
		nombre = str(line[0])
		nombre = Consumible(str(line[0]),int(line[1]),str(line[2]),int(line[3]),int(line[4]))
		consumibles.append(nombre)
	elif (x > cons 
		+ 1) and (x <= cons + equi + 1):
		nombre = str(line[0])
		nombre = Equipamiento(str(line[0]), str(line[1]), float(line[2]))
		equipamientos.append(nombre)
	else:
		nombre = line[0]
		nombre = Prueba(str(line[0]),int(line[1]),int(line[2]), int(line[3]), int(line[4]), int(line[5]), str(line[6]))
		pruebas.append(nombre)
	x += 1
simulacion = Simulacion(consumibles, equipamientos, pruebas, usuario)
simulacion.empezar()
s = str(input())