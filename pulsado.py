from machine import Pin
import time

boton = Pin(5,Pin.IN,Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

while True :
    estado_btn = boton.value()
    if estado_btn :
        led.on()
    else :
        led.off()    
    print(estado_btn)