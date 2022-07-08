import socket
import threading

HOST = 'localhost'
PORT = 15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

def Salario_reajustado(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    nome, cargo, salario = data.split('|')
    
    salario = float(salario)

    if cargo == 'operador':
        salario = salario + salario*0.2
    if cargo == 'programador':
        salario = salario + salario*0.18
        
    data = str.encode(str(salario))

    conn.sendall(data)
    
def Maioridade(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    nome, sexo, idade = data.split('|')

    idade = int(idade)

    if sexo == 'masculino':
        if idade > 18:
            data = 'maior de idade'
        else:
            data = 'menor'
    if sexo == 'feminimo':
        if idade > 21:
            data = 'maior de idade'
        else:
            data = 'menor de idade'
        
    data = str.encode(data)

    conn.sendall(data)
  
def Aprovacao(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    N1, N2, N3 = data.split('|')

    N1 = float(N1)
    N2 = float(N2)
    N3 = float(N3)

    m = ((N1 + N2)/2)

    if m >= 7.0:
        data = 'Aprovado'
    if m > 3.0 and m < 7.0:
        if ((m + N3)/2) >= 5.0 :
            data = 'Aprovado'
    else:
        data = 'Reprovado'
        
    data = str.encode(data)

    conn.sendall(data)
  
def Peso_ideal(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    altura, sexo= data.split('|')

    altura = float(Altura)

    m = ((N1 + N2)/2)

    if sexo == 'masculino':
        data = (72.7*altura) - 58
    else:
        data = (62.1*altura) -44.7
        
    data = str.encode(str(data))

    conn.sendall(data)
  
def Categoria(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    idade = int(idade)

    if idade >=5 and idade <= 7:
        data = 'infantil A'
    else:
        if idade >=8 and idade <= 10:
            data  = 'infantil B'
        else:
            if idade >= 11 and idade <= 13:
                data = ' Juvenil A'
            else:
                if idade >= 14 and idade <= 17:
                    data = 'Juvenil B'
                else:
                    data = 'adulto'
        
    data = str.encode(data)

    conn.sendall(data)
    
def Salario_liquido(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    nome, nivel, salbruto, ndep = data.split('|')

    salbruto = float(salbruto)
    ndep = int(ndep)

    if nivel == 'A':
        if ndep == 0:
            data = salbruto - salbruto*0.03
        else:
            data = salbruto - salbruto * 0.08
    if nivel == 'B':
        if ndep == 0:
            data = salbruto - salbruto * 0.05
        else:
            data = salbruto - salbruto * 0.1
    if nivel == 'C':
        if ndep == 0:
            data = salbruto - salbruto * 0.08
        else:
            data = salbruto - salbruto * 0.15
    if nivel == 'D':
        if ndep == 0:
            data = salbruto - salbruto * 0.10
        else:
            data = salbruto - salbruto * 0.17

    data = str.encode(str(data))

    conn.sendall(data)
    
def Aposenta(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    idade, tempo = data.split('|')

    idade = int(idade)
    tempo = int(tempo)

    if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >=25):
        data = 'aposenta'
    else:
        data = 'não aposenta'

    data = str.encode(str(data))

    conn.sendall(data)
    
def Per_Credito(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    saldo = int(saldo)

    if saldo >=0 and saldo <= 200:
        data = 0
    if saldo >= 201 and saldo <= 400:
        data = saldo*0.2
    if saldo >= 401 and saldo <= 600:
        data = saldo * 0.3
    if saldo >= 201 and saldo <= 400:
        data = saldo*0.2

    data = str.encode(str(data))

    conn.sendall(data)
    
def Baralho(conn):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    num, naipe = data.split(' ')

    num = int(num)
    naipe = int(naipe)


    if(naipe == 1):
        if(num == 1):
            data = 'ás de ouros'
        if (num == 2):
            data = 'dois de ouros'
        if(num == 3):
            data = 'tres de ouros'
        if(num == 4):
            data = 'quatro de ouros'
        if(num == 5):
            data = 'cinco de ouros'
        if (num == 6):
            data = 'seis de ouros'
        if(num == 7):
            data = 'sete de ouros'
        if(num == 8):
            data = 'oito de ouros'
        if(num == 9):
            data = 'nove de ouros'
        if(num == 10):
            data = 'dez de ouros'
        if(num == 11):
            data = 'valete de ouros'
        if(num == 12):
            data = 'rainha de ouros'
        if(num == 13):
            data = 'rei de ouros'
    if (naipe == 2):
        if(num == 1):
            data = 'ás de paus'
        if (num == 2):
            data = 'dois de paus'
        if (num == 3):
            data = 'tres de paus'
        if (num == 4):
            data = 'quatro de paus'
        if (num == 5):
            data = 'cinco de paus'
        if (num == 6):
            data = 'seis de paus'
        if (num == 7):
            data = 'sete de paus'
        if (num == 8):
            data = 'oito de paus'
        if (num == 9):
            data = 'nove de paus'
        if (num == 10):
            data = 'dez de paus'
        if (num == 11):
            data = 'valete de paus'
        if (num == 12):
            data = 'rainha de paus'
        if (num == 13):
            data = 'rei de paus'
    if (naipe == 3):
        if(num == 1):
            data = 'ás de copas'
        if (num == 2):
            data = 'dois de copas'
        if (num == 3):
            data = 'tres de copas'
        if (num == 4):
            data = 'quatro de copas'
        if (num == 5):
            data = 'cinco de copas'
        if (num == 6):
            data = 'seis de copas'
        if (num == 7):
            data = 'sete de copas'
        if (num == 8):
            data = 'oito de copas'
        if (num == 9):
            data = 'nove de copas'
        if (num == 10):
            data = 'dez de copas'
        if (num == 11):
            data = 'valete de copas'
        if (num == 12):
            data = 'rainha de copas'
        if (num == 13):
            data = 'rei de copas'
    if (naipe == 4):
        if (num == 1):
            data = 'ás de espadas'
        if (num == 2):
            data = 'dois de espadas'
        if (num == 3):
            data = 'tres de espadas'
        if (num == 4):
            data = 'quatro de espadas'
        if (num == 5):
            data = 'cinco de espadas'
        if (num == 6):
            data = 'seis de espadas'
        if (num == 7):
            data = 'sete de espadas'
        if (num == 8):
            data = 'oito de espadas'
        if (num == 9):
            data = 'nove de espadas'
        if (num == 10):
            data = 'dez de espadas'
        if (num == 11):
            data = 'valete de espadas'
        if (num == 12):
            data = 'rainha de espadas'
        if (num == 13):
            data = 'rei de espadas'


    data = str.encode(str(data))

    conn.sendall(data)
    
def client(conn, ender):
    data = conn.recv(1024)

    if not data:
    	print('Conexão fechada')
    	conn.close()
    	return 0

    data = data.decode()

    if data == '1':
    	Salario_reajustado(conn)
    if data == '2':
    	Maioridade(conn)	
    if data == '3':
    	Aprovacao(conn)	
    if data == '4':
    	Peso_ideal(conn)	
    if data == '5':
    	Categoria(conn)	
    if data == '6':
    	Salario_liquido(conn)	
    if data == '7':
    	Aposenta(conn)	
    if data == '8':
    	Per_Credito(conn)
    if data == '9':
    	Baralho(conn)
    	    
def conc():
    s.listen()

    print('Esperando conexão')
	
    while True:
    	conn, ender = s.accept()
    	
    	print('Conectado em', ender)
    	thread = threading.Thread(target=client, args=(conn, ender))
    	thread.conc()
    	print(f"Conecçõe {threading.activeCount() - 1}")
    
    conc()
	
conc()
