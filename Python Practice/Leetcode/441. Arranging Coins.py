
"""

You have n coins and you want to build a staircase with these coins.
 The staircase consists of k rows where the ith row has exactly i coins.
  The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of
the staircase you will build.

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.



Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

"""

def coins(number :int):
    n = 0
    m = 0

    list1 = []
    for nums in range(1, number + 1):
        if number == 1 or number == 2:
            return 1
        elif m < number:
            m = m + n + 1
            n = n + 1
            list1.append(m)
        else:
            if number in list1:
                return n
            else:
                return n - 1



print(coins(10))







