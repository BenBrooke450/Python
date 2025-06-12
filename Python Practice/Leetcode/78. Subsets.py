

"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

"""
from itertools import chain, combinations
import numpy as np
def subsets(nums: list[int]) -> list[list[int]]:
    x = chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))
    return [list(y) for y in x]


print(subsets([1,2,3]))






