import dht
from machine import Pin

# Función para verificar el funcionamiento del sensor
def revision(conexion) :
    try :
        sensor = dht.DHT11(Pin(conexion))
        sensor.measure()
        return True
    except OSError as e :
        return False

# Función para retornar la temperatura
def temperatura(conexion) :
    sensor = dht.DHT11(Pin(conexion))
    sensor.measure()
    return sensor.temperature()

# Función para retornar la humedad
def humedad(conexion) :
    sensor = dht.DHT11(Pin(conexion))
    sensor.measure()
    return sensor.humidity()

# Función para retornar la temperatura y humedad
def temperatura_humedad(conexion) :
    sensor = dht.DHT11(Pin(conexion))
    sensor.measure()
    return sensor.temperature(),sensor.humidity()