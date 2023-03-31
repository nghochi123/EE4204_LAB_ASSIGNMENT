from varied.varied_server import run_varied_server
from fixed.fixed_server import run_fixed_server
from utils.util import get_socket
from utils.constants import PORT
from time import sleep

if __name__ == '__main__':
    server = get_socket()
    server.bind(('', PORT))
    print(f'Server listening on {PORT}')
    for du_size in range(1, 200):
        for j in range(5):
            run_varied_server(du_size, server)
    sleep(5)
    for du_size in range(1, 200):
        for j in range(5):
            run_fixed_server(du_size, server)