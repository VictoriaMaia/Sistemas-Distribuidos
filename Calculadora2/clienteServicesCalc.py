import socket
HOST = ''
PORT = 5000
udpCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (HOST, PORT)

print("0 - Calculadora simples\n     soma op1 op2\n     sub op1 op2\n     mult op1 op2\n     div op1 op2\n")
print("1 - Calculadora científica\n     expo op1 op2\n     raizQuadrada op1\n")

while True:    
    informacoes = input()
    udpCliente.sendto(informacoes.encode(), address)
    if informacoes == 'end':
        break
    resp = udpCliente.recv(1024)
    print("   " + resp.decode())

udpCliente.close()