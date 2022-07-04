import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

N1 = input()
N2 = input()
N3 = input()

msg = str(N1 + '|' + N2 + '|' + N3)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()
N1, N2, N3 = data.split(' ')


if data == 'Aprovado':
    print('Aprovado')
else:
    print('Reprovado')