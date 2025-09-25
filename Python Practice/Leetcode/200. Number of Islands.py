

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


"""



def numIslands(grid: list[list[str]]) -> int:

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = []

    def dfs(r, c):

        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        visited.add((r,c))

        dfs(r,c+1)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r-1,c)

    for x in range(rows):
        for y in range(cols):
            if (x,y) not in visited and grid[x][y] == "1":

                dfs(x,y)

                islands.append(1)

    return islands


print(numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))









