import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
sexo = input()
idade = input()

msg = str(nome + '|' + sexo + '|' + idade)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()

print('nome: ', nome)
print('sexo: ', sexo)

if data == 'maioridade':
    print('Atingiu maioridade')
else:
    print('Não atingiu maioridade')
