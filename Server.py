#!/usr/bin/python
#import
import socket

#constantes
s = socket.socket()
host = "127.0.0.1"
port = 25525
s.bind((host, port))
#funciones

#bucle
s.listen(5)

while True:
    c, addr = s.accept()
    print "Joind" , addr
    c.send("Gracias por entrar.")
    print s.recv(1024)
    c.close()