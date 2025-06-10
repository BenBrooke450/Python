
"""
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e., 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array, return the minimum number of operations needed to make all the elements of arr equal.



Example 1:
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:
Input: n = 6
Output: 9

"""

import numpy as np


def minOperations(n: int) -> int:
    i = 0
    j = 1
    extra = 1
    two = 0
    while j != n:
        print(i,extra)
        i = i + extra
        two = two + 1
        if two == 2:
            two = 0
            extra = extra + 1
        j = j + 1
    return i

print(minOperations(5))









def minOperations(n: int) -> int:
     x = list((np.arange(n))*2 + 1)
     i = 0
     j = len(x) - 1
     t = 0

     while i + 1 < j:

         x[i] = x[i] + 1
         x[j] = x[j] - 1
         if x[i] == len(x) and x[j] == len(x):
             i = i + 1
             j = j - 1
         t = t + 1
     return t + 1



"""0 1
1 2
2 3
4 4
6
9
12
16
20
25
30
36
42
29"""










