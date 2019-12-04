# -*- coding: utf-8 -*-


# Emporzhiet e vez ar modul 'socket' evit implij ar fonksionoù rouedad
import socket


# Termenet e vez ar fonksion 'netcat'
def netcat(anaouder, porz, titour):
    # Digoret e vez un 'nor' gant ar protokol TCP war hor urzhiataer
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Kevreet e vez gant ar servijer
    s.connect((anaouder, porz))
    
    # Kaset e vez an titouroù
    s.sendall(titour.encode("utf-8"))
    
    # Sarret e vez al liamm
    s.shutdown(socket.SHUT_WR)
    
    # Lennet e vez ar respont bet adkaset gant ar servijer
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data
    
    # Skrivet e vez ar respont war ho skramm
    print("Resevet:")
    print(response.decode("latin-1"))
    
    # Sarret e vez an 'nor'
    s.close()
    print("Sarret eo bet al liamm.")
