

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
    list1 = []
    t = 0
    p = 0
    for i in range(matrix.shape[0]):
        row = matrix[i, :]
        list1.append([])  # Initialize a new list for each row
        current_segment = [row[0]]

        for j in range(1, len(row)):
            if row[j] == current_segment[0]:
                current_segment.append(row[j])
            else:
                list1[i].append(len(current_segment))
                current_segment = [row[j]]

        if current_segment:
            list1[i].append(len(current_segment))


    return max([list1.count(x) for x in list1])


#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]]))

#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]]))

print(maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]]))


#######################


import numpy as np

def maxEqualRowsAfterFlips(matrix: list[list[int]]) -> int:
    matrix = np.array(matrix)
    list1 = []
    t = 0
    p = 0
    for i in range(matrix.shape[0]):
        row = matrix[i, :]
        print(row)
        list1.append([])  # Initialize a new list for each row

        current_segment = [row[0]]

        for j in range(1, len(row)):
            if row[j] == current_segment[0]:
                current_segment.append(row[j])
            else:
                list1[i].append(current_segment)
                current_segment = [row[j]]

        if current_segment:
            list1[i].append(current_segment)

    return list1


#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]]))

#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]]))

#print(maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]]))



#######################################################

import numpy as np
def maxEqualRowsAfterFlips(matrix: list[list[int]]) -> int:
    matrix = np.array(matrix)
    list1 = [[] for x in range(matrix.shape[0])]
    t = 0
    p = 0
    for i,x in enumerate(range(matrix.shape[0])):
        print("shape:",matrix[x:x+1,:][0])
        list2=[]
        m = 0
        n = 0
        for j,y in enumerate(matrix[x:x+1,:][0]):
            if y == 0:
                if n == 0:
                    list2.append(0)
                    if j + 1 == len(matrix[x:x+1,:][0]):
                        list1[i].append(list2)
                else:
                    list1[i].append(list2)
                    list2 = []
                    n = 0
                    list2.append(0)
                    if j + 1 == len(matrix[x:x+1,:][0]):
                        list1[i].append(list2)
                m = m + 1
            else:
                if m == 0:
                    list2.append(1)
                    if j + 1 == len(matrix[x:x+1,:][0]):
                        list1[i].append(list2)
                else:
                    list1[i].append(list2)
                    list2 = []
                    m = 0
                    list2.append(1)
                    if j + 1 == len(matrix[x:x+1,:][0]):
                        list1[i].append(list2)
                n = n + 1
    return list1


#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]]))

#print(maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]]))

#print(maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]]))













