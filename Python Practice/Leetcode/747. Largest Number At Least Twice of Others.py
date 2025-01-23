


"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice
    as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.



Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
"""

import numpy as np

def dominantIndex(nums: list[int]) -> int:

    arrays_nums = np.array(nums)

    max_num = max(arrays_nums)

    sorted_array = np.sort(arrays_nums)

    if  max_num/2 >= (sorted_array[-2]):
        x = np.where(arrays_nums == max_num)
        return int(x[0][0])
    else:
        return -1

print(dominantIndex([3,6,1,0]))
#1













