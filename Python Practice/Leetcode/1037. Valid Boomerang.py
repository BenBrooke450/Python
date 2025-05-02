
"""
Given an array points where points[i] = [xi, yi] represents
    a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.



Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false

"""


def isBoomerang(points: list[list[int]]) -> bool:
    list1 = []
    if any(points.count(points[p]) > 1 for p in range(len(points) - 1)):
        return False
    for p in range(len(points) - 1):
        if (points[p + 1][0] - points[p][0]) == 0:
            g = 0
        elif (points[p + 1][1] - points[p][1]) == 0:
            g = 1000000
        else:
            g = (points[p + 1][1] - points[p][1]) / (points[p + 1][0] - points[p][0])
        list1.append(g)
    if list1[0] != list1[1]:
        return True
    return False



print(isBoomerang([[0,0],[0,2],[2,1]]))

print(isBoomerang([[1,1],[2,2],[3,3]]))




