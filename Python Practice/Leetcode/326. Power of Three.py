

"""
Given an integer n, return true
 if it is a power of three. Otherwise,
  return false.

An integer n is a power of three,
 if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

"""
import math

def find_three(n : int):
    try:
        x = (math.log10(n) / math.log10(3))
        if (x)**3 == n:
            return True

    except ValueError:
        return False

    else:
        return False


print(find_three(9))


