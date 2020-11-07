#responsável por mandar e receber mensagem
import socket

class Client():
    def __init__(self):
        self.HOST = ''
        self.PORT = 5002
        self.addrComunic = (self.HOST, self.PORT)
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect(self.addrComunic)

    def sendRequest(self, request):
        self.socketClient.send(request.encode())

    def getResponse(self):
        answer = self.socketClient.recv(1024)
        return answer.decode()

    def close(self):
        print("Estou fechando..")
        request = "sair"
        self.socketClient.send(request.encode())
        self.socketClient.close()