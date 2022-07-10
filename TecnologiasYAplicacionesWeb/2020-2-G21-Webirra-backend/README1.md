# Grupo 21 "Webirra"
### PUC IIC2513 - Tecnologías y Aplicaciones Web - Repositorio de Proyecto de Curso
## Integrantes

| Nombre                | Email       | Usuario de Github |
|:--------------------- |:-------------|:-------------|
| José Baboun | jibaboun@uc.cl | [@josebaboun](https://www.github.com/josebaboun) |
| Vicente Espinosa | vnespinosa@uc.cl | [@vnespinosa](https://www.github.com/vnespinosa) |
| Gonzalo Vargas | gtvargas@uc.cl | [@gtvargas](https://www.github.com/gtvargas) |

## Descripción de la distribución del repositorio
El repositorio usa la distribución sugerida por el enunciado, esto es:
- El archivo *index.html* contiene el landing page de nuestra pagina
- La carpeta *views* contiene todas las vistas, es decir, todos los archivos *.html*
- La carpeta *assets* contiene las carpetas *styes*, *imgs* y *scripts*
- La carpeta *styles* contiene los estilos de nuestras vistas, los archivos *.css*
- La carpeta *imgs* contiene todos los archivos de imagen que usamos en las vistas
- La carpeta *scripts* contiene los archivos JavaScript *.js*

## Descripción del proyecto
Nuestro proyecto es una juego muy similar a otro llamado **Risk**, pero con cambios singificativos en el modo de juego, pues esta versión está adaptada para el juego estilo *"play by email"*, ya que los turnos no tienen un orden, y no se sabe que es lo que los demás jugadores hicieron hasta el siguiente turno.
Más infromación sobre el funcionamiento de el juego en la sección *Como jugar* de la pagina o en *Acerca de*.

## Tecnologías empleadas
Se utiliza html para la estructura de la app, css para el estilo y colores, y JavaScript para todas las funcionalidades extra.

## ¿Cómo ejecutar la aplicación?
Para ejecutar la aplicación, hay que levantar un servidor local en el directorio donde esté la aplicación, e ingresar por el browser al puerto donde lo tiene levantado.\
Al ingresar a la aplicación, el usuario podrá visitar distintas secciones presentes en la barra de navegación, conocer las reglas del juego, y crearse una cuenta para jugar. Si el usuario se registra en la aplicación y luego hace login con su cuenta, ingresará a la interfaz del juego.\
En la sección específica de la *Tarea 3* se detalla sobre *cómo jugar*.

## Otros

En los botones para hacer una jugada y guardarla se usaron íconos.

### Respecto a las reglas del juego

Se realizaron algunas modificaciones con respecto a la Tarea 1, las cuales se detallan a continuación:
- En la Tarea 1 se había presentado una vista de la interfaz del juego para cuando era el turno de jugar, y otra para cuando no lo era. Esto se cambió, ya que el juego al ser "play by email" no tiene turnos. Por lo tanto, solo hay una vista, ya que siempre les tocará jugar.
- Hubo cambios en la selección de algunos territorios, principalmente debido a la forma del mapa que finalmente escogimos. Específicamente, se eliminó la biblioteca (en el mapa no se distingue del edificio de Sociales) y la Capilla quedó como Centro Estratégico. También se eliminó Teología por su pequeño tamaño. Lo mismo ocurrió con el Casino, ya que no está en el mapa que escogimos (este corresponde al Campus en el año 2011).

- Se modificó como funciona la reparticion de nuevas tropas, ahora se realiza de manera automatica por parte del servidor.

## Respecto a la tarea 3

### Mejoras de navegación y visuales

- Se arregla lo relativo al z-index para que el Header sea siempre lo que esté "sobre"el resto de la página.
- En la página para efectuar la jugada se cambian los botones, haciendo que estos no se corten. También se ordena la página para que el tablero de resultados se ubique al lado del mapa con un tamano de pantalla más pequeno.
- Se agregan íconos a lo largo de la aplicación.
- La sección de reglas se hace scrollable en el div que las explica. Se hace con el fin de mejorar la experiencia de usuario.
- Se crea nuevo landing page para ordenar el viaje del usuario

### Sobre el login

- Se establece un login que utiliza el local storage
- Este avisa a través de alertas si acepta los datos ingresados o no.
- Es capaz de determinar cuando se deja el campo de usuario o de contrasena vacíos y avisar con mensajes por separado

### Sobre la comunicación Cliente- Servidor

- Se detallan en *documents/protocolos.md* todos los mensajes que serán enviados, en qué momento, y su formato.

### Como jugar

Al ingresar a la interfaz, habrá un mapa donde se podrá diferenciar a qué jugador pertence cada territorio, y haciendo click sobre cada uno se puede conocer el nombre de éste y cuántas tropas hay en ese momento en aquel territorio. Cabe destacar que el usuario, por ahora, será el jugador de color *rojo*.\
El usuario podrá realizar una jugada y guardarla en *Local storage*. Una jugada puede constar de un *reordenamiento* de las tropas que posee actualmente y de un *ataque* a territorios enemigos.\
Al apretar el botón *Mover tropas*, se destacarán en el mapa los territorios que pertenezcan al jugador. Al hacer click sobre el territorio al que desea mandar tropas, el jugador debe apretar el botón *Enviar tropas*, lo cual generará que se marquen del color del jugador aquellos territorios desde los cuales puede mandar tropas (aquellos que sean adyacentes y además pertenezcan a él). El usuario al hacer clik sobre el territorio desde el cual enviará las tropas, deberá indicar cuántas tropas desea enviar.\
Para realizar un ataque se lleva a cabo un proceso similar. Al apretar el botón *Atacar*, podrá elegir en el mapa el territorio que desea atacar, desde cuál desea atacarlo, y con cuántas tropas. Cabe destacar que en un mismo turno el jugador puede preparar varios *ataques* y varios *reordenamientos*. Todo dependerá de la cantidad de tropas que posea el jugador en cada territorio.\
Una vez lista la jugada, el jugador al presionar el botón *Guardar jugada*, guardará la jugada en *Local storage*, y podrá editarla cuando lo estime conveniente. También podrá borrar del *Local storage* la jugada si desea realizar una completamente nueva con el botón *Borrar jugada*, el cual aparece solo si hay una jugada guardada.\
El usuario al apretar el botón *Cargar Partida*, podrá simular una respuesta del servidor. Allí se actualizará el mapa y podrá realizar otra jugada.\
Cabe destacar que la disposición inicial del mapa también se realizó leyendo una respuesta simulada del servidor. O sea, en la carpeta *views/* hay dos archivos de extensión *.json* que contienen supuestos mensajes enviados por el servidor: mensaje_servidor.json y mensaje_servidor2.json.

## Consideraciones para futuras entregas

- El jugador podrá ver el estado actual de la jugada que está realizando. Actualmente, la puede ver ingresando a la consola (Inspeccionar en browser), donde se imprime la jugada.
- El usuario podrá acceder a una bitácora de jugadas con el historial de lo que ha pasado en todos los turnos en el juego.

