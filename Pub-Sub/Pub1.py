import time
import zmq


def main():

    context = zmq.Context()
    publisher = context.socket(zmq.PUB) #criando o socket publicador
    p = "tcp://*:6666" #como e onde se comunica
    publisher.bind(p) #bind socket com endereço

    while True:
        #Exercicio 1 :
        publisher.send_multipart([b"REAJUSTE", b'{ "nome":"Vinicius", "cargo":"programador", "salario":1000}'])
        publisher.send_multipart([b"REAJUSTE", b'{ "nome":"Claudio", "cargo":"operador", "salario":1000}'])
        
        #Exercicio 2 :
        publisher.send_multipart([b"MAIORIDADE", b'{ "nome":"Claudia", "sexo":"feminino", "idade":23}'])
        publisher.send_multipart([b"MAIORIDADE", b'{ "nome":"Vinicius", "sexo":"masculino", "idade":23}'])
        
        #Exercicio 3 :
        publisher.send_multipart([b"APROVAD", b'{ "N1":4, "N2":3, "N3":1}'])
        publisher.send_multipart([b"APROVAD", b'{ "N1":6, "N2":1, "N3":4}'])
        
        #Exercicio 4 :
        publisher.send_multipart([b"PESOIDEAL", b'{ "altura":1.62, "sexo":"feminino"}'])
        publisher.send_multipart([b"PESOIDEAL", b'{ "altura":1.31, "sexo":"feminino"}'])
        
        #Exercicio 5 :
        publisher.send_multipart([b"CLASSIFIC", b'{ "idade":14 }'])
        publisher.send_multipart([b"CLASSIFIC", b'{ "idade":56 }'])
        
        #Exercicio 6 :
        publisher.send_multipart([b"SALLIQ", b'{ "salario":1400, "nome": Renato, "nivel": A "numero dependentes": 0}'])
        publisher.send_multipart([b"SALLIQ", b'{ "salario":1400, "nome": Juliana, "nivel": C "numero dependentes": 2}'])
        
        #Exercicio 7 :
        publisher.send_multipart([b"APOSENT", b'{ "idade":45, "tempo":30}'])
        publisher.send_multipart([b"APOSENT", b'{ "idade":30, "tempo":10}'])
        
        #Exercicio 8:
        publisher.send_multipart([b"CREDITO", b'{ "saldo":602}'])
        publisher.send_multipart([b"CREDITO", b'{ "saldo":156}'])
        
        
        time.sleep(1)

    publisher.close()
    context.term()

if __name__ == "__main__":
    main()
