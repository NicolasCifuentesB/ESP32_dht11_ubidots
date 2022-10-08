from machine import Pin
import time
import censado

boton = Pin(5,Pin.IN,Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)
sensor = 15

print('INICIADO')

while True :
    estado_btn = boton.value()
    if estado_btn and censado.revision(sensor) :
        led.on()
        print('Temperatura: {}'.format(censado.temperatura(sensor)))
    elif not estado_btn and censado.revision(sensor) :
        led.off()
        # print(estado_btn)
    else :
        print('Error en lectura')
