# Grupo 21 "Webirra"
### PUC IIC2513 - Tecnologías y Aplicaciones Web - Repositorio del Backend del Proyecto de Curso
## Integrantes

| Nombre                | Email       | Usuario de Github |
|:--------------------- |:-------------|:-------------|
| José Baboun | jibaboun@uc.cl | [@josebaboun](https://www.github.com/josebaboun) |
| Vicente Espinosa | vnespinosa@uc.cl | [@vnespinosa](https://www.github.com/vnespinosa) |
| Gonzalo Vargas | gtvargas@uc.cl | [@gtvargas](https://www.github.com/gtvargas) |

## El servidor
Es una aplicación de Node.js, que funcionará como el backend del juego Risk, cuya descripción se encuentra en
https://github.com/PUCIIC2513/2020-2-G21-Webirra.\

## Tecnologías empleadas
-El manejador de paquetes utilizado es *Yarn*.\
-El ORM para manejar la base de datos es *Sequelize*.\
-Para encriptar las claves se utiliza *bcrypt*.\
-Se utiliza el framework *Koa*, junto a *Koa-body*, *Koa-session*, *Koa router*.\
-La base de datos es de *Postgres*

## ¿Cómo ejecutar la aplicación?

Para probar la aplicación hay 2 opciones:\
-Acceder vía heroku a este link: https://aqueous-taiga-27569.herokuapp.com.
-Correr en el directorio de la aplicación *yarn install* y *yarn start*. Cabe mencionar que para esta opción se deben modificar las variables de el archivo *config.js*, que se encuentra en la carpeta *config*, con la informacion que corresponda a su usuario postgres/  
Si se sigue esta opción, se deben correr también los comandos: *yarn sequelize db:create*,
*yarn sequelize db:migrate*, *yarn sequelize db:seed:all*.

## Sobre el modelo de datos
La base de datos de la aplicación se basa en el modelo presente en el repositorio del frontend: https://github.com/PUCIIC2513/2020-2-G21-Webirra. El diagrama se encuentra especificamente en documents/diagrama_RISK.pdf.\
En la base de datos se crean los modelos de todas las clases del diagrama, junto con sus respectivas asociaciones.\
También, se ejecutan *seeders* de Territorios, Zonas y Misiones.\
A medida que se prueba la aplicación con lo descrito en la siguiente sección, también se van agregando datos a la base de datos, como nuevos estados del tablero, nuevas jugadas que envían los jugadores, o nuevos jugadores que realizaron login exitoso.


## Para probar la aplicación y requerimientos


**Link app Heroku:**

https://aqueous-taiga-27569.herokuapp.com


## Sobre las rutas

- Todos los inputs son en formato JSON
- Para probar las rutas se recomienda el uso de Postman
- Hay muchos a los cuales no se les revisa su validez, pues esta es hecha por el lado de usauario. Solamente se revisa login.

### POST

**/register**: En esta ruta se puede crear un nuevo usuario, se debe ingresar un body con la siguiente información: *mail*, *username* y *password*. La respuesta a este POST se muestra en la consola, y da informacion sobre si el registro fue existoso o no.


**/login**: Esta ruta usa los inputs *mail* y *password*. Devuelve respuestas sobre si el login funciono o no en la consola.

### GET

**/jugada**: Esta ruta genera la respuesta del servidor usando los inputs de los 3 jugadores y el estado actual del tablero, no recibe ningun input para cargarlo, pues todos los datos estan en la BDD o en los archivos en *data* (se pueden editar estos archivos para crear nuevas respuestas del servidor, el unico que no se debe editar es 'base.json'). 
Cuando se genera una respuesta del servidor, esta se guarda en la BDD, y dado que la jugada se genera a partir del ultimo estado del tablero, esto afectará el resultado de esta ruta (es decir, cada vez que se ejecuta, se va acumulando el resultado, y como solo salen tropas por ahora, se pueden llegar a numeros negativos, para cambiar el tablero se puede usar la ruta **/crear**). Retorna como queda el tablero luego de procesar las jugadas en Postman.

**/crear**: Crea un nuevo tablero de manera aleatoria, esto afecta la ruta jugada. Retorna en Postman el nuevo tablero creado. No recibe inputs


**/estado**: Esta sería la ruta que piden los usuarios para cargar su mapa, pues retorna el ultimo estado del tablero. Retorna el tablero en Postman.

