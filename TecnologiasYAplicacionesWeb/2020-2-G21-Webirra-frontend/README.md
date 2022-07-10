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

## Tecnologías empleadas frontend
Se utiliza html para la estructura de la app, css para el estilo y colores, y JavaScript para todas las funcionalidades extra.

## Tecnologías empleadas backend
-El manejador de paquetes utilizado es *Yarn*.\
-El ORM para manejar la base de datos es *Sequelize*.\
-Para encriptar las claves se utiliza *bcrypt*.\
-Se utiliza el framework *Koa*, junto a *Koa-body*, *Koa-session*, *Koa router*.\
-La base de datos es de *Postgres*
-Se utiliza *Json Web Tokens* para manejar los tokens enviados desde cliente a servidor.

## Sobre los endpoints

Toda la información respecto a las rutas de consulta en el backend o los endopoints se encuentra en */documents/protocolos.md*

## ¿Cómo ejecutar la aplicación?

A continuación se detalla como ejecutar la aplicación de forma remota, además de los pasos que se deben seguir para probar todas las funcionalidades del juego:

El **backend** de la aplicación se encuentra en Heroku, en el siguiente link: https://git.heroku.com/protected-scrubland-81841.git.
Por su parte, el **frontend** se encuentra en el siguiente link: https://webirra.herokuapp.com.

Para ejecutar la aplicación, debe ingresar al link del **frontend** y registrar un nuevo usuario o ingresar con alguno de los que ya están creados (tabla presente al final de la sección).

Una partida del juego comenzará solo si hay 3 jugadores que hayan ingresado. De lo contrario se desplegará un mensaje explicitando el estado de la partida (si ya comenzó o no). En los links mencionados anteriormente ya se encuentra una partida en curso, con los 3 jugadores de la tabla que están en la partida.

Para jugar, puede hacer una jugada con cada jugador (de ataque y/o reordenamiento), y pulsar el botón *Enviar jugada*. Con ello el servidor recibirá la jugada realizada, y podrá dirimir el resultado de un turno cuando este finalice.

El juego seguirá de esa misma forma hasta que haya un ganador. Una vez que haya un ganador (algún jugador completó su misión secreta), se desplegará un mensaje en la pantalla indicando al ganador y se redirigirá hacia la vista de Login. Si quiere jugar una partida nueva, podrá en ese momento repetir lo el proceso recién descrito. (Login denuevo con 3 jugadores, etc.)

| Nombre                | Email       | Clave |  estaEnPartida|
|:--------------------- |:-------------|:-------------|:--------|
| José | jose@uc.cl | 123 | true|
| Vicente | vicente@uc.cl | 123 | true|
| goni | gtvargas@uc.cl | goni | true|
| Admin | admin@uc.cl | 123| false |
| Prueba | prueba@uc.cl | 123 | false|


## Respecto a la tarea 6

### Dashboard

Se creó la vista estadisticas, donde se pueden observar los mejores 5 jugadores en cada una de las categorías. Esta vista esta liberada para cualquier persona, es decir, no es necesario iniciar sesión.


### Tropas extra
Se agrego una repartición de tropas aleatorias a lo largo de todos los territorios, por lo tanto ahora se entregarán entre 0 y 4 tropas a todos los territorios despues de cada turno (En caso de que envies tropas al ataque y al siguiente turno tengas la misma cantidad, probablemente es por esta caracteristica).
Esto se agrego por que no habia forma de conseguir tropas nuevas antes de esto.


## Sobre el modelo de datos
La base de datos de la aplicación se basa en el modelo presente en el repositorio del frontend: https://github.com/PUCIIC2513/2020-2-G21-Webirra. El diagrama se encuentra especificamente en documents/diagrama_RISK.pdf.\
En la base de datos se crean los modelos de todas las clases del diagrama, junto con sus respectivas asociaciones.\
También, se ejecutan *seeders* de Territorios, Zonas y Misiones.\
A medida que se prueba la aplicación con lo descrito en la sección **Como ejecutar la aplicación**, también se van agregando datos a la base de datos, como nuevos estados del tablero, nuevas jugadas que envían los jugadores, o nuevos jugadores que realizaron login exitoso.

### Mejoras respecto a la usabilidad

- Se agrega una sección de 'modo de juego'. En ella se muestra cual es el estado de la partida para guiar al usuario durante ella

- No se permite al ingreso a la zona de juego sin estar previamente logeado. En este caso se redirecciona a la página de login.

- Al seleccionar atacar se visualizan sólo los territorios atacables en vez de todos los del juego.

- Dentro de la zona de los objetivos se muestra un híperlink que redirecciona a la página de instrucciones donde se explica que territorios corresponden a cada zona.

### Sobre el diagrama de datos

- Se actualiza el diagrama con los nuevos cambios a la base de datos relacionados con el dashboard de estadísticas.

## El servidor
Es una aplicación de Node.js, que funcionará como el backend del juego Risk, cuya descripción se encuentra en
https://github.com/PUCIIC2513/2020-2-G21-Webirra-backend.\

## Con respecto al término de un turno
Se implementó que el turno termina de manera automática cuando pasan una de estas cosas: pasan 5 minutos desde que comenzó el turno, o los 3 jugadores ya enviaron una jugada. Esto se informa en la vista con un mensaje de alerta. Si se logra pasar el turno, para ver el nuevo estado del tablero se debe actualizar la página. (Si se quiere cambiar la duración del turno, se debe ingresar la ruta *jugada* presente en el **backend**, en la carpeta /routes, y cambiar en la línea 59 el 5 por la cantidad de minutos que quieres que dure el turno).
