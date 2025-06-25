

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

import numpy as np
def maxArea(height: list[int]) -> int:
    height = np.array(height)
    big_list = np.array([[(min(height[x],height[y]))*(y - x)] for x in np.arange(len(height)) for y in np.arange(len(height)-1,0,-1)])

    return int(max(big_list))


print(maxArea([1,8,6,2,5,4,8,3,7]))







def maxArea(height: list[int]) -> int:

    m = 0
    i = 0
    j = len(height) - 1
    rev_height = height[::-1]

    while i < j:
        min_h = min(height[i],height[j])
        dis_between = j - i
        if min_h*dis_between > m:
            m = min_h*dis_between
            pass

        if height[i] < height[j]:
            i += 1  # try a taller left wall
        else:
            j -= 1  # try a taller right wall

    return m







