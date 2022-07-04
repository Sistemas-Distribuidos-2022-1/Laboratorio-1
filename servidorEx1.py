import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

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

    nome, cargo, sal = data.split(' ')

    sal = float(sal)

    if cargo == 'operador':
        sal = salario + salario*0.2
    if cargo == 'programador':
        sal = salario + salario*0.18

    data = str.encode(nome + ' ' + cargo + ' ' + str(sal))

    conn.sendall(data)
