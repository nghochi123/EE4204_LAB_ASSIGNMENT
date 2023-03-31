from socket import socket, AF_INET, SOCK_DGRAM
import sys
from .constants import PORT

def get_socket():
    return socket(AF_INET, SOCK_DGRAM)

def check_output_validity(first, second):
    pass

def get_address():
    if len(sys.argv) <= 2:
        return ("127.0.0.1", PORT)
    else:
        return (sys.argv[1], PORT)

def get_default_address():
    return ("127.0.0.1", PORT)

def send_all_packets(packets, client, address):
    for packet in packets:
        client.sendto(packet.encode("utf-8"), address)