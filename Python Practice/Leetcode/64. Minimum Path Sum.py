
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

"""


def minPathSum(grid: list[list[int]]) -> int:

    cols = len(grid[0])
    rows = len(grid)
    path = []
    visited = set()
    sums = []
    print(rows,cols)

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited):
            if r+1 == rows and c+1 == cols:
                sums.append(sum(path))
                return
            else:
                return

        visited.add((r,c))
        path.append(grid[r][c])
        print(path,r,c,)

        dfs(r, c + 1)
        dfs(r + 1, c)


    count = 0
    c = 0

    for r in range(rows):
        dfs(r, c)
        visited = set()
        path = []

    return sums


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))





