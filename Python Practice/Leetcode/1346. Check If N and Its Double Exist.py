

"""
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

"""

import numpy as np
def checkIfExist(arr: list[int]) -> bool:
    arr = np.array(arr)
    if any(x / 2 in arr[i + 1:] or x / 2 in arr[:i] for i, x in enumerate(arr)):
        return True
    return False

print(checkIfExist([3,1,7,11]))