import socket
import time

def send_data(token,body) :
    s = socket.socket()
    s.connect(('industrial.api.ubidots.com',80))
    request = bytes('POST /api/v1.6/devices/ESP32 HTTP/1.1\r\nHost: industrial.api.ubidots.com\r\nX-Auth-Token: %s\r\nContent-Type: application/json\r\nContent-Length: %s\r\n\r\n%s\r\n' % (token, len(body), body), 'utf8')
    print('Sending data to ubidots')
    s.send(request)
    dump_socket(s)

def dump_socket(s) :
    try :
        while True :
            
            data = s.recv(100)

            if data :
                print(str(data,'utf-8'),end='')
                s.close()
                break
            else :
                print('Error')
                s.close()
                break
    except :
        s.close()
        raise Exception('Error durante la ejecucion')

def upload(value,ubidots_token) :
    body='{"Estado": ' + repr(value) +'}'
    send_data(ubidots_token,body)