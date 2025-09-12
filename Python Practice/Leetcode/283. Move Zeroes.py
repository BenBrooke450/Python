

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

"""


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    insert_pos = 0

    # Step 1: move all non-zeros forward
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # Step 2: fill the rest with zeros
    for i in range(insert_pos, len(nums)):
        nums[i] = 0








def moveZeroes(nums: list[int]) -> None:

    n_zeros = nums.count(0)

    def re_zero(nums):
        if sum(nums) == 0:
            return nums

        for i in range(len(nums)-1):
            if nums[i] == 0:
                nums.pop(i)
                re_zero(nums)
            else:
                return nums + [x * 0 for x in range(n_zeros)]

    return re_zero(nums)


print(moveZeroes([0,1,0,3,12]))




