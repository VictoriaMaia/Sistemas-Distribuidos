from classProxy import Proxy

if __name__ == "__main__":
    p = Proxy()
    print ("soma op1 op2\nsub op1 op2\nmult op1 op2\ndiv op1 op2\nsair\n")
    while True:
        try:
            operacao = input()
            if operacao == "sair":
                p.close()
                break
            dados = operacao.split(" ")
            operacao = dados[0]
            op1 = dados[1]
            op2 = dados[2]
            if operacao == "soma":
                print(p.soma(op1, op2))    
            elif operacao == "sub":
                print(p.sub(op1, op2))
            elif operacao == "mult":
                print(p.mult(op1, op2))
            elif operacao == "div":
                print(p.div(op1, op2))
            else:
                print("Operação inválida")
        except IndexError:
                print("Operação inválida")
                