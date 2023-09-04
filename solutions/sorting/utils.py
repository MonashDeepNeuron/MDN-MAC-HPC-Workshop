import random

def generate_random_list(n):
    """
    Generates a list of size n with random integers between 1-1000
    """
    return [random.randint(1, 1000) for _ in range(n)]

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """
    # Two pointers for traversing the two halves
    left_pointer = 0
    right_pointer = 0

    merged = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            merged.append(left[left_pointer])
            left_pointer += 1
        else:
            merged.append(right[right_pointer])
            right_pointer += 1

    # Add remaining elements to merged list
    merged += left[left_pointer:]
    merged += right[right_pointer:]

    return merged