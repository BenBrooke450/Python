"""


A perfect number is a positive integer that is equal to the sum of
 its positive divisors, excluding the number itself. A divisor of
 an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.


Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.


Example 2:

Input: num = 7
Output: false

"""



def checkPerfectNumber(number: int) -> bool:

    divisors = 1

    print(number ** 0.5)

    for x in range(2, int(number ** 0.5) + 1):
        print(divisors)
        if number % x == 0:
            divisors = divisors + x
            if x != number // x:
                divisors += number // x

    if divisors == number:
        return True

    return False


print(checkPerfectNumber(28))








