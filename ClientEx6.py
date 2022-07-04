import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

Nome = input()
Nivel = input()
salariobruto = input()
numerodep = input()

msg = str(Nome + '|' + Nível + '|' + salariobruto + '|' + numerodep)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()

Nome, Nível, salariobruto, numerodep = data.split(' ')

print('salario liquido: ' data)
print('Nome: 'Nome)
print('Nível: ', Nivel)