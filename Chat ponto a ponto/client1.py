import socket

HOST = ''
PORT = 5001
server_addr = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_addr)
sock.listen(1)

while True:
    print ("Bem vindo ao chat bloqueante!\nPara sair digite {sair}\nEsperando algúem aparecer")
    conection, client_addr = sock.accept()
    while True:
        print("Sua vez de digitar")
        msg = input()
        if msg: 
            if msg == "sair":
                break
            enviar = "<cliOne> " + msg
            conection.sendall(enviar.encode())
        else:
            break
        print("Espere a resposta")
        data = conection.recv(1024)
        print(data.decode())
        
    break

conection.close()

