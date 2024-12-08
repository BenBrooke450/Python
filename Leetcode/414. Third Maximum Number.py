
"""

Given an integer array nums, return the third distinct
 maximum number in this array. If the third maximum does not exist, return the maximum number.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


"""


def sorted_max(list1: list[int]) -> int:
    if len(list1) > 2:
        set1 = set(list1)
        list1 =list(set1)
        list1.sort(reverse=True)
        if len(list1) <= 2:
            return max(list1)
        else:
            return list1[2]
    else:
        return max(list1)


print(sorted_max([2,2,3,1]))