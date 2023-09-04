import time
from utils import generate_random_list, merge

ARR_N = 500000

def merge_sort(arr):
    """
    Sorts an array in ascending order
    Returns a new sorted array

    Divide: Find the midpoint of the array and divide into subarrays
    Conquer: Recursively sort the subarrays created in previous step
    Combine: Merge the sorted subarrays created in previous step

    Takes O(n log n) time
    """
    if len(arr) <= 1:
        return arr

    # Splitting array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively calling merge_sort() for left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves
    return list(merge(left, right))

# Calling mergesort & Benchmarking
if __name__ == '__main__':
    
  arr = generate_random_list(ARR_N)
  print('\nSorting array of size', str(ARR_N) + '...')
  start = time.time()
  sorted_arr = merge_sort(arr)
  end = time.time()
  print(f'Array Sorted! Execution Time: {end-start} seconds')