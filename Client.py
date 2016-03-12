#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = raw_input("IP:")     # Get local machine name
port = 25525                # Reserve a port for your service.
msg = raw_input("Mensaje:")

if host == "r":
    host = "167.60.92.138"

print host
s.connect((host, port))
meg = s.recv(1024)
meg2 = s.recv(1024)
while True:
    print meg
    print meg2
    s.send(msg)

s.close()   # Close the socket when done

