import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"APROVAD")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"APROVAD")

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
            n1 = x["n1"]
            n2 = x["n2"]
            n3 = x["n3"]
            M = (n1+n2)/2
            if ( M >= 7):
                 resultado = "Aprovado"
            else :
                 resultado = "Reprovado"
            if ( M >=3 and M <= 7):
                if ((M+n3)/2 >= 5):
                    resultado = "Aprovado"
                else :
                    resultado = "Reprovado"
            print(resultado)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            n1 = y["n1"]
            n2 = y["n2"]
            n3 = y["n3"]
            M = (n1+n2)/2
            if ( M >= 7):
                 resultado = "Aprovado"
            else :
                 resultado = "Reprovado"
            if ( M >=3 and M <= 7):
                if ((M+n3)/2 >= 5):
                    resultado = "Aprovado"
                else :
                    resultado = "Reprovado"
            print(resultado)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
