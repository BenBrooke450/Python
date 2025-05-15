

"""
Given an array of integers arr, return true if we can partition the
 array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes
    i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1]
     + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])



Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


"""

import numpy as np


def has_three_equal_parts(arr):
    arr = np.array(arr)
    total = np.sum(arr)

    if total % 3 != 0:
        return False

    target = total // 3
    cumsum = np.cumsum(arr)

    # First part ends at i where cumsum[i] == target
    # Second part ends at j where cumsum[j] == 2 * target

    for i in range(len(arr)):
        if cumsum[i] != target:
            continue
        for j in range(i + 1, len(arr) - 1):
            if cumsum[j] == 2 * target:
                # If third part sum is also target, return True
                return True

    return False



###################################################################


import numpy as np

def canThreePartsEqualSum(arr: list[int]) -> bool:
    arr = np.array(arr)
    cumsum = np.cumsum(arr)
    print(cumsum)
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            sum1 = cumsum[i]
            sum2 = cumsum[j] - cumsum[i]
            print("stage1:",sum1,sum2)
            if sum1 != sum2:
                continue
            for z in range(len(arr)-1,0,-1):
                sum3 = cumsum[-1] - cumsum[z]
                print("stage2:", cumsum[j], sum3, cumsum[z])
                if sum2 == sum3:
                    return True
    return False

print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))




###################################################################


import numpy as np
def canThreePartsEqualSum(arr: list[int]) -> bool:
    arr = np.array(arr)
    for i in np.arange(1, len(arr) - 1):
        for j in np.arange(i, len(arr) - 1):
            if np.sum(arr[:i]) != np.sum(arr[i:j+1]):
                continue
            for z in np.arange(j, len(arr)-1):
                if np.sum(arr[i:j+1]) == np.sum(arr[j+1:]):
                    return True
    return False

###################################################################



import numpy as np
class Solution:
    def canThreePartsEqualSum(arr: list[int]) -> bool:
        if any(sum(arr[:i]) == sum(arr[i:j+1]) and sum(arr[i:j+1]) == sum(arr[j+1:])
            for i in np.arange(1,len(arr)-1)
            for j in np.arange(i,len(arr)-1)
            for z in np.arange(j,len(arr))-1):
                return True
        return False





