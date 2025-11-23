


"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).



Example 1:
Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16


abc
"""


def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

    a_x_length = list(range(ax1, ax2 + 1))
    b_x_length = list(range(bx1, bx2 + 1))

    x = 0

    for a_x in a_x_length:
        if a_x in b_x_length:
            x = x + 1

    if x>= 1:
        x = x - 1

    y = 0

    a_y_length = list(range(ay1, ay2 + 1))
    b_y_length = list(range(by1, by2 + 1))

    for a_y in a_y_length:
        if a_y in b_y_length:
            y = y + 1

    if y>= 1:
        y = y - 1

    total_a = (len(a_x_length) - 1) * (len(a_y_length) - 1)
    total_b = (len(b_x_length) - 1) * (len(b_y_length) - 1)

    total = total_a+total_b


    return a_x_length,b_x_length, x, y, x*y, total_a, total_b, total, total - x*y, a_y_length,b_y_length

#print(computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = 3, by1 = 3, bx2 = 4, by2 = 4))
print(computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))








