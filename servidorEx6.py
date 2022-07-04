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

    Nome, Nivel, salariobruto, numerodep = data.split(' ')

    salariobruto = float(salariobruto)
    numerodep = int(numerodep)

    if Nivel == 'A':
        if numerodep == 0:
            data = salariobruto - salariobruto*0,03
        else:
            data = salariobruto - salariobruto * 0,08
    if nivel == 'B':
        if numerodep == 0:
            data = salariobruto - salariobruto * 0,05
        else:
            data = salariobruto - salariobruto * 0,1
    if nivel == 'C':
        if numerodep == 0:
            data = salariobruto - salariobruto * 0,08
        else:
            data = salariobruto - salariobruto * 0,15
    if nivel == 'D':
        if numerodep == 0:
            data = salariobruto - salariobruto * 0,10
        else:
            data = salariobruto - salariobruto * 0,17

    data = str.encode(Nome + ' ' + Nivel + ' ' + str(salariobruto) + ' ' + str(numerodep))

    conn.sendall(data)