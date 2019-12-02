# -*- coding: utf-8 -*-


# Emporzhiet e vez ar modul 'socket' evit implij ar fonksionoù rouedad
import socket

# Termenet e vez ar fonksion 'netcat'
def netcat(anaouder, porz, titour):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((anaouder, porz))
    s.sendall(titour.encode("utf-8"))
    s.shutdown(socket.SHUT_WR)
    
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data
    
    print("Resevet:")
    print(response.decode("latin-1"))
    s.close()
    print("Sarret eo bet al liamm.")
