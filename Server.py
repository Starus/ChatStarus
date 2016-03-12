#!/usr/bin/python
import socket

#constantes
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse address
host = "0.0.0.0"
port = 25525
s.bind((host, port))
#funciones

#bucle
s.listen(5)

while True:
    c, addr = s.accept()
    while True:
        #print "Joind" , addr
        #c.send("Gracias por entrar.")
        data = c.recv(1024)
        if data == "exit":
            c.send("\0\xDE\xAD\0")
            c.close()
            break
        if data:
		    print "data: %s" % data
		    c.send("%s" % data)
