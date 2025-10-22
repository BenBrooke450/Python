
"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

"""


def nthUglyNumber(n: int) -> int:

    non_ugly = [1]
    x = 1
    while len(non_ugly) != n:
        x = x + 1
        if x%2 == 0 or x%3 == 0 or x%5 == 0:
            non_ugly.append(x)
            if len(non_ugly) == n:
                break

    return non_ugly

print(nthUglyNumber(10))











