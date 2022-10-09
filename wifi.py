import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('SSID','PASSWORD') # SSID: nombre de la red, PASSWORD: clave de la red