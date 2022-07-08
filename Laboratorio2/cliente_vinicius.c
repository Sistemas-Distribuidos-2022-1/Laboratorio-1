#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define PORT 8080
#define BSIZE 2048
#define SERVERNAME "localhost"

void Sal_Reaj(int sock, char *msg, char *buffer){
	int valread;
	char nome[30], cargo[30];
        float salario;
        sprintf(msg, "%s|%s|%.2f", nome, cargo, salario);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Nome: %s, salario reajustado: %s\n", nome, buffer);
}

void M_idade(int sock, char *msg, char *buffer){
	char nome[30], sexo[30];
        int idade, valread;
        sprintf(msg, "%s|%s|%d", nome, sexo, idade);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Nome: %s, %s\n", nome, buffer);
}

void Apr_Rpr(int sock, char *msg, char *buffer){
	int valread;
	float N1, N2, N3;
        sprintf(msg, "%.2f|%.2f|%.2f", N1, N2, N3);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Aluno foi  %s\n", buffer);
}

void Peso_Ideal(int sock, char *msg, char *buffer){
	int valread;
	float altura;
	char sexo[30];
        sprintf(msg, "%.2f|%s", altura, sexo);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Peso ideal  %s\n", buffer);
}

void Classificacao(int sock, char *msg, char *buffer){
	int idade, valread;
        sprintf(msg, "%d", idade);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Categoria:  %s\n", buffer);
}

void Sal_Liq(int sock, char *msg, char *buffer){
	float salbruto;
	char nome[30], nivel[30];
	int ndep, valread;
        sprintf(msg, "%s|%s|%.2f|%d", nome, nivel, salbruto, ndep);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Nome: %s, Salario Liquido: %s\n", nome, buffer);
}

void Aposentar(int sock, char *msg, char *buffer){
	int idade, tempo, valread;
        sprintf(msg, "%d|%d", idade, tempo);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Funcionario %s\n", buffer);
}

void Per_cred(int sock, char *msg, char *buffer){
	int saldo, valread;
        sprintf(msg, "%d", saldo);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("Saldo médio: %d, Percentual de Crédito %s\n", saldo, buffer);
}

void Cartas(int sock, char *msg, char *buffer){
	int num, naipe, valread;
        sprintf(msg, "%d|%d", num, naipe);
        send(sock, msg, strlen(msg), 0);

        valread = read(sock, buffer, BSIZE);
        printf("%s\n", buffer);
}

int main(int argc, char const *argv[]){
	
	int sock = 0, valread, client;
	struct sockaddr_in serv_addr;
	char buffer[BSIZE] = { 0 };
	char msg[BSIZE], data;
	
	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        	printf("\n Erro ao criar o Socket \n");
        	return -1;
    	}
  
    	serv_addr.sin_family = AF_INET;
    	serv_addr.sin_port = htons(PORT);

	// Converte endereco IPv4 e IPv6 para texto binario form
    	if (inet_pton(AF_INET, SERVERNAME, &serv_addr.sin_addr) <= 0 ) {
       		printf("\nEndereco IP invalido/ Endereco nao suportado \n");
        	return -1;
    	}

	if ((client = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0) {
        	printf("\nFalha na conexao \n");
        	return -1;
    	}

	printf("Conectado ao %s\n", SERVERNAME);

	//Escolher qual exercicio será resolvido
	valread = read(sock, buffer, BSIZE);
    	printf("%s\n", buffer);

	int aux=1;
	while(aux){
		int i;
		scanf("%d", &i);

		if(strcmp(msg, "0") == 0) return 0;

		sprintf(msg, "%d", i);

		//exemplo de como construir a mensagem
		//sprintf(msg, "%d|%s|%s|%.2f", i, nome, cargo, salario);
			
		//envio da mensagem para o server
		printf("Enviando mensagem:\n");
		send(sock, msg, strlen(msg), 0);

		valread = read(sock, buffer, BSIZE);
	    	printf("%s\n", buffer);
		printf("Recebido %s bytes\n", buffer);

		if(i == 1){
		    printf("Salario Reajustado.");
		    Sal_Reaj(sock, msg, buffer);
		}
		if(i == 2){
		    printf("Maioridade.");
		    M_idade(sock, msg, buffer);
		}
		if(i == 3){
		    printf("Aprovado ou Reprovado.");
		    Apr_Rpr(sock, msg, buffer);
		}
		if(i == 4){
		    printf("Peso Ideal.");
		    Peso_Ideal(sock, msg, buffer);
		}
		if(i == 5){
		    printf("Categoria Natação.");
		    Classificacao(sock, msg, buffer);
		}
		if(i == 6){
		    printf("Salario Liquido.");
		    Sal_Liq(sock, msg, buffer);
		}
		if(i == 7){
		    printf("Funcionario aposentar.");
		    Aposentar(sock, msg, buffer);
		}
		if(i == 8){
		    printf("Percentual de Credito.");
		    Per_cred(sock, msg, buffer);
		}
		if(i == 9){
		    printf("Baralho.");
		    Cartas(sock, msg, buffer);
		}	
	}

	// encerra socket de conexao
    	close(client);
   	return 0;	
}
