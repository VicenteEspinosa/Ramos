# Readme Entrega 4 grupo 96 y 103

## Rutas tipo GET

### Rutas básicas

falta

### Rutas de búsqueda por texto

Supuestos: para la búsqueda de mensajes sólo nos entregarán un id como int y ese id corresponde al sender.

Cuando se ingresan los datos de desired o required, el text search se realiza mediante querys de mongo. Si además se ingresa un id, se realiza una query con el método $and para buscar mensajes que cumplan con los campos de "desired" o "required (y "forbidden" si fue ingresado) además de que su id sea el ingresado en la request.

Si no se ingresa en la request los campos de "desired" y "required", existen tres tipos de búsqueda. El primer tipo de búsqueda se utiliza cuando sólo se ingresa id, y se buscan los mensajes correspondientes a ese id a través de una query. En cambio, si sólo se ingresa el campo "forbidden", se obtienen todos los mensajes de la bd a través de una query y luego se remueven de la lista obtenida aquellos mensajes que contegan las palabras de la request. Por último, si se ingresan los campos "forbidden" y "userId", se obtienen todos los mensajes correspondientes al usuario de id especificado a través de una query y se remueven de esa lista los mensajes que contengan las palabras del campo "forbidden".

### Ruta de tipo POST
La ruta para la funcion create_message(), recibe los atributos desde un json como se inidca en la pauta. 
Luego atraves de un if se verifica que todas las variables efectivamente existan, en caso contrario se envia un mensaje que no se puede crear el mensaje. Si todo calsa se le asigna un valor random en un rango de 10000 dentro de un ciclo while hasta que sea distinto a cualquier mid de mensjes ya creados. Si el mid coincide con ser unico, se crea el mid y se procede a insertar el mesaje en la base de datos. 

### Ruta de tipo DELETE

Se realiza una query que busca el mensaje que tenga el campo "mid" igual al id especificado en la ruta. Luego, si el resultado de la query es no vacío, se elimina el mensaje de la base de datos y se muestra un mensaje que le notifica al usuario que ha sido eliminado. Si la búsqueda del mensaje con el id especificado no retorna un resultado, se le notifica al usuario a través de un mensaje en pantalla que el mensaje que está tratando borrar no existe.



### Instrucciones para correr la API

Luego de descomprimir la carpeta API.zip, se debe ingresar al terminal del computador y posicionarse en el path en el que se encuentran estos archivos. Posicionados en la carpeta en la que están los archivos main.py, Pipfile, Pipfile.lock, se debe ingresar al entorno vistual corriendo:
```
pip install pipenv
```
```
pipenv install
```
```
pipenv shell
```
```
python main.py
```
Para probar la API se utilizó Postman, donde las primeras rutas hasta /text-search son de tipo GET, luego  /messages tipo POST para agregar mensajes y, por último, /message/:id tipo DELETE que borra el mensaje de id ingresado.
