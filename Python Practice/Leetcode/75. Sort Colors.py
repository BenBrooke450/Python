
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

"""
import numpy as np
def sortColors(nums: list[int]) -> None:

    nums_array = np.array(nums)
    zeros = np.count_nonzero(nums_array == 0)
    ones = np.count_nonzero(nums_array == 1)
    twos = np.count_nonzero(nums_array == 2)

    for i in range(len(nums)):
        print(nums)
        if i < zeros:
            nums[i] = 0
        elif i < zeros + ones:
            nums[i] = 1
        else:
            nums[i] = 2


print(sortColors(nums = [0]))


