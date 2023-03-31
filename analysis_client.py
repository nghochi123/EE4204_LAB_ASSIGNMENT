from varied.varied_client import run_varied_client
from fixed.fixed_client import run_fixed_client
from utils.util import get_socket, get_address
from time import sleep, perf_counter_ns
from utils.constants import READ_FILE, ANALYSIS_VARIED_FILE, ANALYSIS_FIXED_FILE
import os

if __name__ == '__main__':
    client = get_socket()
    address = get_address()
    f_s = os.path.getsize(READ_FILE)
    with open(ANALYSIS_VARIED_FILE, "w") as f:
        f.write("size,du,time\n")
        for du_size in range(1, 200):
            time = 0
            for j in range(5):
                start = perf_counter_ns()
                run_varied_client(du_size, client, address)
                end = perf_counter_ns()
                time += (end - start)
                sleep(0.3)
            time /= 5
            f.write(f"{f_s},{du_size},{time}\n")
    sleep(5)
    with open(ANALYSIS_FIXED_FILE, "w") as f:
        f.write("size,du,time\n")
        for du_size in range(1, 200):
            time = 0
            for j in range(5):
                start = perf_counter_ns()
                run_fixed_client(du_size, client, address)
                end = perf_counter_ns()
                time += (end - start)
                sleep(0.3)
            time /= 5
            f.write(f"{f_s},{du_size},{time}\n")