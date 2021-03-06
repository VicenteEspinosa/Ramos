# Como obtener el _commit_

Para identificar un _commit_, usaremos el SHA-1 _checksum_ de dicho _commit_, también conocido como _HASH_ de _commit_. Para obtener este _HASH_, puedes revisar GitHub o usar el comando `git log` en consola. A continuación mostraremos ambas formas. 

## Desde la página web de GitHub:

Para este ejemplo usaremos el syllabus del curso y obtendremos el _HASH_ del último _commit_.

Pasos:

1. Ir a su repositorio privado. Luego hacer click en _commits_ (cuadro encerrado en magenta).

![image](https://user-images.githubusercontent.com/15641721/55690164-d57ac680-595b-11e9-967c-f80aabeaf25a.png)

2. Luego deberán buscar el _commit_ que quieren (según el mensaje que usaron en `git commit -m "MENSAJE"` y hacer click en el ícono encerrado en magenta.

![image](https://user-images.githubusercontent.com/15641721/55690175-fb07d000-595b-11e9-8749-7c99d338ab81.png)

Eso dejará en el portapapeleres el _HASH_ asociado a dicho _commit_, el cual lo pueden pegar en cualquier parte con CONTROL + V o CMD + V.

En este caso, el HASH sería: `4303626234eddf24a5a73e794f6c7ccd087f9564`

## Desde consola

Luego de hacer `git push` de un _commit_. Ejecutar el comando:`git log` en consola dentro de su repositorio. 
Les saldrá una tabla como la siguiente: (Ejemplo tomado del syllabus)

![image](https://user-images.githubusercontent.com/15641721/55690250-a9ac1080-595c-11e9-9cd9-08fc76f530eb.png)

Con ese comando les aparecerá una lista de los últimos _commits_ del repositorio, con detalles de cada uno:

- _HASH_ (texto en amarillo). 
- Autor.
- Hora del _commit_ .
- Mensaje.


Para ver un _commit_ más antiguo deben oprimir ENTER o la flecha hacia abajo. Cuando encuentren el _commit_ adecuado, con el mouse seleccionan el _HASH_ y hacen CONTROL + C o CMD + C, luego pegan el _HASH_ donde quieran con CONTROL + V o CMD + V.


Más información en este link: https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History.



