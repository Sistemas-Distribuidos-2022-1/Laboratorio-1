import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

Idade = input()
Tempo = input()

msg = str(Idade + '|' + Tempo)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()


if data == 'Aposentar'
    print('Funcionario pode se aposentar')
else
    print('FUncionario não pode se aposentar')
