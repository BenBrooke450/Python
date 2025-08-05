

"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

"""

import numpy as np
def numberOfSubarrays(nums: list[int], k: int) -> int:
    t = 0
    for x in range(0,len(nums)):

        if sum(1 for x in nums if x % 2 != 0) == k:
            t = t + 1

        start = nums[x + 1:]
        if sum(1 for x in start if x % 2 != 0) == k:
            t = t + 1

        end = nums[:-x - 1]
        if sum(1 for x in end if x % 2 != 0) == k:
            t = t + 1

        print("start:",start,"  end:",end)

    return t

print(numberOfSubarrays(nums = [1,1,1,1,1], k = 3))
#print(numberOfSubarrays(nums = [2,4,6], k = 1))
#print(numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))







