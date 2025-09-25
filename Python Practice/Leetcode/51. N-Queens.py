

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

"""



def solveNQueens(n: int) -> list[list[str]]:
    pass











def solveNQueens(n: int) -> list[list[str]]:

    rows = n
    cols = n

    if n == 1:
        return [["Q"]]

    grid = [["." for x in range(n)] for y in range(n)]

    visited = set()
    queen = []

    def dfs(r,c):

        if ((r,c) in visited or r < 0 or r >= rows or c < 0
                or c >= cols or grid[r+1][c+1] == "Q"
                or grid[r-1][c-1] == "Q"
                or grid[r-1][c+1] == "Q"
                or grid[r+1][c-1] == "Q"):
            return


        if "Q" not in grid[r] and "Q" not in [grid[x][c] for x in range(cols-1)]:
            grid[r][c] = "Q"

        visited.add((r,c))

        dfs(r, c + 1)
        dfs(r + 1, c)
        dfs(r ,c - 1)
        dfs(r - 1, c)

    for x in range(n):
        dfs(0,x)
        queen.append(["".join(x) for x in grid])
        queen.append(["".join(x)[::-1] for x in grid])
        visited.clear()
        grid = [["." for x in range(n)] for y in range(n)]

    return queen


print(solveNQueens(4))











