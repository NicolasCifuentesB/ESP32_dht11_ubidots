import dht
from machine import Pin

# Función para verificar el funcionamiento del sensor
def revision(pin_sensor) :
    try :
        sensor = dht.DHT11(Pin(pin_sensor))
        sensor.measure()
        return True
    except OSError as e :
        return False

# Función para retornar la temperatura
def temperatura(pin_sensor) :
    sensor = dht.DHT11(Pin(pin_sensor))
    sensor.measure()
    return sensor.temperature()

# Función para retornar la humedad
def humedad(pin_sensor) :
    sensor = dht.DHT11(Pin(pin_sensor))
    sensor.measure()
    return sensor.humidity()

# Función para retornar la temperatura y humedad
def temperatura_humedad(pin_sensor) :
    sensor = dht.DHT11(Pin(pin_sensor))
    sensor.measure()
    return sensor.temperature(),sensor.humidity()