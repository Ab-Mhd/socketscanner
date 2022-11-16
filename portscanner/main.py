#!/usr/bin/python3


# socket library used for connectivity

import socket

# socket object is created and defined.
# AF_INET used to define the socket and by designating the type of address the socket will communicate with(IP4)
# SOCK_STREAM used to define the protocol that the socket will use at the transport layer (TCP)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# defining static socket

target_ip =input("[+] Please enter target ip\n")
target_port = int(input("[+] Please enter target port\n"))


# port scanner function declared
def portscanner(port):
    if sock.connect_ex((target_ip, target_port)):

        print("Port", port, " is closed")
    else:

        print("Port", port, " is open")


# function call
portscanner(target_port)