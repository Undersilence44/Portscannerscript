import socket


tgtHost = input ('Enter IP Address:')
    
tgtPorts = input ('Enter Ports:')

#print('Target Host:', tgtHost,'\n''Target Port(s):', tgtPorts)



def connscan (tgtHost, tgtPorts):
    try:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((tgtHost, port))
        print('Port:'(port),' is OPEN!')
        s.close()

def pscan (tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyaddr(tgtHost)
    except:
        print('Cannot be resloved:', tgtHost)
        return

    for port in tgtPorts:
        print('Scanning Port', port)
        connscan(tgtHost, int(port))