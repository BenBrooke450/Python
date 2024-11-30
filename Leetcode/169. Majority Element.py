"""
Given an array nums of size n, return the
 majority element.

The majority element is the element that appears
 more than ⌊n / 2⌋ times. You may assume that the
 majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

def highest(list1 : list[int]):

    dic1 = {}

    for index, num in enumerate(list1):
        if num not in dic1.keys():
            dic1[num] = 1
        else:
            dic1[num] = dic1.get(num) + 1

    return max(dic1, key=dic1.get)

nums = [2,2,1,1,1,1,1,2,2]
print(highest(nums))




