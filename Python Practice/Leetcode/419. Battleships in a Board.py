

"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).



Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0

"""


def countBattleships(board: list[list[str]]) -> int:

    col = len(board[0])
    row = len(board)

    visited = set()
    battbleship = 0


    def dfs(r,c):
        if  (r,c) in visited or r < 0 or r + 1 > row or c < 0 or c + 1 > col or board[r][c] == ".":
            return

        print(r,c)
        visited.add((r,c))

        dfs(r ,c + 1)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r - 1, c)

    for x in range(row):
        for y in range(col):
            if board[x][y] == "X" and (x,y) not in visited:
                print(x,y)
                dfs(x,y)
                print("return")
                battbleship += 1

    return battbleship


print(countBattleships(board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))