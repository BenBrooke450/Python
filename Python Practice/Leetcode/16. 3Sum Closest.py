
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

    lowest_num = 10000
    cloest_sum = 0

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):

            sum_nums = nums[i] + nums[j]

            diff = sum_nums - target

            if abs(diff) < lowest_num:


            if abs(diff) <= lowest_num:
                lowest_num = abs(diff)
                cloest_sum = sum_nums

                if diff == 0:
                    return abs(cloest_sum)

    return abs(cloest_sum)

print(threeSumClosest(nums = [-1,2,1,-4], target = 1))


def threeSumClosest(nums: list[int], target: int) -> int:

    lowest_num = 10000
    cloest_sum = 0

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for q in range(j+1,len(nums)):
                sum_nums =  nums[i] + nums[j] + nums[q]
                print(nums[i],nums[j],nums[q])
                diff = sum_nums - target

                if abs(diff) <= lowest_num:
                    lowest_num = abs(diff)
                    cloest_sum = sum_nums

                    if diff == 0:
                        return abs(cloest_sum)

    return abs(cloest_sum)

print(threeSumClosest(nums = [-1,2,1,-4], target = 1))




