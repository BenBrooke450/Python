

"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

"""

import numpy as np

def maxAreaOfIsland(grid: list[list[int]]) -> int:

    row = 0
    for i,x in enumerate(grid):
        for j,y in enumerate(x):
            if y == 1:
                grid[i][j] = [j,row]
        row = row + 1

    row = 0
    column = 0
    max_island = []

    def where(grid: list[list[int]] ,column: int(), row: int(),max_island: list()):

        row_i = grid[row]

        for i,unit in enumerate(row_i):
                if unit == 1:
                    column_i = column[i]


    where(grid,column,row,max_island)

    return grid







def numIslands(grid):

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return

        visited.add((r, c))

        # Explore in all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:

                dfs(r, c)
                count += 1

    return count



print(numIslands(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))


