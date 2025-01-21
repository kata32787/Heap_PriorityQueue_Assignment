# test_priority_queue.py
from priority_queue import insert, extract_max
from task import Task

def test_priority_queue():
    heap = []
    insert(heap, Task(1, 10, 0, 5))
    insert(heap, Task(2, 15, 1, 6))
    insert(heap, Task(3, 5, 2, 7))

    print(f"Extracted task: {extract_max(heap)}")
    print(f"Heap after extraction: {heap}")

if __name__ == "__main__":
    test_priority_queue()
