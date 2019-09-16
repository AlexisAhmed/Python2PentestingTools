#Advanced Port Scanner Optimized For Faster Scans
#Script Usage: python AdvancedPortScanner.py -H 192.168.1.1 -P 22 


#!/usr/bin/env python

from socket import *
import optparse 
from threading import *


def connScan(tgtHost,tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print '[=>]%d/tcp open' % tgtPort
    except:
        print '[=>]%d/tcp closed' % tgtPort
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    
    except:
        print 'Cannot resolve the target %s' %tgtHost
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '[=>] Scan results for : ' + tgtName[0] 

    except:
        print '[=>] Scan results for: ' + tgtIP 
    
    setdefaulttimeout(5)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()



def main():
    parser = optparse.OptionParser('Script usage: ' + ' -H <host> -P <port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='please sopecify the target IP')
    parser.add_option('-P', dest='tgtPort', type='string', help='please specify the target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split('.')

    if (tgtHost == None) | (tgtPort[0] == None):
        print parser.usage
        exit(0)
    portScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main()

