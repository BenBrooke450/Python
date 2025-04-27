

"""
Given an integer array nums and an integer k,
    return true if there are two distinct indices i
     and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""




import numpy as np

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    nums = [[i,x] for i,x in enumerate(nums)]
    nums.sort(key = lambda x: x[1])
    print(nums)
    for n in range(len(nums)-1):
        if nums[n][1] == nums[n+1][1] and (abs(nums[n][0] - nums[n+1][0]) <= k):
            return True
    return False


print(containsNearbyDuplicate([1,2,3,1,2,3],2))



########################################################################



import numpy as np

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    t = 0
    nums = np.array(nums)
    p = len(nums)
    while t + k <= p:
        q = nums[t:t + k + 1]
        if len(q) != len(np.unique(q)):
            return True
        t = t + 1
    return False

print(containsNearbyDuplicate([1,2,3,1],3))





########################################################################


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    if any(abs(x - y) <= k and nums[x] == nums[y] for x in range(len(nums)) for y in range(x+1,len(nums))):
        return True
    return False

print(containsNearbyDuplicate([1,2,3,1],3))






