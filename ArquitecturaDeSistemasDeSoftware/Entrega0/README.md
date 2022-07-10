# Tareas completadas

Se completaron todas menos PostGis y la confirmación de correo

## Comentarios

- Para crear un usuario deben hacer click en registrarse y luego inicar sesión.
- Para crear ubicaciones deben hacer click en donde quieren agregar la ubicación o pueden hacer click en cualquier parte e ingresar las coordenadas.
- Para hacer ping a un usuario deben hacer click primero en una ubicación de este usuario.

## URL

https://www.vicenteespinosa.tk/

## Ingresar al servidor

La ip elastica es `34.204.30.199`, por lo tanto para conectarse es:

`ssh -i ~/.ssh/arquiSoftwareE0.pem ubuntu@ec2-34-204-30-199.compute-1.amazonaws.com`

con la llave entregada por canvas

## Credenciales IAM 

Las credenciales entregadas en el .csv deberian tener permiso para todo.


## Contacto

Si hay algun problema con la tarea me pueden contactar en vnepinosa@uc.cl o @VicenteEspinosa en telegram.

## Levantar la app

Toda la app se levanta solo corriendo `sudo docker-compose up` al ubicarse dentro de la carpeta de este repositorio
