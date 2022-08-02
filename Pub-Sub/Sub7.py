import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"APOSENT")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"APOSENT")

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
            tempo = x["tempo"]
            if (idade >= 65 or tempo >= 30) or (idade >= 60 and tempo >=25):
        	data = 'aposenta'
    	    else:
        	data = 'não aposenta'
                 
            print(data)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            idade = y["idade"]
            tempo = y["tempo"]
            if (idade >= 65 or tempo >= 30) or (idade >= 60 and tempo >=25):
        	data = 'aposenta'
    	    else:
        	data = 'não aposenta'
                 
            print(data)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
