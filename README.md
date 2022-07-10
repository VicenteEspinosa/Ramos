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


# Ramos ordenados por tecnologías usadas

## **Python**  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="python" width="20"/>

  * [Introducción a la Programación \[IIC1103\]]

  * [Programación Avanzada \[IIC2233\]]

  * ### Django <img src="https://seeklogo.com/images/D/django-logo-F46C1DD95E-seeklogo.com.png" alt="django" width="15"/> 
  

    - [Proyecto de Especialidad \[IIC2154\]]

    - [Desarrollo de Software \[IIC3143\]]
  
  



## **Ruby** <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Ruby_logo.svg/1200px-Ruby_logo.svg.png" alt="ruby" width="20"/>

  

  * Ruby On Rails <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Ruby_On_Rails_Logo.svg/1200px-Ruby_On_Rails_Logo.svg.png" alt="ruby" width="20"/>

  

    - [Ingeniería de Software \[IIC2143\]]

    - [Arquitectura de Sistemas de Software \[IIC2173\]]

    - [Taller de Integracion \[IIC3103\]]

    - [Diseño Detallado de Software \[IIC2113\]]

  

  

## **Javascript** <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png" alt="javascript" width="20"/>



  * [Tecnologías y Aplicaciones Web \[IIC2513\]]

  * ### React <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/React.svg/800px-React.svg.png" alt="react" width="20"/> 


    - [Arquitectura de Sistemas de Software \[IIC2173\]]

    - [Taller de Integracion \[IIC3103\]]

    - [Diseño Detallado de Software \[IIC2113\]]

    - [Desarrollo de Software \[IIC3143\]]


  * ### Next <img src="https://seeklogo.com/images/N/next-js-logo-8FCFF51DD2-seeklogo.com.png" alt="next" width="20"/>

    - [Desarrollo de Software \[IIC3143\]]


  * ### Node <img src="https://assets.zabbix.com/img/brands/nodejs.svg" alt="node" width="20"/>



    - [Arquitectura de Sistemas de Software \[IIC2173\]]

    - [Taller de Integracion \[IIC3103\]]



## **C** <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/archive/3/35/20190417225046%21The_C_Programming_Language_logo.svg/120px-The_C_Programming_Language_logo.svg.png" alt="c" width="25"/>


  * [Sistemas Operativos y Redes \[IIC2333\]]

  * [Estructuras de Datos y Algoritmos \[IIC2133\]]




## **Risk-V (assembly)** <img src="https://www.eetasia.com/wp-content/uploads/sites/2/2021/02/RISC-V-logo.jpg" alt="risk" width="20"/>


  * [Arquitectura de Computadores \[IIC2343\]]


## **Docker** <img src="https://d1.awsstatic.com/acs/characters/Logos/Docker-Logo_Horizontel_279x131.b8a5c41e56b77706656d61080f6a0217a3ba356d.png" alt="docker" width="50"/>

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

[Ingeniería de Software \[IIC2143\]]: ./IngenieriaDeSotfware

[Introducción a la Programación \[IIC1103\]]: ./IntroduccionALaProgramacion

[Matemáticas Discretas \[IIC1253\]]: ./MatematicasDiscretas

[Programación Avanzada \[IIC2233\]]: ./ProgramacionAvanzada

[Proyecto de Especialidad \[IIC2154\]]: ./ProyectoDeEspecialidad

[Sistemas Operativos y Redes \[IIC2333\]]: ./SistemasOperativosYRedes

[Taller de Integracion \[IIC3103\]]: ./TallerDeIntegracion

[Tecnologías y Aplicaciones Web \[IIC2513\]]: ./TecnologiasYAplicacionesWeb
