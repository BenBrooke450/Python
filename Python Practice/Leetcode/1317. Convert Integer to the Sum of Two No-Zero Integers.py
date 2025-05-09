

"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n

The test cases are generated so that there is at
 least one valid solution. If there are many valid solutions, you can return any of them.



Example 1:
Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:
Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.


"""
import numpy as np


def getNoZeroIntegers(n: int) -> list[int]:
    num_a = np.arange(1,n+1)
    for m in num_a:
        x = n - m
        q = [x,m]
        if any(r == "0" for r in str(x)) or any(r == "0" for r in str(m)):
            pass
        else:
            return q

print(getNoZeroIntegers(2))
















