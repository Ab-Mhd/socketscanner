#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>
#include <netinet/in.h>
#include <string.h>
#include <stdlib.h>
#include <arpa/inet.h>


int main(int argc, char const* argv[]) {


//Defining the socket, AF_INET = IPV4, SOCK_STREAM = TCP, 0 = IP

int sockfd = socket(AF_INET,SOCK_STREAM,0);
int addr=0;


//buffer to store user input
char buffer[1024] = {0};

struct sockaddr_in address;
printf("Please enter target IPV4 address:\n");

/*
fgets()
printf("%d",valread);
*/



address.sin_family = AF_INET;
address.sin_addr.s_addr = inet_addr("68.178.157.132");
address.sin_port= 8888;

    return 0;



}
