from Tarea_1 import *

root = tk.Tk()
root.geometry('{}x{}'.format("550", "650"))
app = Application(master=root)
import random
ganador = "nadie"
dinero_1 = int(input("Bienvenidos, por favor ingrese dinero inicial: "))
dinero_2 = dinero_1
app.mostrar_dinero(1, dinero_1)
app.mostrar_dinero(2, dinero_2)
app.poner_apuesta(int(input("Ingrese apuesta: ")))
if (app.obtener_apuesta() > app.preguntar_monto(1)) or (app.obtener_apuesta() > app.preguntar_monto(2)) or (app.obtener_apuesta() < 0):
	while (app.obtener_apuesta() > app.preguntar_monto(1)) or (app.obtener_apuesta() > app.preguntar_monto(2)) or (app.obtener_apuesta() < 0):
		app.poner_apuesta(int(input("Error, ingrese otra apuesta: ")))
dinero_1 = dinero_1 - app.obtener_apuesta()
dinero_2 = dinero_2 - app.obtener_apuesta()
app.mostrar_dinero(1, dinero_1)
app.mostrar_dinero(2, dinero_2)
app.mostrar_ventana(True)
for j in range(1,3):   # Formar cartones
			c = 0
			while c == 0:
				for f in range(0,5):
					n=random.randint(1,20)
					app.agregar(n)
					if app.agregar(n)==False:
						while app.agregar(n) == False:
							n = random.randint(1,20)
					app.colocar_numero(f, c, n, j)  
				c = 1
			while c == 1:
				for f in range(0,5):
					n=random.randint(21,40)
					app.agregar(n)
					if app.agregar(n)==False:
						while app.agregar(n) == False:
							n = random.randint(21,40)
					app.colocar_numero(f, c, n, j)
				c = 2
			while c == 2:
				for f in range(0,5):
					n=random.randint(41,60)
					app.agregar(n)
					if app.agregar(n)==False:
						while app.agregar(n) == False:
							n = random.randint(41,60)
					app.colocar_numero(f, c, n, j)
				c = 3
			while c == 3:
				for f in range(0,5):
					n=random.randint(61,80)
					app.agregar(n)
					if app.agregar(n)==False:
						while app.agregar(n) == False:
							n = random.randint(61,80)
					app.colocar_numero(f, c, n, j)
				c = 4
			while c == 4:
				for f in range(0,5):
					n=random.randint(81,100)
					app.agregar(n)
					if app.agregar(n)==False:
						while app.agregar(n) == False:
							n = random.randint(81,100)
					app.colocar_numero(f, c, n, j) 
				c = 5
			app.reiniciar_contador() 
