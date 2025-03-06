
"""
You are given an m x n 2D array grid of positive integers.

Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.

Zigzag pattern traversal is defined as following the below actions:

Start at the top-left cell (0, 0).
Move right within a row until the end of the row is reached.
Drop down to the next row, then traverse left until the beginning of the row is reached.
Continue alternating between right and left traversal until every row has been traversed.
Note that you must skip every alternate cell during the traversal.

Return an array of integers result containing, in order, the value of the cells visited during the zigzag traversal with skips.



Example 1:

Input: grid = [[1,2],[3,4]]

Output: [1,4]

Explanation:



Example 2:

Input: grid = [[2,1],[2,1],[2,1]]

Output: [2,1,2]

Explanation:



Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,3,5,7,9]

Explanation:
"""


def zigzagTraversal(grid: list[list[int]]) -> list[int]:
    level = 0
    list1 = []
    print(grid[0])
    while level != len(grid):
        if level % 2 == 0:
            even_grid = grid[level]
            for i, m in enumerate(even_grid):
                if i % 2 == 0:
                    list1.append(m)
            level = level + 1

        else:
            odd_grid = grid[level]
            reverse_grid = odd_grid[::-1]
            for i, m in enumerate(reverse_grid):
                if i % 2 != 0 and len(reverse_grid) % 2 != 0:
                    list1.append(m)
                elif i % 2 == 0 and len(reverse_grid) % 2 == 0:
                    list1.append(m)
            level = level + 1
    return list1


print(zigzagTraversal([[1,2,3],[4,5,6],[7,8,9]]))










