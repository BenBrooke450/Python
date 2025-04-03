

"""
Given a non-empty array of non-negative integers nums,
    the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length
    of a (contiguous) subarray of nums, that has the same degree as nums.



Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

"""


import numpy as np
def findShortestSubArray(nums: list[int]) -> int:

    #degree = max(nums, key = lambda x: nums.count(x))
    count_of_degree = max([nums.count(x) for x in set(nums)])
    list1 = np.array([x for x in set(nums) if nums.count(x) == count_of_degree])
    print(list1)
    t = 1000000
    for n in list1:
        first_n = nums.index(n)
        last_n = len(nums) - nums[::-1].index(n)
        print(first_n,last_n)
        if len(nums[first_n:last_n]) < t:
            t = len(nums[first_n:last_n])

    return t







######################################################



def findShortestSubArray(nums: list[int]) -> int:

    #degree = max(nums, key = lambda x: nums.count(x))
    count_of_degree = max([nums.count(x) for x in set(nums)])
    list1 = [x for x in set(nums) if nums.count(x) == count_of_degree]
    print(list1)
    t = 1000000
    for n in list1:
        first_n = nums.index(n)
        last_n = len(nums) - nums[::-1].index(n)
        print(first_n,last_n)
        if len(nums[first_n:last_n]) < t:
            t = len(nums[first_n:last_n])

    return t



print(findShortestSubArray([1,3,2,2,3,1]))




print(findShortestSubArray([1,2,2,3,1,4,2]))












