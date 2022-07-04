import socket

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen()

print('Esperando conexão')

conn, ender = s.accept()

print('Conectado em', ender)

while True:
    data = conn.recv(1024)

    if not data:
        print('Conexão fechada')
        conn.close()
        break

    data = data.decode()

    N1, N2, N3 = data.split('|')

    N1 = float(N1)
    N2 = float(N2)
    N3 = float(N3)

    m = ((N1 + N2)/2)

    if m >= 7,0:
        data = 'Aprovado'
    if m > 3,0 and m < 7,0:
        if ((m + N3)/2) >= 5,0 :
            data = 'Aprovado'
    else:
        data = 'Reprovado'

   data = str.encode(data)

   conn.sendall(data)
