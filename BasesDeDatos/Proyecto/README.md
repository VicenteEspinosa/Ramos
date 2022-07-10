# Readme Entrega 5 grupo 96 y 103



### Detalles

- Para el text search, para permitir el uso de comas y facilitar el trabajo, se deben separar las palabras/frases con un ' ; '.

### MAPA

Para visualizar el mapa se realizo un request del tipo get a la [API](https://e5grupo96.herokuapp.com/) realizada en la entrega 4. Se recuperaron todos los mensajes. Para trabajar la respuesta obtenida, se transformo el string a un JSON-ARRAY obteniendo todos los mensajes. Se filtraron todos los mensajes de acuerdo al id del "sender" y que fuese creado dentro de los rangos de fechas estipulados. 
Una vez hecho ese filtro, se almacenaron las coordenadas del mensaje en un arreglo para luego visualizarlas en un mapa obtenido de la API LeafletJS como fue mostrado en ayudantía.

### Crear Mensaje

A traves de un json se ven todos los usuarios dentro del sistema, el cual entrega un string. Este es convertido en array segun cada usuario y luego se procede a buscar el username del destinatario entregado por el usuario. Si este existe, se procede a crear el mensaje con el id de ambos usuarios, el cntenido, se entregan coordenadas aleatorias y fehca fija. Esto conectando con la funcion de la entrega anterior.

### Mensajes recibidos

A traves de un proceso muy silimar al de crear mensaje, a traves de un json buscamos todos los mensajes, y luego se filtran aquellos que su receptant id corresponda al del usario de la sesion.

### Mensajes Enviados

Se utiliza el echo de que en text search se puede buscar por usuario que envio mensaje, entonces se hace un proceso igual al de *text-search* pero solo filtando por usuario.

### Text-Search

Se utilizan los filtros que se solicitan en la vista anterior, se envian a la api indicada más arriba, y se procesa la respuesta de este y se agrega a una tabla para ordenar y presentar de mejor manera la informacion.


### Instrucciones para revisar la entrega

Se puede correr de forma local un php localhost desde la carpeta ```app```, dentro de la carpeta ```Entrega5```, y luego, desde index se debe indicar el usuario que se utilizara. Luego se redireccionara a un menu en el cual hay un boton claramente indicando cual lleva a cada consulta solicitada.

Otra opción mucho mas facil es probarlo en la siguiente pagina:
```
http://codd.ing.puc.cl/~grupo96/index.php
```
