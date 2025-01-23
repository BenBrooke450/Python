



"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:
Input: nums = [2,2,1]
Output: 1


Example 2:
Input: nums = [4,1,2,1,2]
Output: 4


Example 3:
Input: nums = [1]
Output: 1

"""



def only_one(list_number: list[int]):
    sort_list = sorted(list_number)

    j = 0

    while j < len(sort_list):
        try:
            if sort_list[j] == sort_list[j + 1]:
                j = j + 2
            else:
                return sort_list[j]
        except IndexError:
            return sort_list[j]




print(only_one([1,1,2,2]))






