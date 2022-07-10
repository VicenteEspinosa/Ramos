# URL app

[https://www.grupo1.ml](https://www.grupo1.ml)

# Conectarse a EC2

```console
ssh -i ~/.ssh/{llaveEntregada} ubuntu@www.grupo1.ml
```


# Como correr la aplicación

## Local

Simplemente hay que correr los comandos 
```console
docker-compose build 
docker-compose up
``` 
ó
```console
docker compose build
docker compose up 
``` 

en la consola ubicandose en la carpeta principal [e1-2022-1-grupo_01](.)


## Usar la app

Si todo funcionó correctamente el frontend de la app debería poder verse al acceder a [localhost](http://localhost) (sin indicar puerto)

## Producción

Para producción los comandos a correr son:
```console
docker compose -f docker-compose.production.yml build 
docker compose -f docker-compose.production.yml up 
```


## Replicar CI/CD

El CI está implementado en cada push, por lo que basta con crear cualquier rama desde y hacer un push a esta para gatillar el proceso en CircleCI. Este proceso crea una imagen de ruby en docker, y corre el servidor de backend para luego ejecutar la función de testing que viene con rails. Si no hay errores se marcará como correcto, sino el push sera marcado como fallido.

El CD solo se activa con un push a la rama `master`. Al hacer un push se activará primero el CI, y si es que este es exitoso se correrá el CD, que hará deploy de los nuevos cambios en el servidor.

Los detalles de la configuración se pueden ver en el archivo [config.yml](./.circleci/config.yml) ubicado en la carpeta `.circleci`

## Información importante sobre la app

### IDs usables para probar funcionalidad

Ya que no se hicieron todas las funcionalidades no hay forma facil de encontrar el id de los usuarios, por eso se entregan los siguientes usuarios y sus ids para facilitar la revisión:


| Id    | Usuario|
|---|---|
| 1 | Vicente |
| 2 | alericok10 |
| 3 | alericoj10 |


También, se puede acceder a https://www.grupo1.ml/api/v1/users para ver el listado de usuarios con sus ids actualizado

### Cantiadad máxima de usuarios a buscar

A pesar de que se pueden escribir infinitos ids de usuarios, solamente se buscarán los primeros 5, incluyendo los incorrectos (no es un id existente), es decir, si se ingresan 4 ids correctos, luego uno incorrecto y al final uno correcto, solamente se retornaran los primeros 4.

### Input de ids usuarios

Hay que escribir los ids de los usuarios seprados por coma, no es importante si hay o no espacios entre estos.
