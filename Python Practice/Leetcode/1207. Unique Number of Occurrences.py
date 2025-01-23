
"""
Given an array of integers arr, return true if the
    number of occurrences of each value in the array is unique or false otherwise.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""
import numpy as np


def uniqueOccurrences(arr: list[int]) -> bool:

    list1 = []
    for n in set(arr):
        t = arr.count(n)
        if t in list1:
            return False
        else:
            list1.append(t)
    return True

print(uniqueOccurrences([1,2,2,1,1,3]))
#True







