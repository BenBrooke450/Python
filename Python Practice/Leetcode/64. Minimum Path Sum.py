
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
    sums = []

    def dfs(r, c):
        # if out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        # add current cell
        path.append(grid[r][c])

        # if we reached bottom-right, record path sum
        if r == rows - 1 and c == cols - 1:
            sums.append(sum(path))
        else:
            # move right
            dfs(r, c + 1)
            # move down
            dfs(r + 1, c)

        # backtrack
        path.pop()

    dfs(0, 0)   # always start top-left

    return min(sums)


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))










import numpy as np
def minPathSum(grid: list[list[int]]) -> int:

    cols = len(grid[0])
    rows = len(grid)
    path = []

    grid = np.array(grid)

    def dfs(r, c):

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        path.append(grid[r][c])

        print(grid[r,:],grid[:,c])
        if np.sum(grid[r:]) < np.sum(grid[:,c]):
            dfs(r, c + 1)
        else:
            dfs(r + 1, c)

    dfs(0, 0)   # always start top-left

    return path

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))










