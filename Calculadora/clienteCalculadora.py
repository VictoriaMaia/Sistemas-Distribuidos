import socket
# HOST = '192.168.7.1'
HOST = ''
PORT = 5000
udpCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (HOST, PORT)

while True:
    informacoes = input()
    udpCliente.sendto(informacoes.encode(), address)
    if informacoes == 'end':
        break
    resp = udpCliente.recv(1024)
    print("   " + resp.decode())

udpCliente.close()