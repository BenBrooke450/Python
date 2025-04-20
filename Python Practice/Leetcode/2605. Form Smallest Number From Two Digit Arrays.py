


"""
Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.


Example 1:

Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
Example 2:

Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.
"""

import numpy as np
def minNumber(nums1: list[int], nums2: list[int]) -> int:

    common_num =  np.intersect1d(nums1,nums2)

    min_num1 = min(nums1)
    min_num2 = min(nums2)

    if min_num1 <= min_num2:
        second_num = int(str(min_num1) + str(min_num2))
    else:
        second_num = int(str(min_num2) + str(min_num1))

    return min(common_num,second_num)



print(minNumber(nums1 = [4,1,3], nums2 = [5,7]))
