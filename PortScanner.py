#Basic Port Scanner

#!/usr/bin/python  

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.1" 
port = 80 

def portScanner(port):
    if sock.connect_ex((host, port)):
        print "Port %d is closed" % (port)
    else:
        print "Port %d is open" % (port)

portScanner(port)

