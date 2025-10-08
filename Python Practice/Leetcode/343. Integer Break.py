

"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.



Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.


Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

"""

def integerBreak(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4

    min_nums = [3 for x in range(n//3)]
    print(min_nums)

    if n-sum(min_nums) == 1 and len(min_nums) > 1:
        min_nums[-1] = min_nums[-1] + (n-sum(min_nums))
    else:
        if (n-sum(min_nums)) > 0:
            min_nums.append((n-sum(min_nums)))

    print(min_nums)

    h = 1
    for x in min_nums:
        h *= x

    return h

print(integerBreak(8))



