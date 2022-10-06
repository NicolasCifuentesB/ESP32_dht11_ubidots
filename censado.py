import dht
from machine import Pin

def revision(conexion) :
    try :
        sensor = dht11(Pin(conexion))
        sensor.measure()
        return True
    except OSError as e :
        return False

def temperatura(conexion) :
    sensor = dht11(Pin(conexion))
    sensor.measure()
    return sensor.temperature()

def humedad(conexion) :
    sensor = dht11(Pin(conexion))
    sensor.measure()
    return sensor.humidity()

def temperatura_humedad(conexion) :
    sensor = dht11(Pin(conexion))
    sensor.measure()
    return sensor.temperature(),sensor.humedity()