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

    Idade = int(Idade)

    if Idade >=5 and Idade <= 7:
        data = 'infantil A'
    else:
        if Idade >=8 and Idade <= 10:
            data  = 'infantil B'
        else:
            if Idade >= 11 and Idade <= 13:
                data = ' Juvenil A'
            else:
                if Idade >= 14 and Idade <= 17:
                    data = 'Juvenil B'
                else:
                    data = 'adulto'

    data = str.encode(str(Idade))

    conn.sendall(data)
