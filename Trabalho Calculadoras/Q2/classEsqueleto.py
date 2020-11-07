from classCalc import Calculadora
class Esqueleto():
    def __init__(self):
        self.c = Calculadora()

    def soma(self, op1, op2):
        ope1 = float(op1)
        ope2 = float(op2)
        return self.c.soma(ope1, ope2)

    def sub(self, op1, op2):
        ope1 = float(op1)
        ope2 = float(op2)
        return self.c.sub(ope1, ope2)

    def mult(self, op1, op2):
        ope1 = float(op1)
        ope2 = float(op2)
        return self.c.mult(ope1, ope2)
    
    def div(self, op1, op2):
        ope1 = float(op1)
        ope2 = float(op2)
        if ope2 == 0:
            return "Operação inválida"
        return self.c.div(ope1, ope2)
    