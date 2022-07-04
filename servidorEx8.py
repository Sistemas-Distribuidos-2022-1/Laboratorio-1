import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HOST,PORT))

s.listen()

print('Esperando conexão')

conn, ender = s.accept()

pint('Conectado em', ender)

while True
    data = conn.recv(1024)

    if not data:
        print('Conexão fechada')
        conn.close()
        break

    data = data.decode()

    saldo = int(saldo)

    if saldo >=0 and saldo <= 200:
        data = 0
    if saldo >= 201 and saldo <= 400:
        data = saldo*0,2
    if saldo >= 401 and saldo <= 600:
        data = saldo * 0,3
    if saldo >= 201 and saldo <= 400:
        data = saldo*0,2

    data = str.encode(str(saldo))

    conn.sendall(data)