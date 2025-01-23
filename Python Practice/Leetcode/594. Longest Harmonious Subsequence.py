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


print(func([1,3,2,2,5,2,3,7]))
#5



