from classClient import Client

class User():
    def __init__(self):
        self.Cli = Client()

    def readRequest(self):
        operacao = input()
        self.Cli.sendRequest(operacao)
        if operacao == "sair":
            return 1

    def writeAnswer(self):
        print(self.Cli.getResponse())

    def sair(self):
        self.Cli.close()
        