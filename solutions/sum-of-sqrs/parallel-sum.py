import multiprocessing as mp
import time
from utils import chunk_range

MAX_INT = 100000000
NUM_PROCS = 2

# define a function that calculates the sum of squares of a range of numbers
def sum_of_squares(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i * i
    return result

if __name__ == '__main__':
    # create a list of arguments for each chunk
    args = chunk_range(MAX_INT, NUM_PROCS)
    
    # create a pool of processes
    pool = mp.Pool(NUM_PROCS) # use NUM_PROC processes

    # start the timer
    start = time.time()

    # apply the function to each chunk in parallel and get the results
    results = pool.starmap(sum_of_squares, args)

    # stop the timer
    end = time.time()

    # print the results and the time elapsed
    print(f"Result: {sum(results)}")
    print(f"Time elapsed: {end - start} seconds")