

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.



Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


"""

import numpy as np

def jump(nums: list[int]) -> int:

    place = 0

    jumps = nums[0]

    n = len(nums) - 1

    j = 0

    if len(nums) == 1:
        return 0

    if nums[0] >= len(nums[1:]):
        return 1

    while place < n:

        j += 1

        print(nums[place+1:jumps+1])

        max = 0
        for i,x in enumerate(nums[place+1:jumps+1]):
            test_max = x + i
            if test_max > max:
                biggest_jump = i + 1
                max = test_max

        place =  biggest_jump + place

        jumps = nums[place] + place

        print("place:",place, "    we pick: ", nums[place])

        if jumps >= n:
            j += 1
            break

    return j

print(jump(nums = [3,1,3,4,1,1,3,1,3,2,3,1,5,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1]))













