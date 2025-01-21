# Heapsort Analysis
Time Complexity
 Build the Max Heap:

The build_max_heap() function processes each node in the array. The time complexity for this step is 
𝑂
(
𝑛
)
O(n).
We iterate over the non-leaf nodes (from 
floor
(
𝑛
/
2
)
−
1
floor(n/2)−1 to 0) and apply the heapify() operation.
The heapify() operation takes 
𝑂
(
log
⁡
𝑛
)
O(logn) time for each node. However, most nodes are near the leaf level, where the height is small, reducing the cost. Hence, the overall complexity is 
𝑂
(
𝑛
)
O(n) (not 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)).
1.2 Sorting the Array (Heapsort):

The main Heapsort loop repeatedly extracts the maximum element and rebuilds the heap. For each extraction:

Extracting the max element: 
𝑂
(
log
⁡
𝑛
)
O(logn) (due to heapify()).
This extraction process occurs 
𝑛
−
1
n−1 times (since the heap size decreases with each extraction).
Therefore, the total time complexity for Heapsort is 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).

Conclusion:

Best Case: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)
Average Case: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)
Worst Case: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)
2. Space Complexity
The Heapsort algorithm is in-place, meaning it does not require extra space beyond the input array.
Space Complexity: 
𝑂
(
1
)
O(1), as we are only using a constant amount of extra space for variables and the recursion stack in the heapify() function.
3. Why O(n log n) for All Cases
Heapsort’s time complexity is 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) in all cases (best, average, worst) because the heap structure always maintains the property where the largest (or smallest, in the case of a min-heap) element is at the root. Extracting the root element always requires 
𝑂
(
log
⁡
𝑛
)
O(logn) time due to the need to "heapify" the remaining tree. The building of the heap also takes linear time, 
𝑂
(
𝑛
)
O(n), and so the sorting process remains 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).
# the results is as below:
Original array: [3, 5, 1, 10, 2, 7]
Sorted array: [1, 2, 3, 5, 7, 10]

# Comparison of Heapsort with Other Sorting Algorithms
To compare the performance of Heapsort with other popular sorting algorithms, we implemented Quicksort and Mergesort and measured their execution times on the same input array. The comparison was done using a larger array to observe the differences in performance.

# Sorting Algorithms Implemented
Heapsort: We used the previously implemented Heapsort algorithm that builds a max-heap and then extracts the maximum element to sort the array.
Quicksort: A divide-and-conquer sorting algorithm that partitions the array around a pivot and recursively sorts the subarrays. Quicksort generally has an average time complexity of 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn), but it can degrade to 
𝑂
(
𝑛
2
)
O(n 
2
 ) in the worst case when the pivot is poorly chosen.
Mergesort: Another divide-and-conquer algorithm with a consistent time complexity of 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) in all cases. It splits the array into halves, recursively sorts them, and merges the sorted subarrays.
4.2 Time Measurement
We ran the three algorithms on an array of 6000 elements, which were repeated from a smaller test array to simulate larger input sizes. The time taken for each algorithm to sort the array was measured in seconds.
# THE OUTPUT BELOW
Heapsort Time: 0.0687398910522461 seconds
Quicksort Time: 0.005563259124755859 seconds
Mergesort Time: 0.06683874130249023 seconds
# Analysis of Results
Quicksort performed the best with the lowest execution time of 0.00556 seconds. This is typical for Quicksort in practice, especially when the pivot selection is good. Quicksort's average time complexity is 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn), but it benefits from better constants in practical scenarios when the pivot is chosen wisely.

Heapsort took 0.0687 seconds to sort the array. While it has a consistent 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) time complexity in all cases, it tends to have slightly higher overhead due to the need for maintaining the heap structure throughout the sorting process.

Mergesort was very close to Heapsort with a time of 0.0668 seconds. Like Heapsort, Mergesort has 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) time complexity, but it requires additional space to perform the merge step.

# Observations and Conclusion
For this specific test case, Quicksort showed the best performance due to its efficient in-place sorting mechanism.
Heapsort and Mergesort had similar performance in terms of time, though Mergesort has the added overhead of additional space complexity due to the need for temporary arrays during the merge step.
# Explanation of the Test Result
In this test:

We first inserted three tasks with the following priorities:

Task 1: Priority 10
Task 2: Priority 15
Task 3: Priority 5
After inserting the tasks, the heap was correctly organized such that Task 2 (the one with the highest priority of 15) was at the root.

When we called extract_max(), Task 2 was extracted as expected. The remaining heap now contains:

Task 1: Priority 10
Task 3: Priority 5
The remaining tasks were reheapified, and the new root became Task 1 with priority 10. The heap after extraction maintained the correct max-heap structure.