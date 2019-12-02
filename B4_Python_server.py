# -*- coding: utf-8 -*-


import socket

HOSTNAME = "" #socket.gethostname()
PORT = 64646

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
    #clientsocket.sendall("Petra eo da añv ? ".encode('utf-8'))
    data = clientsocket.recv(128)
    if address[0] in resevet:
        resevet[address[0]].append(data.decode('utf-8'))
    else:
        resevet[address[0]] = [data.decode('utf-8')]
    
    print("[{}:{}]\t{}".format(address[0], address[1], data.decode('utf-8')))
    clientsocket.sendall("OK".encode('latin-1'))
    clientsocket.close()
