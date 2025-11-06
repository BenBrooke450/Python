

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


def splitArray(nums: list[int], k: int) -> int:

    b = len(nums)
    biggest_length = len(nums) - (k - 1)
    if k == 2:
        biggest_length = len(nums) - 1
    small_max = []

    def shuffle(biggest_length):
        for i in range(b - biggest_length + 1):
            print(i,nums[i:i + biggest_length],sum(nums[i:i + biggest_length]))
            q = sum(nums[i:i + biggest_length])
            if q > 0:
                small_max.append(q)

        if biggest_length == k + 1:
            return

        shuffle(biggest_length-1)

    shuffle(biggest_length)

    return min(small_max)




print(splitArray(nums = [7,2,5,10,8], k = 2))



print(splitArray(nums = [7,2,5,10,8,11,2,3,4,2,1,23,3,4,55,33], k = 4))




"""len 6 = 5 , 1 group 2
len 6 = 4, 1, 1 group 3
len 6 = 3, 1, 1 ,1 group 4

len 7 = 6 , 1 group 2
len 7 = 5 , 1, 1 group 3

len 10 = 9 , 1 group 2
len 10 = 8, 1 , 1 group 3"""






