def turno():
	n = random.randint(1,100)  # Marcar carton
	if (app.agregar(n) == False):
		while (app.agregar(n) == False):
			n = random.randint(1,100)
	app.agregar(n)
	for j in range(1,3): 
		for c in range(0,5):
			for f in range(0,5):
				if (app.obtener_numero(f, c, j) == n):
					app.marcar_numero(f, c, True, j)  # Fin marcar carton
	j_1_completo = True
	j_2_completo = True
	j_1_Y = True
	j_2_Y = True
	j_1_diag = True
	j_2_diag = True
	for j in range(1,3):
		for c in range(0,5):
			for f in range(0,5):
				if app.esta_marcado(f, c, j) == False:
					if j == 1:
						j_1_completo = False
					else:
						j_2_completo = False
			if j_1_completo == True and j_2_completo == False:
				ganador = "j_1 completo"
			elif j_1_completo == True and j_2_completo == True:
				ganador = "empate"
			elif j_1_completo == False and j_2_completo == True:
				ganador = "j_2 completo"
			else:
			   ganador = "nadie"     
	if (ganador == "nadie"):  # Revisar letra Y
		for j in range(1,3):
			if (app.esta_marcado(0, 0, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
			if (app.esta_marcado(1, 1, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
			if (app.esta_marcado(2, 2, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
			if (app.esta_marcado(1, 3, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
			if (app.esta_marcado(0, 4, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
			if (app.esta_marcado(0, 0, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
			if (app.esta_marcado(3, 2, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
			if (app.esta_marcado(4, 2, j) == False):
				if j == 1:
					j_1_Y = False
				else:
					j_2_Y = False
		if (j_1_Y == True) and (j_2_Y == True):
			ganador = "empate"
		if (j_1_Y == True) and (j_2_Y == False):
			ganador = "j_1 Y"
		if (j_1_Y == False) and (j_2_Y == True):
			ganador = "j_2 Y"
		if (j_1_Y == False) and (j_2_Y == False):
			ganador = "nadie"
	if (ganador == "nadie"):  # Revisar diagonal
		c = 0
		f = 0
		while f < 5:
			for j in range(1,3):
				if (app.esta_marcado(f, c, j) == False):
					if j == 1:
						j_1_diag = False
					else:
						j_2_diag = False
			c += 1
			f += 1
		if (j_1_diag == True) and (j_2_diag == True):
			ganador = "empate"
		if (j_1_diag == True) and (j_2_diag == False):
			ganador = "j_1 diagonal"
		if (j_1_diag == False) and (j_2_diag == True):
			ganador = "j_2 diagonal"	
		if (j_1_diag == False) and (j_2_diag == False):
			ganador = "nadie"
	if (ganador == "nadie"):
		n = str(n)
		app.mostrar_mensaje("El número obtenido fue " + n)
	else:
		if (ganador == "j_1 completo"):
			print("El ganador es el jugador 1, formó carton completo")
		elif (ganador == "j_2 completo"):
			print("El ganador es el jugador 2, formó carton completo")
		elif (ganador == "j_1 Y"):
			print("El ganador es el jugador 1, formó la letra Y")
		elif (ganador == "j_2 Y"):
			print("El ganador es el jugador 2, formó la letra Y")
		elif (ganador == "j_1 diagonal"):
			print("El ganador es el jugador 1, formó la diagonal")
		elif (ganador == "j_2 diagonal"):
			print("El ganador es el jugador 2, formó la diagonal")
		elif (ganador == "empate"):
			print("Hubo un empate")
	if (ganador != "nadie"):  # Repartir apuesta
		dinero_1 = app.preguntar_monto(1)
		dinero_2 = app.preguntar_monto(2)
		if (ganador == "j_1 completo") or (ganador == "j_1 Y") or (ganador == "j_1 diagonal"):
			dinero_1 = int(app.preguntar_monto(1) + (2 * app.obtener_apuesta()))
			dinero_2 = int(app.preguntar_monto(2))
		elif (ganador == "empate"):
			dinero_1 = dinero_1 + app.obtener_apuesta()
			dinero_2 = dinero_2 + app.obtener_apuesta()
		else:
			dinero_1 = int(app.preguntar_monto(1))
			dinero_2 = int(app.preguntar_monto(2) + (2 * app.obtener_apuesta()))
		app.mostrar_dinero(1, dinero_1)
		app.mostrar_dinero(2, dinero_2)
		app.poner_apuesta(0)
		app.reiniciar_contador()
		if (dinero_1 == 0) or (dinero_2 == 0):
			app.mostrar_ventana(False)
			if dinero_1 == 0:
				print("El jugador 1 se ha quedado sin dinero!")	 
			if dinero_2 == 0:
				print("El jugador 2 se ha quedado sin dinero!") 
			app.after(1000)
			print("Ahora se cerrara el juego")
			app.after(1500) 
			app.cerrar_ventana()
			app.after(1500)
	if (app.obtener_apuesta() == 0):
		app.mostrar_ventana(False)
		continuar = str(input("¿Continuar jugando? "))
		while (continuar != "si") and (continuar != "no"):
			continuar = str(input("Debes responder con si o no... Quieres continuar? "))
		if (continuar == "no"):
			print("El juego termino: Jugador 1 =",dinero_1,"Jugador =",dinero_2)
			print("Adios!")
			app.after(2500)
			app.cerrar_ventana()
		elif (continuar == "si"):
			app.poner_apuesta(int(input("Ingrese apuesta: ")))
			if (app.obtener_apuesta() > app.preguntar_monto(1)) or (app.obtener_apuesta() > app.preguntar_monto(2)) or (app.obtener_apuesta() < 0):
				while (app.obtener_apuesta() > app.preguntar_monto(1)) or (app.obtener_apuesta() > app.preguntar_monto(2)) or (app.obtener_apuesta() < 0):
					app.poner_apuesta(int(input("Error, ingrese otra apuesta: ")))
			dinero_1 -= app.obtener_apuesta()
			dinero_2 -= app.obtener_apuesta()
			app.mostrar_dinero(1, dinero_1)
			app.mostrar_dinero(2, dinero_2)
			app.mostrar_ventana(True)
			j = 0
			c = 0
			f = 0
			for j in range(1,3):
				for c in range(0,5):
					for f in range(0,5):
						app.marcar_numero(f, c, False, j) 
			app.reiniciar_contador()
			for j in range(1,3):   # Formar cartones
				c = 0
				while c == 0:
					for f in range(0,5):
						n=random.randint(1,20)
						app.agregar(n)
						if app.agregar(n)==False:
							while app.agregar(n) == False:
								n = random.randint(1,20)
						app.colocar_numero(f, c, n, j)  
					c = 1
				while c == 1:
					for f in range(0,5):
						n=random.randint(21,40)
						app.agregar(n)
						if app.agregar(n)==False:
							while app.agregar(n) == False:
								n = random.randint(21,40)
						app.colocar_numero(f, c, n, j)
					c = 2
				while c == 2:
					for f in range(0,5):
						n=random.randint(41,60)
						app.agregar(n)
						if app.agregar(n)==False:
							while app.agregar(n) == False:
								n = random.randint(41,60)
						app.colocar_numero(f, c, n, j)
					c = 3
				while c == 3:
					for f in range(0,5):
						n=random.randint(61,80)
						app.agregar(n)
						if app.agregar(n)==False:
							while app.agregar(n) == False:
								n = random.randint(61,80)
						app.colocar_numero(f, c, n, j)
					c = 4
				while c == 4:
					for f in range(0,5):
						n=random.randint(81,100)
						app.agregar(n)
						if app.agregar(n)==False:
							while app.agregar(n) == False:
								n = random.randint(81,100)
						app.colocar_numero(f, c, n, j) 
					c = 5
				app.reiniciar_contador() 
				app.mostrar_mensaje("")
# ESTO NO SE TOCA
app.button.config(command=turno)
app.mainloop()
