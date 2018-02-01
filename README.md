# guidebook_challenge

Problem to Solve and Solution:
The problem is based around finding the maximum of the array when given a shifted sorted list. 
My solution was to do a binary search on the sorted list, but instead of searching for a specific 
value, I searched for an index where array[index] > array[index+1]. This is because in the shifted sorted list,
 an index with this property must be the maximum of the array.

Algorithm Reasoning:
I chose to use a binary search algorithm to reach an amortized case of O(log(N)) performance time of finding the maximum, but
worst case the algorithm performs at O(N) peformance time due to certain edge cases.

My algorithm finds the middle, and then determines whether to search down the left or right half of a list under certain criteria.
If array[middle] is greater than the last element in the array, then the maximum must be on the right half. If array[middle] is less
than the last element in the array, then we know the maximum is on the left half. In the case where it's equal, then we compare array[middle]
to the start of the array instead. If array[start] > array[middle], then we know that the maximum is between start and middle. If array[start]
is less than array[middle], then we know the maximum is on the right half.

1. There is an edge case where array[middle] equals array[start] and array[len(array) - 1], in which case there is no way of determining
whether the maximum is on the left or right side of the split. In this case, we simply increment the start variable by 1, and try again. 
We can do this because if array[middle] = array[start], even if array[start] is the maximum, the maximum value will still be present in the
list at the middle index.

However, in the worst case scenario, we hit this edge case O(N) times, and thus the worst case performance is O(N). For example, this would
occur with the array [5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5].

There is another edge case where the whole list is shifted, thus making the list a sorted list. In this scenario, no index
has the property of array[index] > array[index] + 1. My implementation handles this by returning the last element of the list,
which should hold the maximum, if it can't find an index with this property.

2. Since it's binary search, where the list to be searched is halved on each recursion, the order of growth
time amortized is O(log(N)), but worst case the order of growth is O(N), again due to certain edge cases.

3. For a list of 1 million elements, my current implementation is both O(1) in space and amortized O(log(N)) in time performance-wise.
My solution also specifically uses a while loop, so there won't be any overflows on the stack caused by too large of a recursion depth.
Thus, I can't think of a more performant solution to this problem.
