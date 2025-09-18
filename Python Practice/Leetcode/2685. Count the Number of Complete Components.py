
"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.



Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.


Example 2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices.
    On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5.
    Thus, the number of complete components in this graph is 1.

"""
from gc import unfreeze


def countCompleteComponents(n: int, edges: list[list[int]]) -> int:

    """
    A connected component is complete if and only if the number of edges in the component is equal to m*(m-1)/2, where m is the number of nodes in the component.
    """

    nodes = set()
    triangles = set()

    def dfs(y):
        for q in edges:
            if y in q and tuple(q) not in nodes:
                nodes.add(tuple(q))
                for t in q:
                    dfs(t)

    j = 0
    for x in edges:
        nodes.add(tuple(x))  # convert to tuple here
        for y in x:
            dfs(y)
            j = j + 1
            if j == 2:
                triangles.add(frozenset(nodes))  # frozenset to make it hashable
                nodes = set()
                j = 0

    return n -  len(set(q for x in triangles for y in x for q in y)),[len(set(x)) for x in triangles],[set(x) for x in triangles]


print(countCompleteComponents(6,[[0,1],[0,2],[1,2],[3,4]]))

print(countCompleteComponents(6,[[0,1],[0,2],[1,2],[3,4],[3,5]]))

print(countCompleteComponents(4,[[2,1],[3,0],[3,1],[3,2]]))







        






















#m*(m-1)/2

def countCompleteComponents(n: int, edges: list[list[int]]) -> int:

    edges = sorted(edges)
    edges = [y for x in edges for y in x]

    dict1 = dict()

    for x in range(0,len(edges),2):

        tuple_values = [y for x in dict1.values() for y in x]

        if edges[x] not in tuple_values and edges[x+1] not in tuple_values:
            dict1[x] = [edges[x],edges[x+1]]
        else:
            for key, values in dict1.items():

                if edges[x] in (x for x in values) or edges[x+1] in (x for x in values):
                    dict1[key].extend([edges[x],edges[x+1]])
    m = 0

    print(dict1)

    for key, values in dict1.items():
        l = len(set(values))
        k = len(values)/2

        if k == l*(l-1)/2:
            m = m + 1

    return m + n - len(set(edges))





