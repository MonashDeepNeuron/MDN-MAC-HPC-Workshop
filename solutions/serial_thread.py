import time

NUM = 200000

if __name__ == '__main__':
    t1 = time.time()
    for _ in range(NUM//2):
        print('Hello World!', end='\r')
    t2 = time.time()

    print('Total Execution Time: ', t2-t1)