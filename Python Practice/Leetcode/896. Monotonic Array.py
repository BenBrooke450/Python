

"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.



Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

"""




def isMonotonic(nums: list[int]) -> bool:
    if all(nums[x] <= nums[x+1] for x in range(len(nums)-1)):
        return True
    elif all(nums[x] >= nums[x+1] for x in range(len(nums)-1)):
        return True
    else:
        return False








##########################################################





def isMonotonic(nums: list[int]) -> bool:
    def generate_until_break(iterable, break_condition):
        for index, item in enumerate(iterable):
            if break_condition(index):
                break
            yield index, item

    # Check for non-decreasing order
    if all(nums[i] <= nums[i + 1] for i, _ in generate_until_break(nums, lambda i: len(nums) == i + 1)):
        return True
    # Check for non-increasing order
    elif all(nums[i] >= nums[i + 1] for i, _ in generate_until_break(nums, lambda i: len(nums) == i + 1)):
        return True
    else:
        return False

print(isMonotonic([6,5,4,4]))







