from utils.constants import *
from utils.util import *

DU_SIZE = 10


def run_varied_server(du_size, server):
    print(du_size)
    size = 0
    f = open(WRITE_FILE, "w")
    while True:
        sz = (size % 3) + 1
        for i in range(sz):
            m, a = server.recvfrom(du_size)
            m = m.decode('utf-8')
            f.write(m)
            if m == '':
                f.close()
                break

        server.sendto(f"ACK{sz}".encode("utf-8"), a)
        if m == '':
            break
            
        size += 1

if __name__ == '__main__':
    server = get_socket()
    server.bind(('', PORT))
    print(f'Server listening on {PORT}')
    run_varied_server(DU_SIZE, server)