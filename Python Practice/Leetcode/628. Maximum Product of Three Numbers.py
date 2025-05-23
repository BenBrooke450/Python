

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


def maximumProduct(number_list: list[int]) -> int:
    number_list.sort()
    if len(number_list) < 6:
        t = -1000000
        for i,x in enumerate(number_list[:-2]):
            for j,y in enumerate(number_list[i+1:-1]):
                for z in number_list[j+1:]:
                    print(x,y,z)
                    if x*y*z > t:
                        t = x*y*z

    elif len(number_list) >= 6:
        nums = number_list[:3] + number_list[-3:]
        t = -1000000
        for i,x in enumerate(nums[:-2]):
            for j,y in enumerate(nums[i+1:-1]):
                for z in nums[j+1:]:
                    print(x,y,z)
                    if x*y*z > t:
                        t = x*y*z
    return t

print(maximumProduct([1,2,3]))
print(maximumProduct([-5,-3,1,2,1,-1,-2,-3,3,4,5,23,-10]))













########################################################


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












