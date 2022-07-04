import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

vcarta = input()
naipe = input()

msg = str(vcarta + '|' + naipe)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()


print('Carta: ', data)
