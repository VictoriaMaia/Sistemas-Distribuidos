import socket
from threading import Thread

HOST = ''
PORT = 5005
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientAddr = (HOST, PORT)
client.connect(clientAddr)

def enviar(sClient):
    while True:
        msg = input()
        if msg:
            client.send(msg.encode())
            if msg == "sair":
                return
            if msg == "0":
                return
        else:
            print("Digite uma mensagem")



def receber(sClient):
    while True:
        data = sClient.recv(1024)
        print(data.decode())
        if data.decode() == "Saindo do chat...":
            break
        if data.decode() == "Ok, fechando chat":
            break


if __name__ == "__main__":
    treadReceber = Thread(target=receber, args=(client,))
    treadReceber.start()
    enviar(client)
    treadReceber.join()
    print("fechei")
    client.close()
