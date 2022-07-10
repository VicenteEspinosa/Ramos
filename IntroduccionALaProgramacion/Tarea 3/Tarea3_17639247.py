class Simulacion:
	def __init__(self):
		self.consumibles = []
		self.equipamientos = []
		self.pruebas = []
		self.personaje = []

	def empezar(self):
		guardado = []
		print("¡Bienvenido a la simulación de pruebas! ")
		nombre = str(input("Por favor escribe el nombre de tu personaje: "))
		usuario = Personaje(nombre)
		guardado.append(nombre)
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
				self.consumibles.append(nombre)
			elif (x > cons 
				+ 1) and (x <= cons + equi + 1):
				nombre = str(line[0])
				nombre = Equipamiento(str(line[0]), str(line[1]), float(line[2]))
				self.equipamientos.append(nombre)
			else:
				nombre = line[0]
				nombre = Prueba(str(line[0]),int(line[1]),int(line[2]), int(line[3]), int(line[4]), int(line[5]), str(line[6]))
				self.pruebas.append(nombre)
			x += 1
		file.close()
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
		i = 0
		t = 0
		for equipo in self.equipamientos:
			i += 1
			print(str(i) + ".- " + str(equipo.nombre) + ": Bonificador " + str(equipo.bonificador) + " a " + str(equipo.atributo))
		n = int(input("> "))
		print()
		while n != -1:
			if 0 < n < len(self.equipamientos) + 1:	
				equipo = self.equipamientos[n-1]
				self.equipamientos.remove(equipo)
				t += 1
				usuario.multiplicador(equipo)
				if len(self.equipamientos) == 0:
					print()
					print("No te queda mas equipo!")
					print()
					n = -1
					break
				i = 0
				if t == 3:
					print()
					print("Has equipado el maximo de equipo posible!")
					print()
					break
				else:
					for equipo in self.equipamientos:
						i += 1
						print(str(i) + ".- " + str(equipo.nombre) + ": Bonificador " + str(equipo.bonificador) + " a " + str(equipo.atributo))
					print()
					n = int(input("> "))
					print()
			elif n == -1:
				break
			else:
				n = int(input("El numero ingresado no es valido, por favor intentalo otra vez: "))
		vive = True
		for prueba in self.pruebas:
				if vive:
					usuario.guardar()
					print("Aquí estan los consumibles, selecciona el número del objeto que deseas.")
					print("Para comenzar la evaluación ingresa -1.")
					print()
					print("Stats actuales: V ->" + str(usuario.vida) + " D ->" + str(usuario.destreza) + " R ->" + str(usuario.resistencia) + " I ->" + str(usuario.inteligencia) + " S ->" + str(usuario.suerte))
					print("Tiempo disponible: " + str(usuario.tiempo))
					i = 0
					for consumible in self.consumibles:
						i += 1
						print(str(i) + ".- (" + str(consumible.stock) + ") " + str(consumible.nombre) + ": " + str(consumible.costo) + " de tiempo,  " + str(consumible.cuanto) + " de " + str(consumible.stat))
					n = int(input("> "))
					print()
					while n != -1:
						if len(self.consumibles) == 0:
							print("No te quedan mas consumibles!")
							n = -1
						if (0 < n < len(self.consumibles) + 1) :
							consumible = self.consumibles[n-1]
							if consumible.costo < usuario.tiempo:
								usuario.tiempo -= consumible.costo	
								consumible.stock -= 1
								if consumible.stock == 0:
									self.consumibles.remove(consumible)
								usuario.multiplicador_consumible(consumible)
								i = 0
								for consumible in self.consumibles:
									i += 1
									print(str(i) + ".- (" + str(consumible.stock) + ") " + str(consumible.nombre) + ": " + str(consumible.costo) + " de tiempo,  " + str(consumible.cuanto) + " de " + str(consumible.stat))
								print()
								print("Stats actuales: V ->" + str(usuario.vida) + " D ->" + str(usuario.destreza) + " R ->" + str(usuario.resistencia) + " I ->" + str(usuario.inteligencia) + " S ->" + str(usuario.suerte))
								print("Tiempo disponible: " + str(usuario.tiempo))
								n = int(input("> "))
								print()
							else:
								print("No tienes suficiento tiempo para eso :(")
								print("Intentalo con otro consumible")
								print("Tiempo disponible: " + str(usuario.tiempo))
								n = int(input(">"))
						elif n == -1:
							break
						else:
							n = int(input("El numero ingresado no es valido, por favor intentalo otra vez: "))
					vive = usuario.pelea(prueba)
					usuario.restaurar()
		if vive:
			print("Felicitaciones! Pasaste todas las pruebas! :D")
			print("Deseas guardar tu progreso? (SI/NO)")
			r = str(input("> "))
			if r.lower() == "si":
				r = True
				print("¿Que nombre deseas darle a tu archivo?")
				archivo = str(input("> "))
				file = open(archivo,'w')
				for linea in guardado:
					file.write(linea + '\n')
				file.close()
				m = str(input("Presiona enter para salir"))

			elif r.lower() == "no":
				print("Presiona enter para salir")
				r = True
				s = str(input())

			else:
				r = False
			while r == False:
				print("Ingresa alguna de las opciones por favor (SI/NO)")
				r = str(input("> "))
				if r.lower() == "si":
					r = True
					print("¿Que nombre deseas darle a tu archivo?")
					archivo = str(input("> "))
					file = open(archivo,'w')
					for linea in guardado:
						file.write(linea + '\n')
					file.close()
					m = str(input("Presiona enter para salir"))
				elif r.lower() == "no":
					print("Presiona enter para salir")
					r = True
					s = str(input())
				else:
					r = False

		else:
			print("Presiona enter para salir...")
			s = str(input())



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
		self.valores_finales = []

	def multiplicador(self,other):
		if other.atributo == "vida":
			self.vida = int(self.vida * other.bonificador)
		if other.atributo == "destreza":			
			self.destreza = int(self.destreza * other.bonificador)
		if other.atributo == "resistencia":
			self.resistencia = int(self.resistencia * other.bonificador)
		if other.atributo == "inteligencia":
			self.inteligencia = int(self.inteligencia * other.bonificador)
		if other.atributo == "suerte":
			self.suerte = int(self.suerte * other.bonificador)

	def multiplicador_consumible(self,other):
		if other.stat == "vida":
			self.vida = int(self.vida * other.cuanto)
		elif other.stat == "destreza":			
			self.destreza = int(self.destreza * other.cuanto)
		elif other.stat == "resistencia":
			self.resistencia = int(self.resistencia * other.cuanto)
		elif other.stat == "inteligencia":
			self.inteligencia = int(self.inteligencia * other.cuanto)
		elif other.stat == "suerte":
			self.suerte = int(self.suerte * other.cuanto)

	def pelea(self,prueba):
		print("¡Llegó la hora de la evaluación!")
		print("Prepárate " + str(self.nombre) + " para enfrentar a la " + str(prueba.nombre) + " (música dramática) Esta prueba posee V " + str(prueba.vida) + " D " + str(prueba.destreza) + " R " + str(prueba.resistencia) + " I " + str(prueba.inteligencia) + " S " + str(prueba.suerte) + " y es débil contra la " + str(prueba.debilidad) + " ¿Podrás superarla?")
		print()
		print("2 horas después... y 2 semanas...")
		print()
		if prueba.debilidad == "destreza":
			debilidad = self.destreza
		elif prueba.debilidad == "resistencia":
			debilidad = self.resistencia
		elif prueba.debilidad == "inteligencia":
			debilidad = self.inteligencia
		elif prueba.debilidad == "suerte":
			debilidad = self.suerte		
		perdio = (self.destreza + self.resistencia + self.inteligencia + self.suerte - prueba.destreza - prueba.resistencia - prueba.inteligencia - prueba.suerte) * (prueba.vida // debilidad)
		if perdio >= 0:
			print()
			print("Perfecto! Obtuviste un 7!")
			print()
			print("¿Estás listo para el siguiente combate? Mejor prepárate antes.")
			return True
		else:
			if abs(perdio) >= self.vida:
				print("Lo siento, pero no pasaste... Suerte el proximo semetre")
				self.vida += perdio
				return False
			else:
				self.vida += perdio
				print()
				print("¡SÍ! Lo lograste, pero perdiste " + str(abs(perdio)) + " puntos de vida ")
				print()
				print("¿Estás listo para el siguiente combate? Mejor prepárate antes.")
				print()
				return True

	def guardar(self):
		self.valores_finales = []
		self.valores_finales.append(self.destreza)
		self.valores_finales.append(self.resistencia)
		self.valores_finales.append(self.inteligencia)
		self.valores_finales.append(self.suerte)

	def restaurar(self):
		self.destreza = int(self.valores_finales[0])
		self.resistencia = int(self.valores_finales[1])	
		self.inteligencia = int(self.valores_finales[2])
		self.suerte = int(self.valores_finales[3])


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
		self.stock = stock # Cuanto queda
		self.stat = stat #Stat que aumenta
		self.cuanto = cuanto #Cuanto aumenta
		self.costo = costo #Costo de tiempo

class Equipamiento:
	def __init__(self,nombre, atributo, bonificador):
		self.nombre = nombre
		self.atributo = atributo
		self.bonificador = bonificador
#########################################################################
###----------------------------EMPIEZA CODIGO----------------------------###
##########################################################################

simulacion = Simulacion()
simulacion.empezar()