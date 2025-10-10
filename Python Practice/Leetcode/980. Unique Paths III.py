
"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

"""




def uniquePathsIII(grid: list[list[int]]) -> int:

    visted = list()
    col_b = len(grid[0])
    row_b = len(grid)
    full_walk = []
    ones = sum(1 for x in grid for y in x if y == -1)

    def dfs(r,c):
        if (r,c) in visted or r < 0 or r >= row_b or c < 0 or c >= col_b or grid[r][c] == -1:
            print("out: ",(r, c))
            return

        visted.append((r,c))

        print((r,c))

        if grid[r][c] == 2 and len(visted) == col_b * row_b - ones:
            print("got it",(r,c))
            full_walk.append(visted[:])

        else:
            dfs(r,c+1)
            print((r, c))
            dfs(r+1,c)
            print((r, c))
            dfs(r,c-1)
            print((r, c))
            dfs(r-1,c)

        visted.pop()

    # r, c = next((i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 1)
    x = [[i,j] for i,x in enumerate(grid) for j,y in enumerate(x) if y ==1]
    r = x[0][0]
    c = x[0][1]
    dfs(r,c)

    print(full_walk)

    return len(full_walk)


#print(uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(uniquePathsIII([[0,1],[2,0]]))



















def uniquePathsIII(grid: list[list[int]]) -> int:

    visted = set()
    col_b = len(grid[0])
    row_b = len(grid)
    full_walk = []
    ones = sum(1 for x in grid for y in x if y == -1)

    def dfs(r,c):
        if (r,c) in visted or r < 0 or r >= row_b or c < 0 or c >= col_b or grid[r][c] == -1 or len(visted) == col_b * row_b - ones:
            print("out: ",(r, c))
            return

        visted.add((r,c))

        print((r,c))

        if grid[r][c] == 2:
            full_walk.append(visted)
            return

        dfs(r,c+1)
        print((r, c))
        dfs(r+1,c)
        print((r, c))
        dfs(r,c-1)
        print((r, c))
        dfs(r-1,c)


    dfs(0,0)

    return full_walk



