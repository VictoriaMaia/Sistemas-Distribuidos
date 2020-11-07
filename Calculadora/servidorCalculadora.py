import socket
HOST = ''
PORT = 5000
udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (HOST, PORT)
udpServer.bind(address)

def operacoes(dados):
    info = dados.split(" ")
    if info[0] == "soma":
        resp = float(info[1]) + float(info[2])
    elif info[0] == "sub":
        resp = float(info[1]) - float(info[2])
    elif info[0] == "mult":
        resp = float(info[1]) * float(info[2])
    elif info[0] == "div":
        if float(info[2]) == 0:
            resp = "Divisão inválida."
        else:
            resp = float(info[1]) / float(info[2])
    else:
        resp = "Operação inválida."

    return resp


while True:
    print('Esperando pela requisição...')
    dados, cliente = udpServer.recvfrom(1024)
    print(cliente)
    if dados.decode() == 'end':
        break
    resposta = operacoes(dados.decode())
    udpServer.sendto(str(resposta).encode(), cliente)

udpServer.close()