
"""
ou are given an array coordinates, coordinates[i] = [x, y], where [x, y]
 represents the coordinate of a point. Check if these points make a straight line in the XY plane.


Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true


Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

"""


def checkStraightLine(coordinates: list[list[int]]) -> bool:
    y = 0
    for x in range(len(coordinates) - 1):
        if (coordinates[x + 1][0] - coordinates[x][0]) != 0:
            g = (coordinates[x + 1][1] - coordinates[x][1]) / (coordinates[x + 1][0] - coordinates[x][0])
        else:
            g = 1000000

        if x == 0:
            y = g
        elif g != y:
            return False
    return True

print(checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]))



