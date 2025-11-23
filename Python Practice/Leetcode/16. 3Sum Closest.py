
"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

"""




def threeSumClosest(nums: list[int], target: int) -> int:

    nums.sort()
    closest_sum = float('inf')

    print(nums)

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current = nums[i] + nums[left] + nums[right]

            print(nums[:i+1],nums[left],nums[right:])
            print(nums[i], nums[left], nums[right])
            print("  ")

            if abs(current - target) < abs(closest_sum - target):
                closest_sum = current

            if current < target:
                left += 1
            elif current > target:
                right -= 1
            else:
                return current
    return closest_sum

print(threeSumClosest(nums = [0,-9,1,-4,3,13,-15,-2], target = 100))



