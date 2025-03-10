"""

The Fibonacci numbers, commonly denoted F(n)
+form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two
preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

"""


def fib(number:int):

    n = 1
    m = 1
    q = 0

    list1 = []

    for nums in range(0,number):
        z = n + q
        list1.append(z)
        q = z + n
        list1.append(q)
        n = q + z
        list1.append(n)
    list1.insert(0, 1)
    list1.insert(0,0)
    return list1[number]


print(fib(10))

