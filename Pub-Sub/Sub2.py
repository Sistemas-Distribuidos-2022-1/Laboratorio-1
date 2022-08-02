import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"MAIORIDADE")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"MAIORIDADE")

    poller = zmq.Poller()
    poller.register(subscriber, zmq.POLLIN)
    poller.register(sub2, zmq.POLLIN)

    while True:

        try:
            socks = dict(poller.poll())
        except KeyboardInterrupt:
            exit()

        if subscriber in socks:
            [address, contents] = subscriber.recv_multipart()
            x = json.loads(contents)
            sexo = x["sexo"]
            idade = x["idade"]
            if ( (sexo == "masculino" and idade >= 18) or (sexo == "feminino" and idade >= 21)):
                saida = "Atingiu Maioridade"
            else:
            	saida = "Não atingiu Maioridade"

            print(x["nome"], saida)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            sexo = y["sexo"]
            idade = y["idade"]
            if ( (sexo == "masculino" and idade >= 18) or (sexo == "feminino" and idade >= 21)):
                saida = "Atingiu Maioridade"
            else:
            	saida = "Não atingiu Maioridade"

            print(x["nome"], saida)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
