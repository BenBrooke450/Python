

"""
Given an integer n, return true if it is possible to represent n
    as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.



Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:
Input: n = 21
Output: false

"""
import itertools as it
import numpy as np
def checkPowersOfThree(n: int) -> bool:
    t = 0
    for x in range(1000):
        if 3**x >= n:
            t = x
            break

    threes = np.array([3**x for x in range(t+1)])

    for x in range(1,len(threes)+1):
        t = list(it.combinations(threes,x))
        print(t)
        if any(n == sum(y) for y in t):
            return True
    return False

print(checkPowersOfThree(27))











