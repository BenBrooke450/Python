
"""
Given an integer array nums, return the greatest common
    divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the
    largest positive integer that evenly divides both numbers.



Example 1:
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

Example 2:
Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

Example 3:
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
"""

import numpy as np

def findGCD( nums: list[int]) -> int:

    array_nums = np.array(nums)

    min_array = min(array_nums)
    max_array = max(array_nums)

    for x in np.arange(0,min_array+1)[::-1]:
        if min_array % x == 0 and max_array % x == 0:
            return int(x)

print(findGCD([2,5,6,9,10]))






