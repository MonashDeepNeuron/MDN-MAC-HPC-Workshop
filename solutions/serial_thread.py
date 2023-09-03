import time

NUM_HELLOS = 2000000

if __name__ == '__main__':
    t1 = time.time()
    for i in range(NUM_HELLOS):
        print('Hello World x', i, end='\r')
    t2 = time.time()

    print('Total Execution Time: ', t2-t1)