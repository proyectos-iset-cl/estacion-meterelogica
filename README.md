# estacion-meterelogica
Codigos relacionados  al proyecto de Estacion metereologica de  ISET-CL

Codigos relacionados al proyecto de Estacion Metereologica de ISET-CL Codigos del proyecto estudiantil de Estacion de Sondeo Climatico en Casa libertad. Aqui se encuentran algunos de los codigos implementados tanto para el manejo de los sensores como de la interfaz de software que se usara para leer los datos. La red esta compuesta de nodo Xbee como enlaces de radio y de tarjetas Arduino para leer y dar formato a los datos recuperados. Los sensores son el DHT22 para la lectura de humedad ambiental y temperatura, MQ-131 para lectura de niveles de Ozono, y un sensor de radiacion UV. El nodo coordinador de la red se encarga de entregar a una tarjeta Raspberry Pi 3 los datos recabados y posteriormente se realiza su publiacion en Twitter.

La programacion en la Raspberry Pi 3 se hace en Python 2, para la lectura de los valores, identificacion del sensor que provienen y procesamiento. Esto con la finalidad de poder entregar a los scripts en Python los datos necesarios para generar graficas con la herramienta rrdtool y realizar su publicacion en Twitter.

Se pretende seguir ampliando el alcance de este proyecto para incluir sensores más robustos y poder medir otras variables como son presión atmosferica, dirección del viento, precipitación pluvial, entre otros.

