

"""
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.



Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.

"""

import numpy as np
def maxEqualRowsAfterFlips(matrix: list[list[int]]) -> int:
    matrix = np.array(matrix)

    print(matrix[:,:1])
    print(matrix.shape[0])
    t = 0

    for y in range(matrix.shape[1]):
        print(matrix[:, y:y+1])

        for x in range(matrix.shape[0]):
            print("shape:",matrix[x:x+1,:][0])
            s = sum(matrix[x:x+1,:][0])
            if s == 1 or s == 3:
                t = t + 1

    return t

#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]]))

#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]]))

print(maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]]))













