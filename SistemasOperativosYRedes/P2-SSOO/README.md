# Integrantes

- Vicente Espinosa
  17639247

- Brian Saavedra
  17205670
  
- Pablo Molina
  17641381

- José Sáenz
  17640644
  
- Gonzalo Vargas
  17637120



## Descripción paquetes

Para la implementación del lobby, donde jugadores pueden conectarse simultáneamente, se utilizó la librería *pthread*, donde se le asgina a cada posible nuevo jugador un thread, el cual se libera y termina cuando este está listo para jugar.

Los otros paquetes utilizados para la comunicación entre cliente y servidor mediante sockets son los que venían incluidos en el código de ejemplo.


## Messages codes

### Message code 1

Se utiliza para enviar un mensaje al cliente, el cual se debe desplegar en la consola. Después de esto se espera que el cliente responda este mensaje con algún input.


### Message code 2

Se usa para enviar un mensaje al cliente, el cual se debe desplegar en la consola. En este caso no se espera ninguna respuesta del cliente.

### Message code 3

Este codigo indica que se terminó la conexión entre el cliente y el servidor. Se muestra en la consola el mensaje enviado antes de cerrar la conexión.

## Correr programa

Para correr el programa se debe hacer `make` en la carpeta `./server` y `./client`. 

Luego se debe ejectutar cada binario en su carpeta respectiva, para ejecutrar el servidor se debe ejecutar como `./server -i [Dirección IP] -p [Numero de puerto]`, y para correr el cliente se corre con `./client -i [Dirección IP] -p [Numero de puerto]`. En ambos casos se puede cambiar el orden de los argumentos.


## Funciones principales

### empezar_juego()

Esta función se ejecuta cuando el lider comienza el juego, aca se cierran los threads que ya no se van a usar y comienza el flujo del juego.

### desplegar_menu()

Esta función maneja todo el menu mostrado en consola en cada turno y contiene todas las acciones que puede hacer un usuario.


### mostrar_info()
Esta función sirve para que el jugador que esté en su turno pueda revisar sus recursos, cantidad de aldeanos y niveles de aldeanos y de ataque y defensa.

### espiar()

Esta función permite a un jugador espiar el estado del ejercito de otro jugador de la partida, con un costo de 30 de oro, con esto puede averiguar si le conviene atacar o no.
 
### robar()
Esta función permite que el jugador que esté en su turno pueda robarle, a su elección, comida u oro a otro rival. El robo solo se podrá ejecutar si la cantidad de ciencia que tiene el "ladrón" es igual o mayor a 10, y será válido solo si la víctima tiene al menos 10 unidades de ese recurso, ya que se está aproximando la parte entera por abajo.


### crear_aldeano()

Esta función le permite al jugador crear un aldeano del tipo que desee (agricultor, minero, ingeniero o guerrero), si este tiene los recursos necesarios.

### subir_nivel()

Esta función le permite al jugador subir el nivel de la infraestructura de su aldea (agricultura, mineria, ingenieria, ataque o defensa) si es que este posee los recursos necesarios, el costo de subir de nivel aumenta de forma progresiva.

### atacar()

Esta función ejecuta la acción de atacar en el juego, aca se puede atacar a cualquier jugador vivo y luego informa a todos del resultado. Si el atacante gana además elimina al defensor del juego y se queda con todos sus recursos.


## Supuestos

Se asume que quien ejecute el programa comprobará previamente que la IP y/o socket entregado como parametro para el programa sean correctos.