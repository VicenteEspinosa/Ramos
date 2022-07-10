# Tarea 0: LegoSweeper

## Consideraciones generales 
* Si no me equivoco, todo deberia funcionar correctamente, en algun momento fallaba si se entregaba un input vacio, es decir, se presiona enter sin escribir nada, pero deberia estar solucionado.


* El bonus esta implementado, si lo quieren sacar, deben borrar en el archivo principal las dos veces que aparece la funcion Revisar_ceros()

* Ya viene un archivo con algunos puntajes ficticios, pues si esta vacio puede fallar el pedir que imprima el ranking. Se sobreescriben bien, y solo anota los 10 mejores.

### Cosas implementadas y no implementadas 

* **Parte Menus**:
    * **Menu de inicio**: Hecha completa, incluido cada opcion en el.
    * **Menu de juego**: Hecha completa, incluido cada opcion en el.
* **Parte Reglas**:
    * **Parte revisar coordenadas**: Hecha completa, revisa que la coordenada exista, que no este marcada, y si es o no un lego
    * **Parte contar legos alrededor**: Hecha completa
 * **Parte Partida**:
    * **Parte Crear**: Hecha completa
     * **Parte Guardar**: Hecha completa, me quedo un elemento de la lista que no se usa, pero no molesta en el dasarrollo del programa.
     * **Parte Cargar**: Hecha completa
* **Parte Puntajes**:
    Echa completa
* **Parte Archivos entregados**:
    Se importan correctamente todos los archivos, sin usar import *

## Ejecución
El módulo principal de la tarea a ejecutar es  ```Tarea 0.py```.


## Librerías
### Librerías externas utilizadas
La lista de librerías externas que utilicé fueron las siguientes:

1. ```random```: ```randit()```
2. ```os```: ```path()``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Funciones```: contiene las funciones: ```Entre_3_15()```, ```incio()```, ```turno()```, ```gen_tablero()```, ```Cargar_partida()```, ```gen_lista_visible()```, ```Guardar_partida()```, ```Revelar_baldosa()```, ```Perdio()```, ```Revelar_todo()```, ```Gano()```, ```Actualizar_puntajes()```, ```Revisar_ceros()```


## Supuestos y consideraciones adicionales
Los supuestos que realicé durante la tarea son los siguientes:

1. El juego puede cargar o empezar una partida nueva, luego ejecutara un turno, y quedara atrapado en un while hasta que o se pierda o se gane.
2. Para ver si se perdio, el juego revisa que balosa se depejo, y si es una "L", transforma la variable perdio en True
3. Para ver si gano, revisa primero si no perdio al depejar una baldosa, y luego revisa si en la lista que representa queda algun elemento igual a " " (espacio), y luego ve si en esa misma posicion, pero en la lista con las soluciones, hay algo que no sea una "L", y si no lo hay, significa que despejo todas las baldosas sin lego, y gano.

4. Para contar el puntaje, como se iplemento el bonus, conte de todas formas las baldosas que se despejan solas, para eso recorro toda la lista de las casillas marcadas, y cuento cuantas casillas son distintas a " ", que representa las desamrcadas
5. Al momento de crear murallas, se permite que el usuario cree más de una a la vez. Esto es porque pueden haber tantas murallas como lo permitan los recursos y los trabajadores, así no tiene que crear 5 veces una muralla, sino que pueda crear 5 de una vez (como con los personajes).
6. Al perder, se revelan los legos, y deje un input final, para que puedan ver el tablero y el programa no se cierre automaticamente.



-------




## Referencias de código externo 

No use codigo externo.
