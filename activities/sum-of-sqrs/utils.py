def chunk_range(n, k):
    # check if the input is valid
    if not isinstance(n, int) or not isinstance(k, int) or n < 1 or k < 1:
        return None
    # calculate the size of each chunk
    chunk_size = n // k
    # calculate the remainder of the division
    remainder = n % k
    # initialize an empty list to store the tuples
    lst = []
    # initialize a start value for the range
    start = 1
    # loop through the number of chunks
    for i in range(k):
        # if there is a remainder, add one to the chunk size and decrement the remainder
        if remainder > 0:
            chunk_size += 1
            remainder -= 1
        # calculate the end value for the range
        end = start + chunk_size - 1
        # create a tuple of the start and end values and append it to the list
        lst.append((start, end))
        # update the start value for the next range
        start = end + 1
    # return the list of tuples
    return lst