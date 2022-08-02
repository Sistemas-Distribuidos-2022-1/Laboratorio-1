import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:60060/")

print("numero questão: ")
q = input()

if(q == 0 or q > 8):
	print("numero de questão invalida")
	return 0
	
if q == 1:
	print("Nome funcionario : ")
	nome = input()
	print("Cargo funcionario : ")
	cargo = input()
	print("Salario funcionario : ")
	salario = input()

	result = proxy.e1(nome, cargo, salario)
	print(f"Salario reajustado : {result}")

if q == 2:
	print("Nome: ")
	nome = input()
	print("Sexo: ")
	sexo = input()
	print("Idade: ")
	idade = input()

	result = proxy.e2(nome, sexo, idade)
	print(f"{result}")

if q == 3:
	print("Nota 1: ")
	n1 = input()
	print("Nota 2: ")
	n2 = input()
	print("Nota 3: ")
	n3 = input()

	result = proxy.e3(n1, n2, n3)
	print(f"{result}")

if q == 4:
	print("Altura: ")
	altura = input()
	print("Sexo: ")
	sexo = input()
	
	result = proxy.e4(altura, sexo)
	print(f"Peso Ideal : {result}")
	
if q == 5:
	print("Idade: ")
	idade = input()
	
	result = proxy.e5(idade)
	print(f"Categoria é: {result}")
	
if q == 6:
	print("Salario Bruto: ")
	salbruto = input()
	print("Nome: ")
	nome = input()
	print("Nivel: ")
	nivel = input()
	print("Numero de dependentes: ")
	ndep = input()

	result = proxy.e6(salbruto, nome, nivel, ndep)
	print(f"Salario Liquido é: {result}")
	
if q == 7:
	print("Idade: ")
	idade = input()
	print("Tempo: ")
	tempo = input()
	
	result = proxy.e7(idade, tempo)
	print(f"{result}")
	
if q == 8:
	print("Saldo: ")
	saldo = input()

	result = proxy.e8(saldo)
	print(f"Percentual de credito: {result}")
	
