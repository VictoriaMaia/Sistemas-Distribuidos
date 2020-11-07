import socket

HOST = ''
PORT = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = (HOST, PORT)
sock.connect(server_addr)
print("Bem vindo ao chat bloqueante!\nPra sair digite {sair}")
while True:
    print("Espere a resposta")
    data = sock.recv(1024)
    print(data.decode())
    print("Sua vez de digitar")
    msg = input()
    if msg:
        if msg == "sair":
            break
        enviar = "<cliTwo> " + msg
        sock.sendall(enviar.encode())
    else:
        break

sock.close()
