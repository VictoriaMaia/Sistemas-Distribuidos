import socket
import time
from threading import Thread

HOST = ''
PORT = 5005

clientesConectados = {}
serverAddr = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(serverAddr)
server.listen(2)

def conversa(sClient):
    print("entrou")
    nome = sClient.recv(1024)
    nome = nome.decode()
    clientesConectados[sClient] = nome
    msgEntrou = " entrou no chat!"
    broadcast(msgEntrou, nome)
    while True:
        m = sClient.recv(1024)
        mensagem = m.decode()
        if mensagem != "sair":
            broadcast(mensagem, nome)
        else:
            msgFim = "Saindo do chat..."
            sClient.send(msgFim.encode())
            del clientesConectados[sClient]
            broadcast("Saiu do chat", nome)
            sClient.close()
            break            

def broadcast(msg, prefix=''):
    enviar = "<" + prefix + "> " + msg
    for sockCl in clientesConectados:
        print(sockCl)
        sockCl.send(enviar.encode())

def conectou(sClient, addr):
    msgBoasVindas = "Bem-vindo ao Chat!\nSe desejar sair digite {sair}\nPara começar digite seu nome: "
    sClient.send(msgBoasVindas.encode())
    Thread(target=conversa, args=(sClient,)).start()

def recebendoClientes():
    while True:
        print("Esperando conexão...")
        client, clientAddr = server.accept()
        if len(clientesConectados) == 0:
            continuar = "Não tem ninguem no chat. Deseja iniciar o chat? {1:sim}{0:nao}"
            client.send(continuar.encode())
            resp = client.recv(1024)
            if resp.decode() == "1":
                conectou(client, clientAddr[0])
            if resp.decode() == "0":
                saindo = "Ok, fechando chat"
                client.send(saindo.encode())
                client.close()
                return
        else:
            conectou(client, clientAddr[0])


if __name__ == "__main__":
    recebendoClientes()
    #server.close()


