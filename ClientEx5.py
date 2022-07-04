import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

Idade = input()
Sexo = input()

msg = str(Idade)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()

print('Categoria: ' data)