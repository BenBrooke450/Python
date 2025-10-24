
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
    ugly = [1]  # first ugly number
    i2 = i3 = i5 = 0  # pointers for multiples of 2, 3, 5

    for _ in range(1, n):
        next2 = ugly[i2] * 2
        next3 = ugly[i3] * 3
        next5 = ugly[i5] * 5

        print(next2,next3,next5)

        next_ugly = min(next2, next3, next5)
        ugly.append(next_ugly)

        print(next_ugly,ugly)

        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1

    return ugly[-1]

print(nthUglyNumber(20))













