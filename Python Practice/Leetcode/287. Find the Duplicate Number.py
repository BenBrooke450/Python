

"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
"""


def findDuplicate(nums: list[int]) -> int:

    n = len(nums) - 1
    xor_all = 0

    for num in nums:
        xor_all ^= num

    for i in range(1, n + 1):
        xor_all ^= i

    return xor_all

print(findDuplicate([1,3,4,2,2]))












