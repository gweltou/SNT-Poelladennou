# -*- coding: utf-8 -*-


# Emporzhiet e vez ar modul 'socket' evit implij ar fonksionoù rouedad
import socket


HOSTNAME = "" #socket.gethostname()
PORT = 6464

print("Loc'het eo ar servijer")
print("Anaouder: {}".format(socket.gethostbyname(HOSTNAME)))
print("Porzh:    {}".format(PORT))
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOSTNAME, PORT))
print("O selaou...")
serversocket.listen(1)

resevet = dict()

while True:
    (clientsocket, address) = serversocket.accept()
    data = clientsocket.recv(128)
    ostiz = address[0]
    pseudo = f"{address[0]}:{address[1]}"
    if ostiz in resevet:
        resevet[ostiz].append(data.decode('utf-8'))
        pseudo = resevet[ostiz][0][:12].strip()
    else:
        resevet[ostiz] = [data.decode('utf-8')]
    
    print("[{}] {}".format(pseudo, data.decode('utf-8')))
    clientsocket.sendall("OK".encode('latin-1'))
    clientsocket.close()
