

"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.



Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.


Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.


"""

from itertools import combinations, permutations
def splitArray(nums: list[int], k: int) -> int:

    a = k - 1
    b = len(nums)
    i = 0

    def shuffle(m,n):
        for x in range(m,n):
            print(nums[:m],nums[m:x],nums[x:n],nums[n:])

        if m == 0:
            return

        shuffle(m-1,n-1)

    shuffle(a,b)




print(splitArray(nums = [7,2,5,10,8,11,2,3,4,2,1,23,3,4,55,33], k = 4))



















