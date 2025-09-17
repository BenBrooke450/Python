

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


"""
import numpy
import numpy as np


def isValidSudoku(board: list[list[str]]) -> bool:

    visited = set()
    numbers = []
    all = []


    def dfs(r, c):
        if ((r < row-3 or r >= row) or (c < cube-3 or c >= cube) or (r, c) in visited):
            return

        visited.add((r, c))

        if board[r][c] != ".":
            numbers.append(board[r][c])

        # Explore in all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    cube = 3
    row = 3

    for r in range(9):
        for c in range(9):
            if (r, c) not in visited:
                dfs(r, c)
                cube = cube + 3
                if cube > 9:
                    row = row + 3
                    cube = 3
                all.append(numbers)

                row_vals = [x for x in board[r] if x != "."]
                col_vals = [board[x][c] for x in range(9) if board[x][c] != "."]

                if len(row_vals) != len(set(row_vals)) or len(col_vals) != len(set(col_vals)):
                    return False

                numbers = []

    return True



"""print(isValidSudoku(board=[["5","3",".",".","7",".",".",".","."]
                            ,["6",".",".","1","9","5",".",".","."]
                            ,[".","9","8",".",".",".",".","6","."]
                            ,["8",".",".",".","6",".",".",".","3"]
                            ,["4",".",".","8",".","3",".",".","1"]
                            ,["7",".",".",".","2",".",".",".","6"]
                            ,[".","6",".",".",".",".","2","8","."]
                            ,[".",".",".","4","1","9",".",".","5"]
                            ,[".",".",".",".","8",".",".","7","9"]]))


print(isValidSudoku(board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))"""






print(isValidSudoku(board =[[".",".","4",".",".",".","6","3","."],
                            [".",".",".",".",".",".",".",".","."],
                            ["5",".",".",".",".",".",".","9","."],
                            [".",".",".","5","6",".",".",".","."],
                            ["4",".","3",".",".",".",".",".","1"],
                            [".",".",".","7",".",".",".",".","."],
                            [".",".",".","5",".",".",".",".","."],
                            [".",".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".",".","."]]))



