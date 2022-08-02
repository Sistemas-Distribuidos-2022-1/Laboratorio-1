from xmlrpc.server import SimpleXMLRPCServer

def e1(nome, cargo, salario):
	sal = int(salario)
	result = str(cargo)
	if result == "operador":
		sal = sal + sal*0.2
		return str(sal)
	if result == "programador":
		sal = sal + sal*0.18
		return str(sal)
		
def e2(nome, sexo, idade):
	idd = int(idade)
	result = str(sexo)
	if result == 'masculino':
		if idd > 18:
		    return "Maior de idade"
		else:
		    return "Menor de idade"
	if result == 'feminimo':
		if idd > 21:
		    return "Maior de idade"
		else:
		    return "Menor de idade"
		
def e3(n1, n2, n3):
	N1 = int(n1)
	N2 = int(n2)
	N3 = int(n3)
	
	m = ((N1+N2)/2)
	
	if m >= 7.0:
        	return "Aprovado"
    	if m > 3.0 and m < 7.0:
        	if ((m + N3)/2) >= 5.0 :
            		return "Aprovado"
    	else:
        	return "Reprovado"
        	
def e4(altura, sexo):
	result = str(sexo)
	alt = int(altura)
	if result == "masculino":
		alt = (72.7*alt) - 58
		return str(alt)
	else:
		alt = (62.1*alt) - 44.7
		return str(alt)
		
def e5(idade):
    result = int(idade)
    if(result >=5 and result <=7):
        return "infantil A"
    if(result >=8 and result <=10):
        return "infantil B"
    if(result >=11 and result <=13):
        return "juvenil A"
    if(result >=14 and result <=17):
        return "juvenil B"
    if(result >=18):
        return "adulto"
        
def e6(salbruto, nome, nivel, ndep):
	result = str(nivel)
	sb = int(salbruto)
	ndp = int(ndep)
	
	if result == 'A':
		if ndp == 0:
		    sb = sb - sb*0.03
		    return str(sb)
		else:
		    sb = sb - sb * 0.08
		    return str(sb)
	if result == 'B':
		if ndp == 0:
		    sb = sb - sb * 0.05
		    return str(sb)
		else:
		    sb = sb - sb * 0.1
		    return str(sb)
	if result == 'C':
		if ndp == 0:
		    sb = sb - sb * 0.08
		    return str(sb)
		else:
		    sb = sb - sb * 0.15
		    return str(sb)
	if result == 'D':
		if ndp == 0:
		    sb = sb - sb * 0.10
		    return str(sb)
		else:
		    sb = sb - sb * 0.17
		    return str(sb)
		   
def e7(idade, tempo):
	idd = int(idade)
	t = int(tempo)
	
	if idd >= 65 or t >= 30 or (idd >= 60 and t >=25):
        	return "Aposenta"
    	else:
       	return "Não aposenta"
       	
def e8(saldo):
	result  = int(saldo)
	
	if result >=0 and result <= 200:
		result = 0
		return str(result)
	if result >= 201 and result <= 400:
        	result = result*0.2
        	return str(result)
	if result >= 401 and result <= 600:
        	result = result * 0.3
        	return str(result)
	if result >= 201 and result <= 400:
        	result = result*0.2
        	return str(result)	
        
server = SimpleXMLRPCServer(("localhost",2020))
server.register_function(e1,"e1")
server.register_function(e2,"e2")
server.register_function(e3,"e3")
server.register_function(e4,"e4")
server.register_function(e5,"e5")
server.register_function(e6,"e6")
server.register_function(e7,"e7")
server.register_function(e8,"e8")
server.serve_forever()	
