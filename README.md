# Como clonar solo una carpeta

Es mejor clonar solo una carpeta si se va a usar solo esta, ya que el repositorio es bastante grande.

Escoge una carpeta y el nombre de esta sera tu \<folder_name>

**Se requiere git >= 2.25.0**

```console
git clone --filter=blob:none --no-checkout https://github.com/VicenteEspinosa/Ramos.git <folder_name>
```

```console
cd <folder_name>
```

```console
git sparse-checkout set <folder_name>/ 
```

```console
git checkout main
```

Fuente: https://github.blog/2020-01-17-bring-your-monorepo-down-to-size-with-sparse-checkout/ 


# Ramos ordenados cronologicamente

- 2017-2
  * [Introducción a la Programación \[IIC1103\]]

- 2019-2
  * [Programación Avanzada \[IIC2233\]]

- 2020-1
  * [Matemáticas Discretas \[IIC1253\]]
  * [Ingeniería de Software \[IIC2143\]]
  * [Bases de Datos \[IIC2413\]]

- 2020-2
  * [Tecnologías y Aplicaciones Web \[IIC2513\]]

- 2021-1
  * [Estructuras de Datos y Algoritmos \[IIC2133\]]
  * [Proyecto de Especialidad \[IIC2154\]]

- 2021-2
  * [Sistemas Operativos y Redes \[IIC2333\]]
  * [Arquitectura de Computadores \[IIC2343\]]
  
- 2022-1
  * [Arquitectura de Sistemas de Software \[IIC2173\]]
  * [Taller de Integracion \[IIC3103\]]
  * [Diseño Detallado de Software \[IIC2113\]]
  * [Desarrollo de Software \[IIC3143\]]

- 2022-2
  * [Gestion De Proyectos De Tecnologias De Informacion \[IIC3113\]]


# Ramos ordenados por tecnologías usadas

## **Python**  <img src="icons/python.png" alt="python" width="20"/>

  * [Introducción a la Programación \[IIC1103\]]

  * [Programación Avanzada \[IIC2233\]]

  * [Gestion De Proyectos De Tecnologias De Informacion \[IIC3113\]]

  * ### Django <img src="icons/django.png" alt="django" width="15"/> 

    - [Proyecto de Especialidad \[IIC2154\]]

    - [Desarrollo de Software \[IIC3143\]]


## **Ruby** <img src="icons/ruby.png" alt="ruby" width="20"/>

  * Ruby On Rails <img src="icons/rails.png" alt="ruby" width="20"/>

    - [Ingeniería de Software \[IIC2143\]]

    - [Arquitectura de Sistemas de Software \[IIC2173\]]

    - [Taller de Integracion \[IIC3103\]]

    - [Diseño Detallado de Software \[IIC2113\]]

## **Javascript** <img src="icons/javascript.png" alt="javascript" width="20"/>

  * [Tecnologías y Aplicaciones Web \[IIC2513\]]

  * ### React <img src="icons/react.png" alt="react" width="20"/> 

    - [Arquitectura de Sistemas de Software \[IIC2173\]]

    - [Taller de Integracion \[IIC3103\]]

    - [Diseño Detallado de Software \[IIC2113\]]

    - [Desarrollo de Software \[IIC3143\]]

  * ### Next <img src="icons/next.png" alt="next" width="20"/>

    - [Desarrollo de Software \[IIC3143\]]

    - [Gestion De Proyectos De Tecnologias De Informacion \[IIC3113\]]

  * ### Node <img src="icons/node.svg" alt="node" width="20"/>

    - [Arquitectura de Sistemas de Software \[IIC2173\]]

    - [Taller de Integracion \[IIC3103\]]

## **Typescript** <img src="icons/typescript.png" alt="typescript" width="20"/>

  - [Desarrollo de Software \[IIC3143\]]


## **C** <img src="icons/c.png" alt="c" width="25"/>

  * [Sistemas Operativos y Redes \[IIC2333\]]

  * [Estructuras de Datos y Algoritmos \[IIC2133\]]


## **Risk-V (assembly)** <img src="icons/risk-v.png" alt="risk" width="20"/>

  * [Arquitectura de Computadores \[IIC2343\]]


## **Docker** <img src="icons/docker.png" alt="docker" width="50"/>

  * [Proyecto de Especialidad \[IIC2154\]]

  * [Arquitectura de Sistemas de Software \[IIC2173\]]

  * [Desarrollo de Software \[IIC3143\]]


## **Teorico**

  * [Matemáticas Discretas \[IIC1253\]]

  * [Bases de Datos \[IIC2413\]]


<!-- Links -->

[Arquitectura de Computadores \[IIC2343\]]: ./ArquitecturaDeComputadores

[Arquitectura de Sistemas de Software \[IIC2173\]]: ./ArquitecturaDeSistemasDeSoftware

[Bases de Datos \[IIC2413\]]: ./BasesDeDatos

[Desarrollo de Software \[IIC3143\]]: ./DesarrolloDeSoftware

[Diseño Detallado de Software \[IIC2113\]]: ./DisenoDetalladoDeSoftware

[Estructuras de Datos y Algoritmos \[IIC2133\]]: ./EstructurasDeDatosYAlgoritmos

[Gestion De Proyectos De Tecnologias De Informacion \[IIC3113\]]: ./GestionDeProyectosDeTecnologiasDeInformacion

[Ingeniería de Software \[IIC2143\]]: ./IngenieriaDeSotfware

[Introducción a la Programación \[IIC1103\]]: ./IntroduccionALaProgramacion

[Matemáticas Discretas \[IIC1253\]]: ./MatematicasDiscretas

[Programación Avanzada \[IIC2233\]]: ./ProgramacionAvanzada

[Proyecto de Especialidad \[IIC2154\]]: ./ProyectoDeEspecialidad

[Sistemas Operativos y Redes \[IIC2333\]]: ./SistemasOperativosYRedes

[Taller de Integracion \[IIC3103\]]: ./TallerDeIntegracion

[Tecnologías y Aplicaciones Web \[IIC2513\]]: ./TecnologiasYAplicacionesWeb
