

"""
You are given an array of integers nums.
    Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.



Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
Hence, we return 3.

"""


def longestMonotonicSubarray(nums: list[int]) -> int:
    m = 1
    t = 1
    q = 0
    for i,n in enumerate(nums):
        if len(nums) == i + 1:
            break
        elif  nums[i+1] > n:
            m = m + 1
            if n > m:
                q = m
        else:
            m = 1

    for i,n in enumerate(nums):
        if len(nums) == i + 1:
            break
        elif nums[i+1] < n:
            t = t + 1
            if t > q:
                q = t
        else:
            t = 1
    return q

print(longestMonotonicSubarray([1,4,3,3,2]))



















