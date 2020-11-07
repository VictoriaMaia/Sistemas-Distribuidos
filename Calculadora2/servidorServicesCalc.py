import socket
import math
HOST = ''
PORT = 5000
udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (HOST, PORT)
udpServer.bind(address)

def calculadoraSimples(info):
    if info[1] == "soma":
        resp = float(info[2]) + float(info[3])
    elif info[1] == "sub":
        resp = float(info[2]) - float(info[3])
    elif info[1] == "mult":
        resp = float(info[2]) * float(info[3])
    elif info[1] == "div":
        if float(info[3]) == 0:
            resp = "Divisão inválida."
        else:
            resp = float(info[2]) / float(info[3])
    else:
        resp = "Operação inválida."

    return resp

def calculadoraCientifica(info):
    if info[1] == "expo":
        resp = pow(float(info[2]), float(info[3]))
    elif info[1] == "raizQuadrada":
        resp = math.sqrt(float(info[2]))
    else:
        resp = "Operação inválida."

    return resp


while True:
    print('Esperando pela requisição...')
    dados, cliente = udpServer.recvfrom(1024)
    recebi = dados.decode()
    info = recebi.split(" ")

    if info[0] == 'end':
        break
    if info[0] == "0":
        resposta = calculadoraSimples(info)
    elif info[0] == "1":
        resposta = calculadoraCientifica(info)
    else:
        resposta = "Operação inválida."

    udpServer.sendto(str(resposta).encode(), cliente)

udpServer.close()