"""

We define a harmonious array as an
array where the difference between
its maximum value and its minimum value is exactly 1.

Given an integer array nums, return
the length of its longest harmonious subsequence
 among all its possible subsequences.



Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:
Input: nums = [1,1,1,1]
Output: 0
Explanation:
No harmonic subsequence exists.

"""



import numpy as np

def func(list1:list[int]):
    array2 = np.array([[x,list1.count(x)] for x in set(list1)])
    m = 0
    array3 = array2[np.argsort(array2[:, 0])]
    for i in np.arange(len(array2)-1):
        if array2[i,0] + 1 == array2[i+1,0]:
            plus = array2[i, 1] + array2[i + 1, 1]
            if plus > m:
                m = plus
    return m


print(func([1,3,2,2,5,2,3,7]))

print(func([-1,0,-1,0,-1,0,-1]))














#######################################





def func(list1:list[int]):
    array1 = np.array(list1)
    m = 0
    for n in array1:
        down_n = sum(1 for x in array1 if n == x or x == n - 1)
        up_n = sum(1 for x in array1 if n == x or x == n + 1)
        biggest = max(down_n,up_n)
        if biggest > m:
            m = biggest
    return m



print(func([1,3,2,2,5,2,3,7]))











#######################################










def func(list1:list[int]):

    sorted_list = sorted(list1)
    n = 0
    list2 = []

    for nums in sorted_list:
        for nums2 in sorted_list:
            if nums + 1 == nums2 or nums == nums2:
                list2.append(nums2)
        length = len(list2)
        if length > n and len(set(list2)) != 1:
            n = length
        list2 = []
    return n






