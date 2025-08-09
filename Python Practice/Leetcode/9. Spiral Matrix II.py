
"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

"""

import numpy as np

def generateMatrix(n: int) -> list[list[int]]:
    matrix = np.zeros((n, n), dtype=int)

    r = 0
    c = 0
    s = 0
    rotate = 1
    rotation = 0
    steps = n  # how many steps before turning

    for i, m in enumerate(range(1, n * n + 1)):
        matrix[r, c] = m
        print(matrix)
        s += 1

        if s == steps:  # Time to rotate
            matrix = np.rot90(matrix)
            s = 0
            rotation += 1

            # Find first zero in rotated matrix and start there
            r, c = np.argwhere(matrix == 0)[0]

            # After every two rotations, shrink step count
            if rotation % 2 == 0:
                steps -= 1
        else:
            c += 1

    print(matrix)

    return np.rot90(matrix, k=1).tolist()















import numpy as np

def generateMatrix(n: int) -> list[list[int]]:


    matrix = np.zeros((n,n),dtype=int)

    t = 0
    r = 0
    c = 0
    s = 0
    rotate = 1
    rotation = 0

    for i,m in enumerate(range(1,n*n+1)):

        if s < n:
            matrix[r,c] = m

        elif s == n:
            matrix = np.rot90(matrix)

            zeros = np.argwhere(matrix == 0)
            print(zeros)

            if zeros.size > 0:
                c = zeros[0]

            s = 0

            if i == n:
                n = n - 1
                rotation = 0

            elif rotation == n*2:
                rotation = 0
                n = n - 1

            if rotate % 4 == 0:
                r = r + 1

            matrix[r, c] = m

            rotate = rotate + 1
            print(matrix)


        rotation = rotation + 1
        s = s + 1
        c = c + 1

        print(matrix, m, rotation)

    return np.rot90(matrix,k=1).tolist()



print(generateMatrix(4))









