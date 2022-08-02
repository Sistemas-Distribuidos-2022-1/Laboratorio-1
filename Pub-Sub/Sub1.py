import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"REAJUSTE")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"REAJUSTE")

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
            salario = x["salario"]
            cargo = x["cargo"]
            if ( cargo == "programador"):
                salario = x["salario"]*1.18
            else:
                salario = x["salario"]*1.2

            print("Nome : ",x["nome"],",","Salario final : ",salario)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            salario2 = y["salario"]
            cargo2 = y["cargo"]
            if ( cargo2 == "programador"):
                salario = y["salario"]*1.18
            else:
                salario = y["salario"]*1.2

            print("Nome : ",y["nome"],",","Salario final : ",salario)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
