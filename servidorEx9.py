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

    data = data.decode(

    vcarta, naipe = data.split(' ')

    vcarta = int(vcarta)
    naipe = int(naipe)


    if(naipe == 1):
        if(vcarta == 1):
            data = 'ás de ouros'
        if (vcarta == 2):
            data = 'dois de ouros'
        if(vcarta == 3):
            data = 'tres de ouros'
        if(vcarta == 4):
            data = 'quatro de ouros'
        if(vcarta == 5):
            data = 'cinco de ouros'
        if (vcarta == 6):
            data = 'seis de ouros'
        if(vcarta == 7):
            data = 'sete de ouros'
        if(vcarta == 8):
            data = 'oito de ouros'
        if(vcarta == 9):
            data = 'nove de ouros'
        if(vcarta == 10):
            data = 'dez de ouros'
        if(vcarta == 11):
            data = 'valete de ouros'
        if(vcarta == 12):
            data = 'rainha de ouros'
        if(vcarta == 13):
            data = 'rei de ouros'
    if (naipe == 2):
        if(vcarta == 1):
            data = 'ás de paus'
        if (vcarta == 2):
            data = 'dois de paus'
        if (vcarta == 3):
            data = 'tres de paus'
        if (vcarta == 4):
            data = 'quatro de paus'
        if (vcarta == 5):
            data = 'cinco de paus'
        if (vcarta == 6):
            data = 'seis de paus'
        if (vcarta == 7):
            data = 'sete de paus'
        if (vcarta == 8):
            data = 'oito de paus'
        if (vcarta == 9):
            data = 'nove de paus'
        if (vcarta == 10):
            data = 'dez de paus'
        if (vcarta == 11):
            data = 'valete de paus'
        if (vcarta == 12):
            data = 'rainha de paus'
        if (vcarta == 13):
            data = 'rei de paus'
    if (naipe == 3):
        if(vcarta == 1):
            data = 'ás de copas'
        if (vcarta == 2):
            data = 'dois de copas'
        if (vcarta == 3):
            data = 'tres de copas'
        if (vcarta == 4):
            data = 'quatro de copas'
        if (vcarta == 5):
            data = 'cinco de copas'
        if (vcarta == 6):
            data = 'seis de copas'
        if (vcarta == 7):
            data = 'sete de copas'
        if (vcarta == 8):
            data = 'oito de copas'
        if (vcarta == 9):
            data = 'nove de copas'
        if (vcarta == 10):
            data = 'dez de copas'
        if (vcarta == 11):
            data = 'valete de copas'
        if (vcarta == 12):
            data = 'rainha de copas'
        if (vcarta == 13):
            data = 'rei de copas'
    if (naipe == 4):
        if (vcarta == 1):
            data = 'ás de espadas'
        if (vcarta == 2):
            data = 'dois de espadas'
        if (vcarta == 3):
            data = 'tres de espadas'
        if (vcarta == 4):
            data = 'quatro de espadas'
        if (vcarta == 5):
            data = 'cinco de espadas'
        if (vcarta == 6):
            data = 'seis de espadas'
        if (vcarta == 7):
            data = 'sete de espadas'
        if (vcarta == 8):
            data = 'oito de espadas'
        if (vcarta == 9):
            data = 'nove de espadas'
        if (vcarta == 10):
            data = 'dez de espadas'
        if (vcarta == 11):
            data = 'valete de espadas'
        if (vcarta == 12):
            data = 'rainha de espadas'
        if (vcarta == 13):
            data = 'rei de espadas'

    data = str.encode(str(data))

    conn.sendall(data)
