
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


def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)

    i = n - 1
    while i >= 0:
        max_val = 0
        best = 0
        for j in range(i, min(i + k, n)):
            max_val = max(max_val, arr[j])
            length = j - i + 1
            total = max_val * length + dp[j + 1]
            best = max(best, total)
        dp[i] = best
        i -= 1

    return dp[0]

print(maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], k = 4))








import numpy as np
import itertools as it
def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    i = 0
    q = 0
    j = 0
    r = 0
    while i < len(arr):
        max_x = max(arr[j:j+k+1 - r])

        print(arr[j:j + k + 1 - r],len(arr[j:j + k + 1 - r]))

        if np.argmax(arr[j:j + k + 1]) + 1 == len(arr[j:j + k + 1]) and len(arr[j:j + k + 1]) > k :
            j = i + 1
            q = q + arr[i]
            r = 1
            print(q,arr[i])

        if i%k+2 == len(arr[j:j + k]) + 1:
            print(q, max_x,len(arr[j:j + k]))
            q = q + max_x*len(arr[j:j + k])
            j = i + 1
        i = i + 1

    return q

#print(maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))

#print(maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], k = 4))







import numpy as np
def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    q = 0
    for shift in range(k):
        chunks = []
        idx = 0
        while idx < len(arr):
            size = k
            if shift > k:
                shift = shift%k
            if shift > 0:
                if len(chunks) == 0:
                    size = shift
                else:
                    size = k
            chunk = max(arr[idx:idx + size])*len(arr[idx:idx + size])
            if chunk:
                chunks.append(chunk)
            idx += size
        t = sum(chunks)
        if t > q:
            q = t
    return q





import numpy as np
def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    for shift in range(k+1):
        chunks = []
        idx = 0
        while idx < len(arr):
            size = k
            if shift > k:
                shift = shift%k
            if shift > 0:
                if len(chunks) == 0:
                    size = shift
                else:
                    size = k
            chunk = arr[idx:idx + size]
            print(chunk)
            if chunk:
                chunks.append(chunk)
            idx += size

        print(f"Shift {shift}: {chunks}")










