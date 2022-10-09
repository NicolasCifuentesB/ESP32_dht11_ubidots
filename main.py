import censado
import ubidots
import wifi
from machine import Pin

boton = Pin(5,Pin.IN,Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)
sensor = 15
ubidots_token = 'Ubidots token'

print('------ iniciado ------')
while wifi.station.isconnected() :
    estado_btn = boton.value()
    if estado_btn and censado.revision(sensor) :
        led.on()
        ubidots.upload(censado.temperatura(sensor), ubidots_token)
    elif not estado_btn and censado.revision(sensor) :
        led.off()
    else :
        print('Error en lectura')