# Tarea 1: Initial P

## Consideraciones generales 
* No termine la tarea por completo. La entregue muy apurado por lo que hay muchas cosas que no logre testear como corresponde.


* Hice el bonus de buenas practicas solamente.


### Cosas implementadas y no implementadas 

* **Parte Menus**:
    * **Menu de sesion**: Hecha completa.
    * **Menu principal**: Hecha completa.
    * **Menu de compra de vehículos**: Hecha completa.
    * **Menu de preparacion carrera**: Hecha completa.
    * **Menu de carrera**: Hecha completa.
    * **Menu de los pits**: Hecha completa.
* **Parte Flujo de la carrera**:
    * **Parte Dinero por vuelta**: Hecha completa, se entrega dinero si queda en primer lugar (no revise bien si se calcula correctamente el dinero, pero supongo que si)
    * **Parte orden de los menus**: Hecha completa
    * **Parte tiempo en los pits**: No lo implemente, pero esta la funcion.
    * **Parte dinero y experiencia**: Hecha completa.
 * **Entidades**:
    * **Vehiculo**: Hecha completa, cada categoria como una subclase de esta (Clases.py).
     * **Pista**: Hecha completa (Clases.py).
     * **Piloto**: Hecha completa (Clases.py).
* **Parte Archivos**:
    Hecha completa, se cargar y guardan correctamente todos los archivos.
* **Parte Formulas**:
    Hecha completa, en el archivo funciones.py

## Ejecución
El módulo principal de la tarea a ejecutar es  ```main.py```.


## Librerías
### Librerías externas utilizadas
La lista de librerías externas que utilicé fueron las siguientes:

1. ```random```: ```randit()```, ```choice()```, ```random()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones```: contiene las funciones: ```Velocidad_Recomendada()```, ```Velocidad_Intencional()```, ```Velocidad_Real()```, ```Dificultad_Control()```, ```Hipotermia()```, ```Golpe_Recibido_por_vuelta()```, ```Tiempo_Pits()```, ```Dinero_Por_Vuelta()```, ```Probabilidad_accidente()```, ```Tiempo_Vuelta()```, ```Dinero_Ganador()```, ```Ventaja_ultimo_lugar()```, ```Experiencia_ganador()```, ```Cargar_Contrincantes()```, ```Cargar_Pistas()```, ```Cargar_Contrincantes_Pista()```

2. ```parametros```: contiene todos los paramteros con respecto a las clases

3. ```Clases```: contiene a las clases y sus respectivas funciones: ```Corredor()```, ```Competidor(Corredor)```,```Contrincante(Corredor)```,```Vehiculo()```,```Automovil(Vehiculo)```,```Motocicleta(Vehiculo)```,```Troncomovil(Vehiculo)```,```Bicicleta(Vehiculo)```,```Pista()```

4. ```menu```: contiene a las clases y sus respectivas funciones: ```Menu()```, ```MenuInicio(Menu)```, ```MenuPrincipal(Menu)```, ```MenuCompra(Menu)```, ```Menu_Preparacion_Carrera(Menu)```, ```Menu_Carrera(Menu)```,  ```MenuPits(Menu)```



## Supuestos y consideraciones adicionales
Los supuestos que realicé durante la tarea son los siguientes:

1. Al iniciar una partida nueva, se le regala un vehiculo generado al azar al usuario.
2. Cualquier parametro usado, que no venia especificado en el archivo paramtero, fue "hardcodeado", como el precio de comprar un vehiculo.

-------


## Referencias de código externo 

No use codigo externo.
