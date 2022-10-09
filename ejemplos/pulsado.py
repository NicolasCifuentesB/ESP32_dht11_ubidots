from machine import Pin
import censado

boton = Pin(5,Pin.IN,Pin.PULL_DOWN) # Pin para del pulsador
led = Pin(2, Pin.OUT) # Pin interno a iluminar
sensor = 15 # Pin de lectura para el sensor deht11

print('INICIADO')

while True :
    estado_btn = boton.value() # Verifica el estado del pulsador
    if estado_btn and censado.revision(sensor) : # Pulsador activado y sensor funcionando
        led.on() # Enciende el led interno
        print('Temperatura: {}'.format(censado.temperatura(sensor))) # Imprime la temperatura
    elif not estado_btn and censado.revision(sensor) : # Pulsador desactivado y sensor funcionando
        led.off() # Apaga el led
    else :
        print('Error en lectura')
