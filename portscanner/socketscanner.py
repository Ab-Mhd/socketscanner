#!/usr/bin/python3


# socket library used for connectivity

import socket

# socket object is created and defined.
# AF_INET used to define the socket and by designating the type of address the socket will communicate with(IP4)
# SOCK_STREAM used to define the protocol that the socket will use at the transport layer (TCP)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)
# defining static socket



target_ip = input("[+] Please enter target ip\n")
choice = int(input("[+] Would you like to scan using the first 1000(1) ports or specify one(2)?: [1/2]\n"))


# port scanner function declared
def portscanner(port):
    if sock.connect_ex((target_ip, target_port)):

        print("Port", port, " is closed")
    else:

        print("Port", port, " is open")


# execution

if choice == 1:
    for port in range(1, 1000):
        portscanner(port)
else:
    target_port = int(input("[+] Please enter target port\n"))
    portscanner(target_port)
