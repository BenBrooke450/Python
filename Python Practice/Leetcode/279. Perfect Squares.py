

"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

import math

def numSquares(n: int) -> int:

    minumum = [1 for x in range(n)]
    perfect_squares = tuple(i * i for i in range(1, n//2))


    def checker(number_list):

        start = 0
        for x in number_list:
            start += x
            per_squ = int(math.sqrt(start))

            if per_squ in perfect_squares and start != 1:
                print(start)

    checker(number_list=minumum)

    return minumum

print(numSquares(13))

print(numSquares(85))
