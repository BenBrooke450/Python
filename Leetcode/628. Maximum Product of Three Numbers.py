

"""

Given an integer array nums, find
 three numbers whose product is
  maximum and return the maximum product.



Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

"""
from sphinx.addnodes import index


def max_num(number_list : list[int]):

    if len(number_list) < 4:
        a = number_list[0]
        b = number_list[1]
        c = number_list[2]
        return a * b * c

    elif len(number_list) > 3:

        a = max(number_list)
        index_a = number_list.index(a)
        number_list[index_a] = 0
        b = max(number_list, key=abs)
        index_b = number_list.index(b)
        number_list[index_b] = 0
        c = max(number_list, key=abs)
        index_c = number_list.index(c)
        number_list[index_c] = 0

        if a*b*c < 0:
            pass



    return a, b, c, number_list




print(max_num([1,2,1,-1,-2,-3]))








