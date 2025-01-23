"""

Given an array nums containing n distinct numbers in
the range [0, n], return the only number in the range
that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all
numbers are in the range [0,3]. 2 is the missing number
 in the range since it does not appear in nums.


Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all
 numbers are in the range [0,2]. 2 is the missing number
  in the range since it does not appear in nums.



Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9
numbers, so all numbers are in the range [0,9].
 8 is the missing number in the range since it
 does not appear in nums.

"""
from sqlalchemy.sql.functions import random


def missingNumber(self, list1: List[int]) -> int:
    sorted_list = sorted(list1)
    i = 1
    if 1 not in list1:
        return 1
    elif 0 not in list1:
        return 0

    for index, nums in enumerate(sorted_list):
        if nums + 1 == sorted_list[i]:
            i = i + 1
            if len(list1) - 1 == index + 1:
                return max(list1) + 1
        else:
            return nums + 1


nums = [9,6,4,2,3,5,7,0,1]
nums1 = [0,1]
print(missing_num(nums1))


