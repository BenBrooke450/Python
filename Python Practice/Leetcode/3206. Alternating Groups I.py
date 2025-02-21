
"""
There is a circle of red and blue tiles. You are given an array
    of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors
    (the middle tile has a different color from its left and right tiles)
     is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle,
    the first and the last tiles are considered to be next to each other.



Example 1:
Input: colors = [1,1,1]
Output: 0
Explanation:



Example 2:
Input: colors = [0,1,0,0,1]
Output: 3
Explanation:



Alternating groups:

"""


def numberOfAlternatingGroups(colors: list[int]) -> int:
    m = 0
    i = 0
    t = colors
    colors = colors + colors
    while len(t) != i:
        if (colors[i:i + 3].count(1) == 2 and colors[i:i + 3].count(0) == 1 and colors[i + 1] == 0) or (
                colors[i:i + 3].count(0) == 2 and colors[i:i + 3].count(1) == 1 and colors[i + 1] == 1):
            m = m + 1
            i = i + 1
        else:
            i = i + 1
    return m

print(numberOfAlternatingGroups([0,1,0,0,1]))



