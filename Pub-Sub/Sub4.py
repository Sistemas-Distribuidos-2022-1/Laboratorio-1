import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"PESOIDEAL")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"PESOIDEAL")

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
            altura = x["altura"]
            sexo = x["sexo"]
            if ( sexo == "masculino" ):
                 peso = (72.7*altura) - 58
            else :
                 peso = (62.1*altura) - 44.7
                 
            print("Peso Ideal: ", peso)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            altura = y["altura"]
            sexo = y["sexo"]
            if ( sexo == "masculino" ):
                 peso = (72.7*altura) - 58
            else :
                 peso = (62.1*altura) - 44.7
                 
            print("Peso Ideal: ", peso)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
