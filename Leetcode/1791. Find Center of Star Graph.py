"""
There is an undirected star graph consisting of n nodes
 labeled from 1 to n. A star graph is a graph where there
  is one center node and exactly n - 1 edges that connect
   the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi]
 indicates that there is an edge between the nodes ui and vi.
  Return the center of the given star graph.

Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

"""

def star(list1:list[int]):

    dic1 = {}
    for x in list1:
        for y in x:
            if y not in dic1.keys():
                dic1[y] = 1
            else:
                dic1[y] = dic1.get(y) + 1
    return max(dic1, key=dic1.get)



print(star([[1,2],[5,1],[1,3],[1,4]]))
#1


print(star([[1,2],[2,3],[4,2]]))
#2
