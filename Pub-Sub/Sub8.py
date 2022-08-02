import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"CREDITO")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"CREDITO")

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
            saldo = x["saldo"]
            if saldo >=0 and saldo <= 200:
		data = 0
	    if saldo >= 201 and saldo <= 400:
		data = saldo*0.2
	    if saldo >= 401 and saldo <= 600:
		data = saldo * 0.3
	    if saldo >= 201 and saldo <= 400:
		data = saldo*0.2
                 
            print("Saldo de credito :", data)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            saldo = y["saldo"]
            if saldo >=0 and saldo <= 200:
		data = 0
	    if saldo >= 201 and saldo <= 400:
		data = saldo*0.2
	    if saldo >= 401 and saldo <= 600:
		data = saldo * 0.3
	    if saldo >= 201 and saldo <= 400:
		data = saldo*0.2
                 
            print("Saldo de credito :", data)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
