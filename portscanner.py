

import socket

tgtHost = input('Enter IP Address:')

tgtPorts = input('Enter Ports:')


# print('Target Host:', tgtHost,'\n''Target Port(s):', tgtPorts)


def connscan(tgtHost, tgtPorts):
    port = tgtPorts
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((tgtHost, port))
        print('Port:', (port), ' is OPEN!')
        s.close()
    except:
        print("Couldn't Connect")
        s.close()


def pscan(tgtHost, tgtPorts):
    port = tgtPorts
    try:
        tgtIP = socket.gethostbyaddr(tgtHost)
    except:
        print('Cannot be resolved:', tgtHost)
        return

    if port in tgtPorts:
        print('Scanning Port', port)
        connscan(tgtHost, port)


pscan(tgtHost, tgtPorts)
