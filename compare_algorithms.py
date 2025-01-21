# compare code
import time
from heapsort import heapsort
from quicksort import quicksort
from mergesort import mergesort

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

def compare_algorithms():
    arr = [3, 5, 1, 10, 2, 7] * 1000  # Test with a larger array

    # Heapsort
    arr_copy = arr.copy()
    print(f"Heapsort Time: {measure_time(heapsort, arr_copy)}")

    # Quicksort
    arr_copy = arr.copy()
    print(f"Quicksort Time: {measure_time(quicksort, arr_copy)}")

    # Mergesort
    arr_copy = arr.copy()
    print(f"Mergesort Time: {measure_time(mergesort, arr_copy)}")

if __name__ == "__main__":
    compare_algorithms()
