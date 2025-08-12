

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














def combine(n: int, k: int) -> list[list[int]]:

    ran = []
    new = list(range(1, n+1))
    start = 0
    end = 1

    def com(ran: list[int], new, start, end, k):

        if start >= n or end > n:
            return

        part = new[start:k+start-1]
        part.extend(new[end:k+end-1])
        print(part)

        if len(part) == k and part not in ran:
            ran.append(part)

        if end + 1 < n:

            if end + 1 == n:
                com(ran, new, start, end + 1, k)


            else:
                com(ran, new, start, end + 1, k)

        if start + 1 < n:
            com(ran, new, start + 1, start + 2, k)

        return ran

    com(ran, new, start, end, k)

    return ran # ✅ added return here


print(combine(n = 6, k = 3))










