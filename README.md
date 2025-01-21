# Heap_PriorityQueue_Assignment
# Instructions Breakdown:
Cloning: The first step is to clone the repository using git clone.
Dependencies: Since this is a Python project with no external dependencies, we will be using Python 3.x.
Running the Code: i have provided the necessary commands to execute each script for Heapsort, algorithm comparison, and priority queue tests.
# summary of the findings
# Heapsort Results
When running the Heapsort algorithm on the input array [3, 5, 1, 10, 2, 7], the original and sorted arrays were as follows:

Original array: [3, 5, 1, 10, 2, 7]
Sorted array: [1, 2, 3, 5, 7, 10]
Heapsort was able to correctly sort the array in ascending order, demonstrating the correct implementation of the heap property and sorting procedure.

# Algorithm Comparison
We compared the performance of Heapsort, Quicksort, and Mergesort using the following execution times for a larger array of 6000 elements:

Heapsort Time: 0.0687398910522461 seconds
Quicksort Time: 0.005563259124755859 seconds
Mergesort Time: 0.06683874130249023 seconds
Analysis:

Quicksort was the fastest with a significantly lower execution time, benefiting from its efficient partitioning strategy.
Heapsort and Mergesort performed similarly in terms of time, with Heapsort being slightly slower. Both have 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) time complexity, but Heapsort has additional overhead due to heap structure maintenance, while Mergesort requires extra space for merging.
# Priority Queue Test
For the Priority Queue implementation, we tested the insertion of tasks with different priorities and extracted the highest-priority task. Here is the output of the test:

Extracted task: Task(2, Priority: 15)
Heap after extraction: [Task(1, Priority: 10), Task(3, Priority: 5)]
Analysis:

The highest-priority task, Task(2) with priority 15, was correctly extracted from the priority queue.
After extraction, the heap was restructured, and the next highest-priority task, Task(1) with priority 10, was moved to the top.
This test confirmed that the priority queue was functioning as expected, maintaining the heap property and correctly managing tasks based on their priority.