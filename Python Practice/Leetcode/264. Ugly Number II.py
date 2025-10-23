
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

import math

def nthUglyNumber(n: int) -> int:

    primes = set()

    def is_prime(x):
        if x < 2:
            return False
        for y in range(2, int(math.isqrt(x)) + 1):
            if x % y == 0:
                return False
        return True


    for x in range(n - 1, 1, -1):  # start from n-1 and go down
        if not is_prime(x):
            return x


print(nthUglyNumber(10))





def nthUglyNumber(n: int) -> int:

    primes = set()

    for x in range(6,n+40):
        if all(x%y!=0 for y in range(2,x) if y != x):
            primes.add(x)

    x = 0
    list1 = []
    while x != n:
        if x not in primes and all(x%y!=0 for y in primes):
            list1.append(x)
        else:
            n = n + 1
        x = x + 1

    return list1[-1]













