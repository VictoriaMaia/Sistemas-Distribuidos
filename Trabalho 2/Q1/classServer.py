import socket
from classCalc import Calculadora

class Server():
    def __init__(self):   
        self.calc = Calculadora()
        self.HOST = ''
        self.PORT = 5000
        self.addrComunic = (self.HOST, self.PORT)
        self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketServer.bind(self.addrComunic)
        self.socketServer.listen(2)
        self.socketC, self.addrC = self.socketServer.accept()

    # def conectarCliente(self):
    #     socketCliente, addrCli = self.socketServer.accept()
    #     return socketCliente

    def getRequest(self):
        request = self.socketC.recv(1024).decode()
        return request
        
    def sendResponse(self):
        while True:
            try:
                request = self.getRequest()
                if request == "sair":
                    break
                info = request.split(" ")
                if info[0] == "soma":
                    resposta = self.calc.soma(info[1], info[2])
                elif info[0] == "sub":
                    resposta = self.calc.sub(info[1], info[2])
                elif info[0] == "mult":
                    resposta = self.calc.mult(info[1], info[2])
                elif info[0] == "div":
                    if info[2] == "0":
                        resposta = "Operação inválida"
                    else:
                        resposta = self.calc.div(info[1], info[2])
                else:
                    resposta = "Operação inválida"
                self.socketC.send(str(resposta).encode())
            except IndexError:
                resposta = "Operação inválida"
                self.socketC.send(str(resposta).encode())
        
        return 
            
    def closed(self):
        self.socketC.close()

        

