

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


def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:

    list1 = []
    empty_list = [0]

    def recur(graph,t,empty_list):

        x = graph[t]

        for y in range(len(x)):
            print("place in sublist: ",x[y])
            print("sublist: ",x)
            print(empty_list)
            print(graph[x[y]])

            if len(graph[x[y]]) == 0:
                empty_list.append(x[y])
                print("len(x): ", empty_list)
                list1.append(empty_list)
                empty_list = [0]
                recur(graph, t, empty_list)

            empty_list.append(x[y])
            recur(graph,x[y],empty_list)

        return list1

    return recur(graph,0,empty_list)


print(allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))





















