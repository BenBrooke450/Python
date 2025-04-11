

"""
A valid cut in a circle can be:

A cut that is represented by a straight line that touches
    two points on the edge of the circle and passes through its center, or

A cut that is represented by a straight line that touches
    one point on the edge of the circle and its center.

Some valid and invalid cuts are shown in the figures below.


Given the integer n, return the minimum number of cuts needed to divide a circle into n equal slices.
"""




def numberOfCuts(n: int) -> int:
    if n % 2 == 0:
        return int(n/2)
    elif n > 2 and n % 2 != 0:
        return n
    elif n == 1:
        return 0

"""1 2
2 4
3 6
4 8


> 3
4 4 (2 4)
5 5
6 6 (3 6)
7 7"""










