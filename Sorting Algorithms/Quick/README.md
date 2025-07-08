# Quick Sort

- Time complexity

The worst case scenario for Quicksort is 
O
(
n
2
)
. This is when the pivot element is either the highest or lowest value in every sub-array, which leads to a lot of recursive calls. With our implementation above, this happens when the array is already sorted.

But on average, the time complexity for Quicksort is actually just 
O
(
n
log
n
).

