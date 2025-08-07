

"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

"""



def numIslands(grid):

    rows, cols = len(grid), len(grid[0])
    visited = set()
    q = 0
    list1 = []

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return 0

        visited.add((r, c))

        count = 1

        # Explore in all 4 directions
        count = count + dfs(r+1, c)  # down
        count = count + dfs(r-1, c)  # up
        count = count + dfs(r, c+1)  # right
        count = count + dfs(r, c-1)  # left

        return count

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                size = dfs(r, c)
                list1.append(size)

                if size > q:
                    q = size
                size = 0

    return list1, q



print(numIslands(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))


