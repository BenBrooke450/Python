

"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

"""

from itertools import combinations, permutations
def combine(n: int, k: int) -> list[list[int]]:

    ran = list(range(1,n+1))
    start = 1


    def com(ran: list[int],start,k):

        part = [start]
        part.extend(ran[start:k-1])
        print("Part :",part)

        if k < len(ran):
            k = k + 1
            com(ran, start, k)

        start = k
        k = k + start

        if start > len(ran):
            return part

        com(ran, start, k)

    com(ran,0,k)

print(combine(n = 8, k = 2))











def combine(n: int, k: int) -> list[list[int]]:

    all_list = set()

    for x in range(1,n-k+3):
        for y in range(1,n-k+3):
            if (x,y) not in all_list and (y,x) not in all_list and x != y:
                all_list.add((x,y))

    return [list(x) for x in all_list]
















