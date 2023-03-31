from utils.constants import *
from utils.util import *
from socket import timeout
from time import sleep

DU_SIZE = 10

def run_fixed_client(du_size, client, address):
    count = 0
    packets = []
    
    f =  open(READ_FILE, "r", encoding='utf-8')
    while True:
        packet = f.read(du_size)
        packets.append(packet)
        if len(packets) >= FIXED_SIZE or packet == '':
            try:
                send_all_packets(packets, client, address)
                packets = []
                data, server = client.recvfrom(4)
            except timeout:
                print(f"Request Timed Out. {count}")
                count += 1
                if count >= 16:
                    print("Terminating...")
                sleep(1)
            if packet == '':
                break
    f.close()

if __name__ == '__main__':
    client = get_socket()
    address = get_address()
    run_fixed_client(DU_SIZE, client, address)
    
            