

"""
Given an binary array nums and an integer k,
    return true if all 1's are at least k
     places away from each other, otherwise return false.



Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

"""



def kLengthApart(nums: list[int], k: int) -> bool:
    t = 0
    for n in nums:
        if n == 1:
            if t > 0:
                return False
            else:
                t = k
        else:
            if t <= 0:
                t = 0
            else:
                t = t - 1
    return True








