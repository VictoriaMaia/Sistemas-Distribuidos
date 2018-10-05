from classEsqueleto import Esqueleto
class Despachante():
    def __init__(self):
        self.e = Esqueleto()

    def decodifica(self, msg):
        dados = msg.decode()
        info = dados.split(" ")
        operacao = info[0]
        op1 = info[1]
        op2 = info[2]
        if operacao == "soma":
            resposta = self.e.soma(op1, op2)    
        elif operacao == "sub":
            resposta = self.e.sub(op1, op2)
        elif operacao == "mult":
            resposta = self.e.mult(op1, op2)
        elif operacao == "div":
            resposta = self.e.div(op1, op2)
        return resposta
    
    