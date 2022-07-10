# Tarea 3 Sistemas Operativos y Redes

## Miembros

Vicente Espinosa: 17639247


Gonzalo Vargas: 17637120

## Consideraciones

- Para activar todas las configuraciones de los Home Routers se debe abrir cada uno y volver a guardar los cambios.
- Al principio cuando se intenta enviar un paquete, fallará al menos 2 veces en distintas ubicaciones pero a la tercera funciona como es deseado.
- A veces al abrir el programa, se cambia la configuracion de los Laptop y se pierde su IP estática, todos tienen su IP designada como una nota al lado de ellos.
- Se implementaron todas las configuraciones pedidas en el enunciado. Esto incluye que el firewall del servidor de Netflix bloquee las solicitudes que vengan desde la subred Eduroam, y que en la casa de Jorge entre las 22:00 y 23:00 hrs se bloquea Netflix (esta configuración se encuentra en el router de la casa de Jorge).

## Preguntas

1. ¿Cuál es el largo en bits de la dirección IP de destino?

La dirección IP de destino corresponde a 3.3.0.2, y tiene un largo de 32 bits. Esto, porque al analizar los detalles del Simple PDU enviado, se puede ver que la dirección ocupa un bloque completo el cual tiene un tamaño de 32 bits.

2. ¿Cuál es la dirección IP de origen cuando el paquete se encuentra en el router central y el último dispositivo
visitado es el router gateway de la red Eduroam?

La IP que aparece como origen en este momento es 172.67.7.2, la cual corresponde al Home Router de Eduroam. Esto se puede ver en el Panel de simulación, donde uno puede seleccionar un mensaje en un momento determinado, es decir, en este caso se está analizando el mensaje que está en el router central y viene del router gateaway de Eduroam.

3. ¿Cuál es la dirección IP de origen cuando el paquete se encuentra en el router central y el último dispositivo
visitado es el router gateway de la red DNS? 

Análogamente a la pregunta anterior, esta respuesta se encuentra directamente al analizar el Panel de simulación. El IP de origen en este caso es el 3.3.0.2, la cual corresponde a la IP del servidor DNS.

4. Describa, en orden y separado por capas de entrada y salida, todo lo que ocurre con el paquete cuando este se
encuentra en el servidor de la red DNS y el último dispositivo visitado es el router gateway de la red DNS.

Para la Capa 1 (Layer 1), se puede ver que no hay cambios entre la de Entrada y Salida, ya que ambas hacen referencia al Puerto de FastEthernet0. Para la Capa 2, se invierten las direcciones (Address) de origen y destino, los cuales se encuentran en los Headers. Por último, para la Capa 3, se invierten las direcciones de origen y destino (direcciones IP), y se ve que además de los Headers se cambia el ICMP Message Type desde 8 a 0.

5. ¿Cuál es el largo en bytes del HTTP Request del paquete HTTP? 

Al revisar en el Panel de Simulación (en la sección de Outbound PDU Details) el detalle del HTTP Request, se comprueba que ocupa un bloque entero de 32 bytes.

6. Describa que tipos de paquetes se están usando, es decir, decir que tipo de paquete son, por qué se usan estos
paquetes y que deben contener.

En primer lugar, se envía un paquete de tipo DNS al servidor DNS para conocer la dirección IP del servidor que corresponde a la URL www.netflix.com. Este paquete lleva el nombre de la URL (en la sección DNS Query) hacia el servidor DNS y luego trae el IP correspondiente hacia el cliente.
Luego, el cliente envía un paquete de tipo TCP hacia la dirección IP que le proporcionó el paquete DNS, con el fin de establecer una conexión para permitir el flujo de datos entre hosts. Este paquete contiene los puertos del host de destino y de origen que se usarán para el trasapaso de datos.
Finalmente, el cliente envía un paquete HTTP al servidor de Netflix. El paquete contiene tanto de ida como de vuelta las IP de origen y destino (Laptop Jorge y Netflix, y viceversa), y los puertos de origen y destino. También trae un bloque de HTTP request, el cual cuando va desde Netflix hacia Casa Jorge contiene el Html que se mostrará en el navegador.

7. Describa de forma ordenada que rutas toman los distintos paquetes (especificar por donde pasan y en que orden).

El primer paquete en viajar es el de tipo DNS, el cual va desde la casa de Jorge hasta el servidor DNS, ida y vuelta. Este, luego del cliente que manda la solicitud pasa por el router de la casa de Jorge, por el router gateaway de esta subred, después por el router central, luego se dirige al router getaway de la subred DNS, para finalmente pasar por un switch y llegar al servidor. En la vuelta, toma la misma secuencia de componentes, hasta llegar al cliente que hizo la solicitud (puede haber sido el computador, una de las laptops o el celular).
El segundo es el TCP, el cual va desde la Laptop De Jorge hacia su Home Router, luego esto se dirige a el Gateway de la Casa De Jorge, para despues pasar por el router central. Este después se dirige al Gateway de Netflix, pasa por el Switch y llega a el servidor de Netflix. Finalmente este paquete toma la misma ruta de vuelta.
El último paquete corresponde al de HTTP, que toma exactamente la misma ruta del TCP.