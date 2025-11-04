

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

    perfect_squares = [i * i for i in range(1, n)][::-1]
    number_list= []
    perfect_list = []

    def checker(i):

        if sum(number_list) == n:
            perfect_list.append(number_list.copy())
            return

        if sum(number_list) > n or i >= len(perfect_squares):
            return

        number_list.append(perfect_squares[i])
        checker(i)           # reuse the same square
        number_list.pop()

        # move to next square
        checker(i + 1)


    checker(0)

    return min(perfect_list, key=lambda x:len(x))

print(numSquares(165))




##########################################
#CHATCPT
def numSquares(self, n: int) -> int:
    perfect_squares = [i * i for i in range(1, int(n**0.5) + 1)][::-1]
    min_length = float('inf')

    def checker(i, current_sum, count):
        nonlocal min_length

        if count >= min_length:
            return

        if current_sum == n:
            min_length = min(min_length, count)
            return

        if current_sum > n or i >= len(perfect_squares):
            return

        checker(i, current_sum + perfect_squares[i], count + 1)

        checker(i + 1, current_sum, count)

    checker(0, 0, 0)
    return min_length