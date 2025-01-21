# test_heapsort.py
from heapsort import heapsort

def test_heapsort():
    arr = [3, 5, 1, 10, 2, 7]
    print(f"Original array: {arr}")
    heapsort(arr)
    print(f"Sorted array: {arr}")

if __name__ == "__main__":
    test_heapsort()
