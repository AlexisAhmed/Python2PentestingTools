#Simple Banner Grabber

#!/usr/bin/python

import socket

def bannerGrab(ip, port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    ip = raw_input("[=>] Enter IP: ")
    port = str(raw_input("[=>] Enter Port: "))
    for port in range (20, 100):
        banner = bannerGrab(ip, port)
        if banner:
            print "[=>] " + ip + "/" + str(port) + ": " + banner.strip('/n')
            exit()

main()