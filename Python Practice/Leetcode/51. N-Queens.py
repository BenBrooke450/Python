

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

    grid = [["." for x in range(n)] for y in range(n)]
    lines = []
    all_q = []

    def dfs(r,c):
        t = 0

        print(grid,[grid[x][c] for x in range(n)])

        for y in range(n):

            print("Y: ",y,"   R:  ",r)

            i, j = r - 1, y - 1
            while i >= 0 and j >= 0:
                if grid[i][j] == "Q":
                    t = 1
                    print("BRAKED FIRST")
                    break
                i -= 1
                j -= 1


            if t == 1 or "Q" in [grid[x][y] for x in range(n)]:
                t = 0
                continue

            i, j = r - 1, y + 1
            while i >= 0 and j < n:
                if grid[i][j] == "Q":
                    t = 1
                    print("BRAKED SECOND")
                    break
                i -= 1
                j += 1


            if t == 1:
                t = 0
                continue

            grid[r][y] = "Q"

            lines.append(grid[r])

            dfs(r + 1, c)

            p = [x.count("Q") for x in lines]

            print("P:  ", p)

            if all(y != 1 for y in p) or len(p) != n:
                lines = []

            else:
                all_q.append(lines)
                lines = []

    c = 0
    r = 0
    for x in range(n):
        print("STARTING ROW:  ",x)
        grid[0][x] = "Q"
        dfs(r+1,c)

        grid = [["." for x in range(n)] for y in range(n)]

    return all_q


print(solveNQueens(4))










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







