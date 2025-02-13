
"""
You are given an 8 x 8 matrix representing a chessboard. There is
    exactly one white rook represented by 'R', some number of white
     bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

A rook can move any number of squares horizontally or vertically
    (up, down, left, right) until it reaches another piece or the
     edge of the board. A rook is attacking a pawn if it can move
      to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns.
    This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the number of pawns the white rook is attacking.



Example 1:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
    [".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 3
Explanation:
In this example, the rook is attacking all the pawns.

Example 2:
Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],
    [".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],
    [".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],
    [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 0
Explanation:
The bishops are blocking the rook from attacking any of the pawns.

Example 3:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
    [".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],
    [".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],
    [".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 3
Explanation:
The rook is attacking the pawns at positions b5, d6, and f5.

"""

import numpy as np

def numRookCaptures(board: list[list[str]]) -> int:

    board = np.array(board)
    coor = np.where(board == "R")
    x = board[coor[0]][0].tolist()
    y = [x[0] for x in board[:,coor[1]].tolist()]
    m = 0
    p = 0
    q = 0
    f = 0
    for t in x:
        if t == "p":
            m = 1
        elif t == "B":
            m = 0
        elif t == "R":
            break

    for t in x[::-1]:
        if t == "p":
            p = 1
        elif t == "B":
            p = 0
        elif t == "R":
            break

    for t in y:
        if t == "p":
            q = 1
        elif t == "B":
            q = 0
        elif t == "R":
            break

    for t in y[::-1]:
        if t == "p":
            f = 1
        elif t == "B":
            f = 0
        elif t == "R":
            break

    return p+q+f+m

print(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
    [".",".",".","p",".",".",".","."],["p","p",".",".","R","p","B","."],
    [".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],
    [".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))




