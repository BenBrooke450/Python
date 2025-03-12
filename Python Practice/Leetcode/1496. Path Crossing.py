
"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each
    representing moving one unit north, south, east, or west,
    respectively. You start at the origin (0, 0) on a 2D plane
    and walk on the path specified by path.

Return true if the path crosses itself at any point, that is,
    if at any time you are on a location you have previously visited. Return false otherwise.



Example 1:
Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.


Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
"""

import copy

def isPathCrossing(path: str) -> bool:
    list1 = [[0,0]]
    for n in path:

        last_p = copy.deepcopy(list1)
        last_p = last_p[0]

        if n == "N":
            last_p[0] = last_p[0] + 1
            print(list1,last_p)
            if last_p in list1:
                return True
            else:
                list1.insert(0,last_p,)
        elif n == "E":
            last_p[1] = last_p[1] + 1
            if last_p in list1:
                return True
            else:
                list1.insert(0,last_p,)

        elif n == "S":
            last_p[0] = last_p[0] - 1
            if last_p in list1:
                return True
            else:
                list1.insert(0,last_p,)

        elif n == "W":
            last_p[1] = last_p[1] - 1
            if last_p in list1:
                return True
            else:
                list1.insert(0,last_p,)
    return False



print(isPathCrossing("NES"))







