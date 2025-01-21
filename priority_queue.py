# priority_queue.py
from task import Task

def heapify(heap, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left].priority > heap[largest].priority:
        largest = left
    if right < n and heap[right].priority > heap[largest].priority:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, n, largest)

def insert(heap, task):
    heap.append(task)
    i = len(heap) - 1
    while i > 0 and heap[(i - 1) // 2].priority < heap[i].priority:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2

def extract_max(heap):
    if len(heap) == 0:
        return None
    if len(heap) == 1:
        return heap.pop()
    root = heap[0]
    heap[0] = heap.pop()
    heapify(heap, len(heap), 0)
    return root
