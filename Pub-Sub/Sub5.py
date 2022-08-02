import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"CLASSIFIC")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"CLASSIFIC")

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
            idade = x["idade"]
            if idade >= 5 and idade <= 7:
                 data = "infantil A"
            else :
                 if idade >= 8 and idade <=10
                 	 data  = 'infantil B'
                 else:
                 	if idade >= 11 and idade <= 13:
                		data = ' Juvenil A'
            		else:
                		if idade >= 14 and idade <= 17:
                    			data = 'Juvenil B'
                		else:
                    			data = 'adulto'
                    			
            print("Classificação: ", data)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            idade = y["idade"]
            if idade >= 5 and idade <= 7:
                 data = "infantil A"
            else :
                 if idade >= 8 and idade <=10
                 	 data  = 'infantil B'
                 else:
                 	if idade >= 11 and idade <= 13:
                		data = ' Juvenil A'
            		else:
                		if idade >= 14 and idade <= 17:
                    			data = 'Juvenil B'
                		else:
                    			data = 'adulto'
                    			
            print("Classificação: ", data)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
