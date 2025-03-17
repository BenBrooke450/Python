

"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.



Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""
import numpy as np

def findKthPositive(arr: list[int], k: int) -> int:

    set_diff = range(1,max(arr)+k+1)
    x = np.setdiff1d(set_diff,arr)
    x = x.tolist()
    return x[k-1]


print(findKthPositive(arr = [2,3,4,7,11], k = 5))













