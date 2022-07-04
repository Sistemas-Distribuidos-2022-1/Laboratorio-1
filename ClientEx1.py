import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
cargo = input()
salario = input()

msg = str(nome + '|' + cargo + '|' + salario)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()
nome, cargo, salario = data.split('|')


print('Cargo: ', cargo)
print('Salario com reajuste: ', salario)
