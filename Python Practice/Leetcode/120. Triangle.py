
"""



Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
"""


def minimumTotal(triangle: list[list[int]]) -> int:
    # Start from second last row and go upward
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            print(row,col)
            # Update each element with min path sum from row below
            print(triangle)
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

    # The top element now contains the minimum path sum
    return triangle[0][0]



print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
"""
2 0
[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
2 1
[[2], [3, 4], [7, 5, 7], [4, 1, 8, 3]]
2 2
[[2], [3, 4], [7, 6, 7], [4, 1, 8, 3]]
1 0
[[2], [3, 4], [7, 6, 10], [4, 1, 8, 3]]
1 1
[[2], [9, 4], [7, 6, 10], [4, 1, 8, 3]]
0 0
[[2], [9, 10], [7, 6, 10], [4, 1, 8, 3]]
11
"""











def minimumTotal(triangle: list[list[int]]) -> int:


    def move(n,list1,i,j):
        print("FIRST:",list1[i])
        print("SECOND:",list1[i][0])
        i = i + 1
        if i >= len(list1):
            if len(list1[-1]) == 1:
                return
            else:
                print("NEW-------")
                j = j + 1
                if j >= len(list1):
                    j = 0
                    pass
                print(i,j)
                list1[i-j] = list1[i-j][1:]
                i = 0
                move(n, list1, i, j)
        else:
            move(n,list1,i,j)

    move(n = 0, list1 = triangle, i = 0,j = 0)

    return triangle

