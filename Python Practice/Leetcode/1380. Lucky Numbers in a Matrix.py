
"""
Given an m x n matrix of distinct numbers,
    return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such
    that it is the minimum element in its
    row and maximum in its column.



Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since
    it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number
    since it is the minimum in its
     row and the maximum in its column.


Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky
    number since it is the minimum
    in its row and the maximum in its column.

"""
import numpy as np


def luckyNumbers(matrix: list[list[int]]):

    matrix_np = np.array(matrix)
    list1 = []
    n = 0
    for row in matrix:
        min_row = min(row)
        n = row.index(min_row)
        if  all(min_row >= x for x in matrix_np[:,n]):
            list1.append(min_row)

    return list1


print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
#[12]

print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
#[15]








