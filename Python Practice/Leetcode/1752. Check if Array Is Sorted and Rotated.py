
"""
Given an array nums, return true if the array
 was originally sorted in non-decreasing order,
  then rotated some number of positions (including zero).
   Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in
 an array B of the same length such
  that B[i] == A[(i+x) % A.length] for every valid index i.



Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

"""

import numpy as np
def check(nums: list[int]) -> bool:
    nums = np.array(nums)
    for n in nums:
        if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
            return True
        else:
            print(nums)
            nums = np.insert(nums,values=nums[-1],obj=0)
            nums = nums[:-1]
            print(nums)
    return False

print(check([6,10,6]))




###########################################################



import numpy as np
def check(nums: list[int]) -> bool:
    max_p = len(nums) - 1 - np.argmax(nums[::-1])
    nums =  nums[max_p+1:] + nums[:max_p + 1]
    print(nums)
    if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
        return True
    return False




###########################################################



import numpy as np
def check(nums: list[int]) -> bool:
    min_p = len(nums) - 1 - np.argmin(nums[::-1])
    nums = nums + nums
    max_p = min_p + int((len(nums)/2))
    print(min_p,max_p)
    nums = nums[min_p:max_p]
    print(nums)
    if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
        return True
    return False

















