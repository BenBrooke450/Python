

"""
Given a directed acyclic graph (DAG) of n nodes labeled
    from 0 to n - 1, find all possible paths from node 0
     to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of
    all nodes you can visit from node i (i.e., there
     is a directed edge from node i to node graph[i][j]).



Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

"""

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        list1 = []
        empty_list = []
        def recur(graph,t,empty_list):
            x = graph[t]
            empty_list.append(t)
            if t + 1 == len(graph):
                list1.append(empty_list.copy())  # Save a copy of the current path
                return
            for y in x:
                recur(graph, y, empty_list.copy())
            return list1
        return recur(graph,0,empty_list)








def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:

    list1 = []
    empty_list = []

    def recur(graph,t,empty_list):

        x = graph[t]

        empty_list.append(t)

        if len(x) == 0:
            list1.append(empty_list.copy())  # Save a copy of the current path
            return

        for y in x:
            recur(graph, y, empty_list.copy())

        return list1

    return recur(graph,0,empty_list)


print(allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))























