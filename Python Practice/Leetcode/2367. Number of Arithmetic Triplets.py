


"""


You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.



Example 1:
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.


Example 2:
Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.


"""

def triple(list1:list[int] , n : int):

    list2 = []
    m = 0

    for nums in list1:
        for nums2 in list1:
            if nums2 < nums and (nums - nums2 == n):
                list2.append(nums2)
            elif nums2 > nums and (nums2 - nums == n):
                list2.append(nums2)

        if len(list2) == 2:
            m = m + 1
            list2 = []
        else:
            list2 = []
    return m


print(triple([4,5,6,7,8,9], 2))
#2






