import censado

# Asignación del pin usado en la ESP32
pin = 15

if censado.revision(pin) : # Revisa el funcionamiento del sensor
    temp_1 = censado.temperatura(pin) # Envia la temperatura
    hum_1 = censado.humedad(pin) # Envia la humedad
    temp_2,hum_2 = censado.temperatura_humedad(pin) # Envia la temperatura y la humedad
    print('Temperatura 1:{} C\nHumedad 1:{} %\nTemperatura 2:{} C\nHumedad 2:{} %\n'.format(temp_1,hum_1,temp_2,hum_2))
else :
    print('Error de censado')