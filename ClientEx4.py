import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

Altura = input()
Sexo = input()

msg = str(Altura + '|' + Sexo)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()

print('Peso: ' data)
