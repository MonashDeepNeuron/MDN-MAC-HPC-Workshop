import time
from multiprocessing import Pool

NUM_HELLOS = 2000000
NUM_PROCS = 2

def print_hello(i):
    print('Hello World x', i, end='\r')

if __name__ == "__main__":
    start = time.time()

    pool = Pool(NUM_PROCS)
    pool.map(print_hello, range(NUM_HELLOS//NUM_PROCS))
    pool.close()
    pool.join()

    end = time.time()

    print('Total Execution Time: ', end-start)