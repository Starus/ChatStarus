import socket, threading

#const -------------------------------------------

s = socket.socket()
#host = raw_input("IP del server: ")
host = "0.0.0.0"
port = 25525


#if host == "r":
 #   host = "167.60.92.138"
  #  print host

#fuciones ----------------------------------------

threads = list()

def recibir():
    while True:
        rmsg = s.recv(120)
        print rmsg

def enviar():
    while True:
        smsg = raw_input(">>> ")
        s.send(smsg)
        rmsg = s.recv(120)
        if rmsg == "\0\xDE\xAD\0":
            exit(0)
        print rmsg

#loop --------------------------------------------
s.connect((host, port))
t1 = threading.Thread(target=recibir)
threads.append(t1)
t2 = threading.Thread(target=enviar)
threads.append(t2)
	

	#t1.setDaemon(True)
	#t2.setDaemon(True)

#t1.start()
t2.start()
#s.close()
