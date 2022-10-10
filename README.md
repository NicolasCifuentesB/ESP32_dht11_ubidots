# Envio DHT11 a ubidots por pulsador con ESP32
El presente repositorio tiene como finalidad realizar el envio de la temperatura detectada por un sensor DHT11 a un dashboard de ubidots al hacer uso de un pulsador, esto gracias al microcontrolador ESP32 y el lenguaje micropython para el mismo.

## Instalación micropython en ESP32
En primer lugar es necesario preparar el microcontrolador para que pueda hacer uso de micropython siguiendo los siguientes pasos:
1. Descargar el firmware en https://micropython.org/download/#esp32.
2. Realizar los siguientes comandos en terminal para instalar el firmware de micropython:

Herramienta para poder escribir el firmware en el microcontrolador.

`pip install esptool`

Borrar la memora flash del microcontrolador.

`esptool.py --port 'Nombre del puerto' erase_flash`

Instalar en el microcontrolador el archivo *.bin* descargado en el iteral anterior.

`esptool.py --chip esp32 --port 'Nombre del puerto' -z 0x1000 esp32-20180511-v1.9.4.bin`

3. Realizar los siguientes comandos en terminal para instalar la terminal con la cual interactuar con la placa

Instalar el serial de interacción con la placa

`pip install adafruit-ampy`

Apreciar comandos de funcionamiento para *ampy*

`ampy --help`

## Cargar de módulos en la placa
Una vez preparado el microcontrolador es necesario guardar en su memoria los archivos que hacen de modulos para la práctica, siendo estos: censado para el DHT11, carga de datos al servidor y conexión a red wifi. Para esto se llevan a cabo los siguientes comandos.

`ampy -p 'Nombre del puerto' put censado.py`

`ampy -p 'Nombre del puerto' put ubidots.py`

`ampy -p 'Nombre del puerto' put wifi.py`

## Orden de ejecución y montaje
Una vez cargados los módulos es necesario seguir el siguiente proceso de montaje y compilación. En el diagrama presente a continuación se aprecia las conexiones fisicas necesarias.

![esquematico](/img/Conexion_Fisica.png)

En el siguiente diagrama se presenta el circuito esquemático para una mayor claridad sobre las conexiones. Siguiendo con las lineas de compilación.

![circuito](/img/Schematic_esp32_ubidots_dth11.png)

Conexión a la red wifi, es importante modificar el nombre de la red y la contraseña en el módulo *wifi.py*

`ampy -p 'Nombre del puerto' run wifi.py`

Ejecución del programa principal.

`ampy -p 'Nombre del puerto' run main.py`

Finalmente en la plataforma de ubidots se creara el dispositivo y la variable correspondiente a la cual crearle dashboards. Para este caso se uso termometro y gráfica tal como se ve a continuacion.

![dashboards](/img/dashboards.png)
