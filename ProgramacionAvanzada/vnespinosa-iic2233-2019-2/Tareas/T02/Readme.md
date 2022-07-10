# Tarea 2: DCCampo

## Consideraciones generales 
* A veces se lagea un poco el juego, y puede llegar a congelarse, pero despues vuelve a funcionar. Solo me paso un par de veces.

* No entendi por completo el tema de señales, entonces puede que hayan algunas mal implementadas.

* Hice el bonus de la casa (aunque es muy fea).

* Perdon por la cantidad de archivos pero lo hice para evitar pasar las 400 lineas, tambien hay algunas lineas al limite de los 100 caracteres, pero no las dividí por la misma razon.


### Cosas implementadas y no implementadas 

* **Parte Ventanas**:
    * **Ventana de inicio**: Hecha completa, se usa la señal ```revisar_mapa``` e ```iniciar_juego``` en  *pantalla_inicio.py*, y ```Respuesta_cargar_mapa``` en *Back_end.py*.
    * **Ventana de Juego**: Hecha completa, se usan los archivos *Back_end_juego_1.py* y *Back_end_2.py* en los cuales se usan muchas señales, tales como ```fin```, ```procesar_key```, ```revisar_tiempo_drops```, ```actualizar_inventario```, ```pixeles_main```, ```Cargar```, ```Comprar```, ```mover```, ```Agregar_cultivo```, ```entrar_casa```, ```abrir_tienda```, ```pasar_dia```. actualizar_energia es una funcion de *Juego.py*, la cual se ejecuta depues de acciones que gastan energia, por lo que no fue necesario hacer una señal para esta, a menos de que llegue a 0. 
    * **Inventario**: Hecho completo. Todo esta implementado como se debe, el drag y drop se hicieron por separado, ambos en el principio del archivo *Back_end_juego_1.py*
    * **Tienda**: Hecha completa. Todas las señales, al igual que la ventana de esta estan en el archivo *Compra.py*, no se puede acceder a la tienda sin estar sobre ella en el mapa.
* **Parte Entidades**:
    * **Parte Jugador**: Hecha completa, el movimiento es "fluido", da pasos, y choca tanto con piedras, arboles como con el borde del mapa, todo esto esta en *Back_end_2.py*, se usa la funcion ```mover_usuario```, la cual a su vez llama a otras para comprobar si es factible el movimiento. 
    Los cultivos son recogidos al pasar sobre ellos, al igual que cualquier otro tipo de "drop", esto se comprueba cada vez que el jugador se mueve, con la funcion ```revisar_pisar_drop```.
    * **Parte Recursos**: Los cultivos se actualizan correctamente usando un temporizador propio, lo que si es que me parece que cambie un poco las imagenes de los cultivos, pero no deberia ser problema, era algo confuso el enunciado, entonces puse que la imagen final de los choclos sea la del nivel 6, y antes la del 7, esto deberia ser problema solo la primera cosecha, pues despues sigue el orden adecuado, fue un error de interpretacion del enunciado, no de codigo. Los arobles y oro aparecen correctamente (puse que al pasar un dia, se cuente todo el tiempo que ha pasado y se le agregue tanto a los cultivos como a los "drops", por lo que no se veran 2 oros a la vez en el mapa a menos que el dia dure menos que el tiempo de duracion del oro). La leña aparece al clickear un arbol y tener el hacha en el inventario, el label esta definido en *Back_end_2.py*, se llama ```ClickMadera```. Los recursos desaparecen pasado el tiempo, ya sea jugando o durmiendo (el tiempo no pasa en la tienda). 
    * **Parte Herramientas**: No se puede ni talar sin hacha, ni arar sin azada.
* **Tiempo**:
    * **Reloj**: Hecha completa, se pasa el tiempo cada 15 minutos, pues me parecio mas estetico que pasarlo cada minuto, se usa el reloj ```self.timer```, el que esta conectado a ```self.actualizar_tiempo```.
 * **Funcionadidades extra**:
    * **K+I+P**: Hecha completa, solo que a veces me cuesta un poco activarla, pero debe ser problema de mi computador.
     * **M+N+Y**: Hecha completa.
     * **Pausa**: Hecha completa, el boton de pausa se define en el *Back_end_juego_1.py*, se define como ```self.boton_pausa```.
* **General**:
     * **Modularizacion**: El front end son los archivos *Juego.py*, *pantalla_inicio.py*, *Compra.py* y *ventana_fin.py*. Y el back end son *Back_end.py*, *Back_end_juego_1.py* y *back_end_2.py*
     * **Dependencia circular**: Me preocupe en todo momento de evitar esto, por lo que no deberia haber.
     * **Archivos**: Uso todos los archivos correctamente
     * **Consistencia**: Siempre se muestra la informacion actual tanto de energia, dinero e inventario.
     * **parametros.py**: solo use ese archivo para todos los parametros no entregados.
* **Bonus**:
     * **Pesca**: No la hice. No se entendia mucho
    * **Casa**: Hecha completa (el tiempo sigue pasando dentro de la casa)

## Ejecución
El módulo principal de la tarea a ejecutar es  ```main.py```.


## Librerías
### Librerías externas utilizadas
La lista de librerías externas que utilicé fueron las siguientes:

1. ```PyQt5.QtWidgets```, ```PyQt5.QtCore```, ```PyQt5.QtGui```, ```random```, ```os```, ```sys```, ```PyQt5.QtTest```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```parametros.py```: contiene parametros y diccionarios con paths para los pixeles y el usuario


## Supuestos y consideraciones adicionales
Los supuestos que realicé durante la tarea son los siguientes:

1. El tiempo pasa en todos lados a menos que se pause, o se entre a la tienda.

-------


## Referencias de código externo 

https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5
Para los drag y drop labels. (de la linea 11 a la 47 en archivo *Back_end_juego_1.py*)