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

    Altura, Sexo= data.split('|')

    Altura = float(Altura)

    m = ((N1 + N2)/2)

    if Sexo == 'masculino':
        data = (72.7*Altura) - 58
    else:
        data = (62,1*Altura) -44,7

    data = str.encode(data)

    conn.sendall(data)
