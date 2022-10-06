import censado

pin = 15

if censado.revision(pin) :
    print(censado.temperatura(pin))
    print(censado.humedad(pin))
    print(censado.temperatura_humedad(pin))