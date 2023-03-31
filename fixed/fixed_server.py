from utils.constants import *
from utils.util import *

DU_SIZE = 10

def run_fixed_server(du_size, server):
    print(du_size)
    f = open(WRITE_FILE, "w")
    while True:
        for i in range(FIXED_SIZE):
            m, a = server.recvfrom(du_size)
            m = m.decode("utf-8")
            f.write(m)
            if m == '':
                f.close()
                break

        server.sendto(f"ACK{FIXED_SIZE}".encode("utf-8"), a)
        if m == '':
            break
        
            
        

if __name__ == '__main__':
    server = get_socket()
    server.bind(('', PORT))
    print(f'Server listening on {PORT}')
    run_fixed_server(DU_SIZE, server)
    