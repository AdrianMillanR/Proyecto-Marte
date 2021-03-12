# Proyecto Marte
Tendrán que realizar un programa en Python que simule la exploración del planeta Marte. El proyecto se realizará de forma **individual**. El diseño de la interface queda abierto a tu creatividad, sin embargo es necesario que el mapa, los recursos y los agentes sean visibles de alguna forma.

>La misión espacial Cerberus ha sido enviada a Marte para recoger muestras geológicas las cuales serán extraídas para su estudio en la tierra. Sin embargo este viaje no puede ser tripulado puesto que aun no se cuenta con la tecnología adecuada. Por esta razón se ha optado por utilizar robots para la extracción de los materiales geológicos. La nave espacial cuenta con 4 robots que tienen la forma de pequeños carros, cuyas llantas les permitirá moverse a través del terreno inhóspito de Marte.

>Se te ha solicitado realizar la programación de los robots (agentes), para ello mostrarás una simulación de su funcionamiento, para después ser implementada en los robots. Los agentes saldrán de la nave y no tendrán conocimiento alguno del terreno que están explorando. Por ello tendrán que moverse en diferentes direcciones y explorar.

#### Para la facilidad del desarrollo de este prototipo se cuentan con las siguientes reglas:
* Los agentes solo se pueden mover en 4 direcciones (norte, sur, este y oeste)
* Los recursos pueden variar de tamaño (1 a 5 unidades)
* Los agentes solo pueden cargar 1 unidad a la vez
* La nave terminará su misión cuando tenga 25 unidades. En este momento
todos los agentes deberán regresar a la nave para preparar el regreso a la
tierra.
* El diseño inicial del mapa donde los agentes se moverán, queda abierto a tu discreción

#### Para implementar el algoritmo se ha propuesto separar su desarrollo en diferentes fases
1. **Comportamiento reactivo**
En esta primera fase los agentes no tendrán conocimiento de los otros agentes, y realmente no serán inteligentes. Ellos se moverán en una dirección que previamente no hayan explorado. Si encuentran un obstáculo se moverán en una dirección diferente de forma aleatoria.
Si encuentran un recurso, recogerán el recurso y regresarán a la nave para depositarlo.
Si el recurso contaba con más unidades, el agente regresará a recogerlas.
El agente deberá ir almacenando el conocimiento del mapa que haya explorado, de esta forma sabrá donde están los obstáculos y en qué dirección no ha explorado.

1. **Comportamiento colaborativo - mapa**
En esta fase los agentes compartirán el conocimiento adquirido del mapa con el resto de los agentes. De esta forma los agentes compartirán el conocimiento que han adquirido conforme han explorado la superficie del planeta.

1. **Comportamiento colaborativo – inteligencia**
En esta fase un agente que encuentre un recurso que sea muy grande (mayor a 2) puede pedir ayuda a otros agentes libres para que lo puedan ayudar a recoger el recurso. Un agente libre es aquel agente que no se encuentra actualmente cargando un recurso o no se encuentra en camino a ayudar a un agente.

#### El proyecto se evaluará en base a la siguiente rúbrica:
* Los agentes se pueden mover sobre el mapa diseñado por el alumno **(10
puntos)**
* En la fase reactiva, los agentes se mueven de forma aleatoria en una dirección
no explorada **(10 puntos)**
* En la fase reactiva, los agentes eligen una dirección diferente para moverse
cuando encuentran un obstáculo. Adicionalmente los agentes no pueden
moverse a través de un obstáculo **(10 puntos)**
 En la fase reactiva, los agentes realizan un mapa de forma individual del
terreno que han explorado **(10 puntos)**
* En la fase reactiva, el agente es capaz de recoger un recurso del mapa y
regresar a la nave con el **(10 puntos)**
* En la fase reactiva, si el agente no pudo terminar de recoger un recurso, el
agente regresará a recoger el resto **(10 puntos)**
* En la fase colaborativa, el agente podrá compartir su conocimiento del mapa
con el resto de los agentes conforme va explorando **(15 puntos)**
* En la fase colaborativa, el agente podrá solicitar ayuda a otros agentes libres
cuando encuentre un recurso grande **(15 puntos)**
* Cuando la nave espacial llega a su límite, todos los agentes deberán regresar a
la nave espacial **(10 puntos)**