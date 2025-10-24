
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

    primes = set()
    l = 1
    x = 2

    while l < n:
        print(x,l,n)
        if x%2 == 0 or x%3 == 0 or x%5 == 0:
            if any(x%y == 0 for y in primes):
                pass
            else:
                 l = l + 1
        else:
            primes.add(x)
        x = x + 1
    return x

print(nthUglyNumber(20))













