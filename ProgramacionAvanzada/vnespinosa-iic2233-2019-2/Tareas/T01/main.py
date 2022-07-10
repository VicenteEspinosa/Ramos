import parametros as p
import funciones as f
import Clases as c
import menu as m

a = m.Menu()


Pistas = f.Cargar_Pistas()
Contrincantes_totales = f.Cargar_Contrincantes()
a = m.MenuInicio() 
Usuario = a.Usuario
while True:
    b = m.MenuPrincipal(Usuario, Pistas, a.usuarios, Contrincantes_totales)
    Usuario = b.Usuario
    usuarios = b.usuarios
    pista = b.pista
    Contrincantes_Pista = f.Cargar_Contrincantes_Pista(pista, Contrincantes_totales)
    carrera = m.Menu_Carrera(Usuario, pista, Contrincantes_Pista)
    Usuario = carrera.Usuario
