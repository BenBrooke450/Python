
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

import numpy as np
def minPathSum(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    grid = np.array(grid)

    # Start from the top-left corner and update each cell with min path sum
    for r in range(rows):
        for c in range(cols):
            print(grid)
            if r == 0 and c == 0:
                continue  # start cell, nothing to do
            elif r == 0:
                grid[r,c] += grid[r,c - 1]  # first row, can only come from left
            elif c == 0:
                grid[r,c] += grid[r - 1,c]  # first column, can only come from top
            else:
                grid[r,c] += min(grid[r - 1,c], grid[r,c - 1])  # min from top or left

    return grid[-1,-1]


# Example
print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # Output: 7
"""
[1 3 1]
 [1 5 1]
 [4 2 1]]
 
[[1 3 1]
 [1 5 1]
 [4 2 1]]
 
[[1 4 1]
 [1 5 1]
 [4 2 1]]
 
[[1 4 5]
 [1 5 1]
 [4 2 1]]
 
[[1 4 5]
 [2 5 1]
 [4 2 1]]
 
[[1 4 5]
 [2 7 1]
 [4 2 1]]
 
[[1 4 5]
 [2 7 6]
 [4 2 1]]
 
[[1 4 5]
 [2 7 6]
 [6 2 1]]
 
[[1 4 5]
 [2 7 6]
 [6 8 1]]
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

    dfs(0, 0,)

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




















