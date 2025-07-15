
# Backtracking

Backtracking is a **recursive problem-solving technique** used to build a solution incrementally and undo ("backtrack") choices that don’t lead to a valid or optimal solution.

It tries all possible paths, and if a path doesn't work, it goes back (or “backtracks”) to try the next option.



```python
def backtrack(start, path):
    print("Subset:", path)
    for i in range(start, len(nums)):
        # Choose
        path.append(nums[i])
        
        # Explore
        backtrack(i + 1, path)
        
        # Un-choose (Backtrack)
        path.pop()
```

nums = [1, 2, 3]
backtrack(0, [])

```python
"""
Subset: []
Subset: [1]
Subset: [1, 2]
Subset: [1, 2, 3]
Subset: [1, 3]
Subset: [2]
Subset: [2, 3]
Subset: [3]
"""
```

## 1. Initial Call:

```python
nums = [1, 2, 3]

backtrack(0, [])
```

start = 0

path = []

This is the empty subset → printed first: 

Subset: []

<br>


## 2. First Loop (i = 0)

```python 
path.append(nums[0])  # path becomes [1]

backtrack(1, [1])
```

Now inside this call:

Subset: [1] is printed

Next loop: i = 1

<br>

## 3. Next Level Down (i = 1)

```python 
path.append(nums[1])  # path becomes [1, 2]

backtrack(2, [1, 2])
```

Subset: [1, 2] is printed

Next: i = 2

<br>

## 4. One More Level (i = 2)

```python 
path.append(nums[2])  # path becomes [1, 2, 3]

backtrack(3, [1, 2, 3])
```

Subset: [1, 2, 3] is printed

#Now i = 3 is out of bounds → returns

Backtrack: .pop() → path becomes [1, 2]

<br>

## 5. Backtracking Continues

Back at [1, 2], loop is over → backtrack: .pop() → path becomes [1]

Next loop: i = 2

```python 
path.append(nums[2])  # [1, 3]

backtrack(3, [1, 3])
```
→ Subset: [1, 3]

<br>

## 6. More Backtracking
Backtrack to [1], then to []

Now i = 1, start fresh:

```python
path.append(nums[1])  # [2]

backtrack(2, [2]) 
```
→ Subset: [2], then explores [2, 3], then backtracks.


## Key Line:

```python
for i in range(start, len(nums)):
```

This for loop controls when recursion happens. If start >= len(nums), then:

 - **range(start, len(nums)) becomes an empty range**

 - **So the loop does not execute**

 - **Therefore, nothing inside the loop runs — and the function returns automatically (backtracks)**

Loop never runs (range(3, 3)), so the function exits

That’s the return

Then .pop() is called to remove 3 → backtrack!






<br><br><br><br><br><br>

# Example 1




```ptyhon
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # reuse allowed
            path.pop()

    backtrack(0, [], 0)
    return res


print(combinationSum(candidates = [2,3,6,7], target = 7))
```








```ptyhon
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    list1 = []
    seen = set()
    def backtrack(start, path):
        for i in range(start, len(candidates)):
            print(path)
            path.append(candidates[i])
            if sum(path) < target:
                backtrack(i, path)
            elif sum(path) == target:
                if tuple(path) not in seen:
                    seen.add(tuple(path))
                    list1.append(path[:])
                    pass
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return list1


print(combinationSum(candidates = [2,3,6,7], target = 7))
```






# Example 2

```python
"""

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]




Example 2:


Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30

"""


def generate(numRows: int) -> list[list[int]]:

    list1 = []

    def pas(first,incre,numRows):

        list1.append(first[:])
        first.append(incre)
        first = [1] + [sum(first[x:x+2]) for x in range(len(first)-1)]
        if len(list1) >= numRows:
            return list1
        else:
            pas(first,incre,numRows)

    pas(first = [1],incre = 0,numRows = numRows)

    return list1


print(generate(5))
#[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

```









# Example 3

```python

def generateParenthesis(n: int) -> list[str]:
    result = []

    def backtrack(current, open_count, close_count):
        # Base case: valid combination
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add an open parenthesis if we still can
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        # Add a close parenthesis if it won’t break validity
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    # Start the recursion
    backtrack("", 0, 0)
    return result

print(generateParenthesis(2))
```





# Example 4

```python
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

```

## Graph Representation
This is an adjacency list — each index represents a node, and the list at each index tells you which nodes it points to.


```python
graph = [[1, 2], [3], [3], []]
```

| Node | Points To  |
| ---- | ---------- |
| 0    | 1, 2       |
| 1    | 3          |
| 2    | 3          |
| 3    | \[] (leaf) |



## Let's Walk Through It Line-by-Line


### First Call: recur(graph, 0, [])
 - t = 0

 - x = [1, 2] → Node 0 has neighbors 1 and 2

 - path_so_far = [0]

 - We loop through [1, 2] and call recur() for each.


<br>

### <> First Branch: recur(graph, 1, [0])

 - t = 1

 - x = [3] → Node 1 points to 3

 - path_so_far = [0, 1]

 - Loop through [3]:

 

<br>

#### Next: recur(graph, 3, [0, 1])

 - t = 3

 - x = [] → Node 3 is a leaf

 - path_so_far = [0, 1, 3]

 - We append path_so_far.copy() → list1 = [[0, 1, 3]]

We return.

<br>

### <>Second Branch: recur(graph, 2, [0])

 - t = 2

 - x = [3] → Node 2 points to 3

 - path_so_far = [0, 2]

#### Next: recur(graph, 3, [0, 2])

 - t = 3

 - x = [] → Leaf node

 - path_so_far = [0, 2, 3]

 - We append path_so_far.copy() → list1 = [[0, 1, 3], [0, 2, 3]]


## Final Output

[[0, 1, 3], [0, 2, 3]]

