

"""
You are given a map of a server center, represented as a m * n integer matrix grid,
    where 1 means that on that cell there is a server and 0 means that it is no server.
     Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.



Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.


Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.


Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate
    with each other. The two servers in the third column can communicate
     with each other. The server at right bottom corner can't communicate
      with any other server.

"""


import numpy as np
def countServers(grid: list[list[int]]) -> int:
    array_grid = np.array(grid)
    t = 0
    for n in range(array_grid.shape[0]):
        print(array_grid[n,:])
        q = list(array_grid[n,:]).count(1)
        if q > 1:
            t = t + q
            array_grid[n, :][array_grid[n, :] == 0] = -1
            array_grid[n, :][array_grid[n, :] == 1] = 2
        else:
            array_grid[n,:][array_grid[n,:] == 0] = -1
            array_grid[n, :][array_grid[n, :] == 1] = 3

    print(array_grid)

    for n in range(array_grid.shape[1]):
        print(array_grid[:, n:n+1])
        q = list(array_grid[n, :]).count(3)
        if q > 1:
            t = t + q

    return array_grid,t

#print(countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))

print(countServers(grid = [[1,0],[1,1]]))














