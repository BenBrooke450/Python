
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

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current = nums[i] + nums[left] + nums[right]

            if abs(current - target) < abs(closest_sum - target):
                closest_sum = current

            if current < target:
                left += 1
            elif current > target:
                right -= 1
            else:
                return current

print(threeSumClosest(nums = [-1,2,1,-4], target = 1))

















def threeSumClosest(nums: list[int], target: int) -> int:

    lowest_num = 10000
    cloest_sum = 0

    nums = tuple(nums)

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):

            sum_nums = nums[i] + nums[j]

            diff = sum_nums - target

            if abs(diff) <= lowest_num:
                lowest_num = abs(diff)
                cloest_sum = sum_nums

                if diff == 0:
                    return abs(cloest_sum)

    return abs(cloest_sum)













from itertools import combinations, permutations
def threeSumClosest(nums: list[int], target: int) -> int:


    remainders = {abs(sum(x)-target):sum(x) for x in combinations(nums,3)}

    min_remainders = min(remainders.keys())

    remainders[min_remainders]

    return remainders[min_remainders],{sum(x):abs(sum(x)-target) for x in combinations(nums,3)}




print(threeSumClosest(nums = [0,-9,1,-4,3,13], target = -10))




