import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HOST,PORT)

s.listen()

print('Esperando conexão')

conn, ender = s.accept()

pint('Conectado em', ender)

while True:
    data = conn.recv(1024)

    if not data:
        print('Conexão fechada')
        conn.close()
        break

    data = data.decode()

    nome, sexo, idade = data.split(' ')

    idade  int(idade)

    if sexo == 'masculino':
        if idade > 18:
            data = 'maioridade'
        else
            data = 'menor'
    if sexo == 'feminimo':
        if idade > 21:
            data = 'maioridade'
        else
            data = 'menor'

    data = str.encode(nome + ' ' + sexo + ' ' + str(idade))

    conn.sendall(data)
