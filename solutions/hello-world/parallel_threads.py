import threading
import time

NUM = 200000

def print_thread1(num):
    for _ in range(num):
        print('Hello World from thread 1!', end='\r')

def print_thread2(num):
    for _ in range(num):
        print('Hello World from thread 2', end='\r')

if __name__ == "__main__":
    thread1 = threading.Thread(target=print_thread1, args=(NUM//2,))
    thread2 = threading.Thread(target=print_thread2, args=(NUM//2,))

    t1 = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    t2 = time.time()

    print('Total Execution Time: ', t2-t1)