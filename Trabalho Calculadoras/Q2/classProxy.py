from classClient import Client

class Proxy():
    def __init__(self):
        self.Cli = Client()

    def soma(self, op1, op2):
        msg = "soma" + " " + op1 + " " + op2
        self.Cli.sendRequest(msg)
        return self.Cli.getResponse()

    def sub(self, op1, op2):
        msg = "sub" + " " + op1 + " " + op2
        self.Cli.sendRequest(msg)
        return self.Cli.getResponse()

    def mult(self, op1, op2):
        msg = "mult" + " " + op1 + " " + op2
        self.Cli.sendRequest(msg)
        return self.Cli.getResponse()
    
    def div(self, op1, op2):
        msg = "div" + " " + op1 + " " + op2
        self.Cli.sendRequest(msg)
        return self.Cli.getResponse()
    
    def close(self):
        self.Cli.close()