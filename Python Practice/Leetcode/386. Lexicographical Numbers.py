
"""
Given an integer n, return all the numbers in the range
 [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.



Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]

"""



def lexicalOrder(n: int) -> list[int]:

    res = []

    def dfs(cur):
        if cur > n:
            return
        res.append(cur)
        for i in range(10):
            dfs(cur * 10 + i)

    for i in range(1,10):
        dfs(i)
    return res

print(lexicalOrder(136))




import numpy as np
def lexicalOrder(n: int) -> list[int]:
    t = ["1","2","3","4","5","6","7","8","9"]
    i = 0
    array_n = np.arange(1,n+1)

    while True:
        array_n.sort()






