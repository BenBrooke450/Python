
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
        if r < 0 or r >= rows or c < 0 or c >= cols:
            print(f"Returning: {r,c} out of bounds")
            return

        path.append(grid[r][c])
        print(f"In bounds: {r,c}")

        if r == rows - 1 and c == cols - 1:
            print(f"Reached the end {r,c}")
            sums.append(sum(path))

        else:

            dfs(r, c + 1)

            dfs(r + 1, c)

        print(f"Removing: {r,c}")
        path.pop()

    dfs(0, 0)

    return min(sums)


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

"""
In bounds: (0, 0)
In bounds: (0, 1)
In bounds: (0, 2)
Returning: (0, 3) out of bounds
In bounds: (1, 2)
Returning: (1, 3) out of bounds
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Removing: (1, 2)
Removing: (0, 2)
In bounds: (1, 1)
In bounds: (1, 2)
Returning: (1, 3) out of bounds
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Removing: (1, 2)
In bounds: (2, 1)
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Returning: (3, 1) out of bounds
Removing: (2, 1)
Removing: (1, 1)
Removing: (0, 1)
In bounds: (1, 0)
In bounds: (1, 1)
In bounds: (1, 2)
Returning: (1, 3) out of bounds
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Removing: (1, 2)
In bounds: (2, 1)
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Returning: (3, 1) out of bounds
Removing: (2, 1)
Removing: (1, 1)
In bounds: (2, 0)
In bounds: (2, 1)
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Returning: (3, 1) out of bounds
Removing: (2, 1)
Returning: (3, 0) out of bounds
Removing: (2, 0)
Removing: (1, 0)
Removing: (0, 0)
7"""




















