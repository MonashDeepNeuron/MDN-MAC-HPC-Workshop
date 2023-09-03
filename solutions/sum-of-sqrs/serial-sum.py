import time

MAX_INT = 100000000

# define a function that calculates the sum of squares of a range of numbers
def sum_of_squares(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i * i
    return result

if __name__ == '__main__':
    # start the timer
    start = time.time()

    # calculate the sum of squares of all numbers from 1 to MAX_INT
    result = sum_of_squares(1, MAX_INT)

    # stop the timer
    end = time.time()

    # print the result and the time elapsed
    print(f"Result: {result}")
    print(f"Time elapsed: {end - start} seconds")