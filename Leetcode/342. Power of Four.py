"""

Given an integer n, return true if it is
 a power of four. Otherwise, return false.

An integer n is a power of four, if there
 exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true

"""

import math


def find_four(n : int):
    try:
        x = round((math.log10(n) / math.log10(4)),0)
        if ((4)**x) == n:
            return True

    except ValueError:
        return False

    else:
        return False


print(find_four(3))






