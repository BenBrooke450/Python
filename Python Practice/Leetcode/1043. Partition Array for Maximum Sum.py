
"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.



Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

1,4,1,5,7,3,6,1,9,9,3
K = 4

Array can partitioned into at most k=4 size

1| 4,1,5,7 | 3,6,1,9 | 9,3
each value in partitioned subarray will be max of that sub array

1 -> 1* 1 = 1
7 -> 7 * 4 = 28
9 -> 9 * 4 = 36
9 -> 9 * 2 = 18
83

Example 3:
Input: arr = [1], k = 1
Output: 1

"""

import numpy as np
def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    for shift in range(k+2):
        chunks = []
        idx = 0
        print(k)
        while idx < len(arr):
            size = k
            if shift > 0:
                if len(chunks) == 0:
                    size = shift
                else:
                    size = k
            chunk = arr[idx:idx + size]
            if chunk:
                chunks.append(chunk)
            idx += size

        print(f"Shift {shift}: {chunks}")

print(maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))









