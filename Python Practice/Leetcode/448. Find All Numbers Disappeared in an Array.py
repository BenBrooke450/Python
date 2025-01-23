"""

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]


Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

"""
import numpy as np


def not_there(array1:np.array):
    return (np.setxor1d(array1,np.arange(1,len(array1)+1))).tolist()


print(not_there([1,1]))



