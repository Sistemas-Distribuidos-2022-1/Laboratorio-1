import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    p = "tcp://localhost:6666"
    subscriber.connect(p)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"SALLIQ")

    sub2 = context.socket(zmq.SUB)
    p2 = "tcp://localhost:6668"
    sub2.connect(p2)
    sub2.setsockopt(zmq.SUBSCRIBE, b"SALLIQ")

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
            nome = x["nome"]
            salbruto = x["salario"]
            nivel = x["nivel"]
            ndep = x["numero dependentes"]
            if nivel == 'A':
            	if ndep == 0:
		    data = salbruto - salbruto*0.03
		else:
		    data = salbruto - salbruto * 0.08
	    if nivel == 'B':
		if ndep == 0:
		    data = salbruto - salbruto * 0.05
		else:
		    data = salbruto - salbruto * 0.1
            if nivel == 'C':
		if ndep == 0:
		    data = salbruto - salbruto * 0.08
		else:
		    data = salbruto - salbruto * 0.15
            if nivel == 'D':
		if ndep == 0:
		    data = salbruto - salbruto * 0.10
		else:
		    data = salbruto - salbruto * 0.17
                    			
            print("Funcionario :" + nome + "Salario liquido: ", data)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            nome = y["nome"]
            salbruto = y["salario"]
            nivel = y["nivel"]
            ndep = y["numero dependentes"]
            if nivel == 'A':
            	if ndep == 0:
		    data = salbruto - salbruto*0.03
		else:
		    data = salbruto - salbruto * 0.08
	    if nivel == 'B':
		if ndep == 0:
		    data = salbruto - salbruto * 0.05
		else:
		    data = salbruto - salbruto * 0.1
            if nivel == 'C':
		if ndep == 0:
		    data = salbruto - salbruto * 0.08
		else:
		    data = salbruto - salbruto * 0.15
            if nivel == 'D':
		if ndep == 0:
		    data = salbruto - salbruto * 0.10
		else:
		    data = salbruto - salbruto * 0.17
                    			
            print("Funcionario :" + nome + "Salario liquido: ", data)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
