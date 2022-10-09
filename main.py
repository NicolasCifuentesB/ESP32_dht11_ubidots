import censado
import ubidots
import wifi # Necesario ejecutar primero este modulo para conectarse a la red
from machine import Pin

boton = Pin(5,Pin.IN,Pin.PULL_DOWN) # Pin para el pulsador
led = Pin(2, Pin.OUT) # Pin para el led interno
sensor = 15 # Pin para el sensor
ubidots_token = 'Ubidots token' # Ubidots token: Token asigando en la plataforma ubidtos

print('------ iniciado ------')
while wifi.station.isconnected() : # Mientras se este conectado a la red
    estado_btn = boton.value() # Verifica el estado del pulsador
    if estado_btn and censado.revision(sensor) : # Pulsador activado y sensor funcionando
        led.on() # Enciende el led interno
        ubidots.upload(censado.temperatura(sensor), ubidots_token) # Inicia la subidad de datos de temperatura
    elif not estado_btn and censado.revision(sensor) : # Pulsador desactivo y sensor funcionando
        led.off() # Apaga el led
    else :
        print('Error en lectura')