import socket
from classDespachante import Despachante

class Server():
    def __init__(self):   
        self.d = Despachante()
        self.HOST = ''
        self.PORT = 5002
        self.addrComunic = (self.HOST, self.PORT)
        self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketServer.bind(self.addrComunic)
        self.socketServer.listen(2)
        self.socketC, self.addrC = self.socketServer.accept()

    def getRequest(self):
        return self.socketC.recv(1024)
        
    def sendResponse(self):
        while True:
            request = self.getRequest()
            if request.decode() == "sair":
                break
            resposta = self.d.decodifica(request)
            self.socketC.send(str(resposta).encode())

    def closed(self):
        self.socketC.close()

        

