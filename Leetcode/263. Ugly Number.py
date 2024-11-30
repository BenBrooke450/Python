"""


An ugly number is a positive integer
which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if
n is an ugly number.



Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3


Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.


Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it
includes the prime factor 7.


"""

# so any prime number except 2 3 5 that can go into a number is false,
# i.e the number can only be divided by those three prime numbers
  # if it can be done nby any other then it´s false


def ugly(n: int):

    out = []

    for num in range(6, n + 1):
        if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
            if num % n == 0:
                return False

    return True

print(ugly(2147483647))





####################################################################


def ugly(n: int):

    out = []

    for num in range(6, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            out.append(num)

    for nums in out:
        if nums % n == 0:
            return False

    return True

print(ugly(4))





####################################################################


def ugly(number: int):
    out = list()
    for num in range(1, n+1):
        print(list(num % i != 0 for i in range(2, num)),num)
        if all(num % i != 0 for i in range(2, num)):
            out.append(num)
    return out

