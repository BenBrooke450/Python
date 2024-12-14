"""

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that
 has the maximum average value and return this value.
 Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""
from numpy.matlib import empty


def avg(nums: list[int], k: int):

    list1 = []

    for index,n in enumerate(len(nums) - k + 1):

        x = nums[index:index+k]
        if len(x) == 4:
            list1.append((sum(x)/k))

    return max(list1)


print(avg(nums = [1,12,-5,-6,50,3], k = 4))

















