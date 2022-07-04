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

    Idade, Tempo = data.split(' ')

    Idade = int(Idade)
    Tempo = int(Tempo)

    if Idade >= 65 or Tempo >= 30 or (Idade >= 60 and Tempo >=25):
        data = 'Aposentar'
    else:
        data = 'Trabalhar'

    data = str.encode(Nome + ' ' + Nivel + ' ' + str(salariobruto) + ' ' + str(numerodep))

    conn.sendall(data)