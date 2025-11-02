

<br><br><br><br><br>

**Summary:**
Depth First Search (DFS) is a graph traversal algorithm that explores as far as possible along each path before backtracking. It uses recursion or a stack, marking nodes as visited to avoid revisiting them. DFS is efficient (O(V + E)) and commonly used for path finding, cycle detection, and exploring connected components in graphs or trees.
"

<br><br><br><br>

# Example 1

```python

def numIslands(grid):

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return

        visited.add((r, c))

        # Explore in all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:

                dfs(r, c)
                count += 1

    return count



print(numIslands(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))

```

<br>


<br>

### Step 1.0

Here we set up the dimensions of the matrix for use to loop through.

```python
rows, cols = len(grid), len(grid[0])

visited = set()
```




<br>


### Step 2.0

We move past this part for now as we haven't called the function.

```python
def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return

        visited.add((r, c))

        # Explore in all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
```


<br>


### Step 3.0

We begin to loop through the rows and columns of the matrix, when the first 1 appears we then enter the dfs(r, c) which begins the recursion

```python

count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:

                dfs(r, c)
                count += 1
```

<br>

### Step 3.1

We now enter the function.

```python

if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
    return
```

This top statement tells us if any of these conditions are met we **return** to the function below, BUT as we have just entered this statement it will never happen the first time.

```python
if grid[r][c] == 1 and (r, c) not in visited:
    dfs(r, c)
    count += 1
```


<br>

### Step 3.2

Now we check each space above and below, left and right as we are go further into the recursion.

Let's say that **dfs(r+1, c)** has found a 1, so then you renter the function.

```python

visited.add((r, c))

# Explore in all 4 directions
dfs(r+1, c)
dfs(r-1, c)
dfs(r, c+1)
dfs(r, c-1)
```

We then move back to this statement. This again checks if we have met any of the conditions. If we do meet one of these conditions we return back to the previous space/area. 
 - BUT you have to remember if we then find a 0 below that 1, we return to the one and then move into the next **dfs(r-1, c)** and we work our way down the list of dfs

```python

if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
    return
```

<br>

### Step 3.3

Let's say we hit a 0 at (1,3) and we were on (1,2) we then **return** to (1,2), we move through the matrix.

dfs(r+1, c) we can´t go any further as there's a 0 at (1,3).

We move back a space to (1,2) BUT we move onto the next dfs which would be dfs(r-1, c).

dfs(r-1, c) we try to go back to (1,1) BUT **(r, c) in visited** so we move to the next one.

dfs(r, c+1)....

**IT CAN ONLY RETRACE ITS STEPS BY THE RETURN FUNCTION NOT BY THE FUNCTIONS BELOW, THE RETURN FUNCTION WILL PULL IT BACK TO WITHIN ITS SELF AND CAN ONLY BE DONE WHEN THERE´S NO WHERE ELSE LEFT TO GO**

```python
# Explore in all 4 directions
dfs(r+1, c)
dfs(r-1, c)
dfs(r, c+1)
dfs(r, c-1)
```

**Left, right, up and down, searching every part AND THEN IT PULLS/RETURNS IT-SELF TO THE BEGINNING AFTER IT CAN´T FIND ANYWHERE ELSE TO GO**

<br>

### Step 4

After every part of the island has been searched, it returns to dfs(r, c) the original function and counts +1 counting an island.

```python
if grid[r][c] == 1 and (r, c) not in visited:
    dfs(r, c)
    count += 1
```

And then after the count +1 the loop moves to the next **cols**, counting all the islands

```python

count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:

                dfs(r, c)
                count += 1
```

















<br><br><br><br>

## Example 2

## Broken Example

```python
def letterCombinations(digits: str) -> list[str]:

    tele = {"2":['a', 'b', 'c'], "3":['d', 'e', 'f'], "4":['g', 'h', 'i'], "5":['j', 'k', 'l'], "6":['m', 'n', 'o'], "7":['p', 'q', 'r','s'], "8": ['t', 'u', 'v'], "9": ['w','x','y','z']}

    list1 = []

    for x in digits:
        list1.append(tele[x])

    list2 = []
    start = list1[0]
    i = 0

    def loop(numbers : list[list[str]],list2,start:list[str],i):

        for z,x in enumerate(start):
            for j,y in enumerate(list1[1 + i]):

                if i == 0 :
                    list2.append([x,y])
                else:
                    list3 = []
                    list3.extend(x)
                    list3.extend(y)
                    list2.append(list3)

        if i + 2 < len(list1):
            start = list2
            list2 = []
            start = loop(list1,list2,start, i+1)
            return start

        return start

    loop(list1,list2,start,i)

    return start




print(letterCombinations("23"))
#['a', 'b', 'c']
```

Perfect — let’s trace with a small example so you can **see exactly where the results vanish**.

Suppose you call your function with:

```python
digits = "23"
```

so:

```python
list1 = [['a','b','c'], ['d','e','f']]
```

---

### Step 1 — first call (`i = 0`)

* `start = ['a','b','c']`
* Inside the nested loops, you pair each from `start` with each from `list1[1]` → `[['a','d'], ['a','e'], ... , ['c','f']]`
* Now:

  ```python
  start = list2   # (list2 has those 9 pairs)
  list2 = []      # <-- here you wipe it out
  ```

At this point `start` holds your **9 pairs**, but `list2` is empty.

---

### Step 2 — recursive call (`i = 1`)

* You call `loop(list1, list2, start, 1)`
  BUT notice: `list2` is `[]` (you just reset it before).
* Inside this call, the loops try to use `list1[2]` … but `len(list1) = 2`, so `i+1 = 2` is out of range.
* Therefore, the inner loops do **nothing**.
* Then the condition `if i + 2 < len(list1)` → `if 3 < 2` is false.
* So you fall to `return start`.

Here, `start` still has the **9 pairs**, so this deepest call returns them. 

---

### Step 3 — back at the first call

* The recursive call returned the 9 pairs…
* BUT you never captured them:

  ```python
  loop(list1, list2, start, i+1)   # result ignored
  return start                     # returns the *old* start
  ```

So the top-level call just hands back its own `start` (whatever it was before recursion), not what recursion computed.

---

### Key insight

* Your deepest call *does* return the right result.
* The parent call ignores it because you don’t do:

  ```python
  start = loop(list1, list2, start, i+1)
  ```
* Instead, you just throw it away and return your local `start`.

---

That’s why you never see the “final” results bubble all the way back out.




<br>

# Fixed Example 2

```python
def letterCombinations(digits: str) -> list[str]:

    tele = {"2":['a', 'b', 'c'], "3":['d', 'e', 'f'], "4":['g', 'h', 'i'], "5":['j', 'k', 'l'], "6":['m', 'n', 'o'], "7":['p', 'q', 'r','s'], "8": ['t', 'u', 'v'], "9": ['w','x','y','z']}

    list1 = []

    for x in digits:
        list1.append(tele[x])

    print(list1)

    list2 = []
    start = list1[0]
    i = 0

    def loop(numbers : list[list[str]],list2,start:list[str],i):

        for z,x in enumerate(start):
            for j,y in enumerate(list1[1 + i]):

                if i == 0 :
                    list2.append([x,y])
                else:
                    list3 = []
                    list3.extend(x)
                    list3.extend(y)
                    list2.append(list3)

        if i + 2 < len(list1):
            start = list2
            list2 = []
            last = loop(list1,list2,start, i+1)
            return last

        return list2

    return loop(list1,list2,start,i)


print(letterCombinations("23"))
```















<br><br><br><br><br><br><br><br>

# Example 3



```python
def combine(n: int, k: int) -> list[list[int]]:

    ran = []
    new = list(range(1,n+1))
    start = 0
    end = 1

    def com(ran: list[int],new,start, end ,k):

        if start >= n or end > n:
            return

        part = [new[start]]
        print(end,k+end-1,new)
        part.extend(new[end:k+end-1])
        print("Part :",part)

        if len(part) == k:
            ran.append(part)
            print(ran)

        print(ran)

        if end + 1 < n:
            part = []
            end = end + 1
            com(ran, new, start, end, k)

        start = start + 1
        end = start + 1
        part = []

        if start < n:
            com(ran, new, start, end, k)

        return ran

    return com(ran,new,start,end, k)
```

-----

### Step-by-Step Analysis of the Errors

Let's trace the execution with an example, like `combine(4, 2)`.

1.  **Initial Call:** `com([], [1, 2, 3, 4], 0, 1, 2)`

<br>

2.  **Inside `com`:**

      * **Base Case:** `if start >= n or end > n` is `if 0 >= 4 or 1 > 4`, which is `False`. The function continues.
      * **Building `part`:** `part` becomes `[new[0]]`, which is `[1]`.
      * The `extend` line is where the first issue appears: `part.extend(new[end:k+end-1])`. With `end = 1` and `k = 2`, the slice is `new[1:1+2-1]`, which is `new[1:2]`. So, `part` becomes `[1, 2]`. This is your first combination.
      * **Appending `ran`:** The `if len(part) == k` check is `if len([1, 2]) == 2`, which is `True`. So, `ran` is appended with `[1, 2]`. Now, `ran = [[1, 2]]`.

<br>
    
3.  **The First Recursive Call (Problem Area \#1):**

      * The code enters `if end + 1 < n`, which is `if 1 + 1 < 4`, which is `True`.
      * It then increments `end` to `2` and makes a recursive call: `com(ran, new, 0, 2, 2)`.
      * This is where things start to go wrong. The function calls itself, but it never "un-chooses" anything. It just keeps adding to `ran`.

<br>
    
4.  **Inside the Second Call:** `com(ran, [1, 2, 3, 4], 0, 2, 2)`

      * The base case is still `False`.
      * `part` becomes `[1]`. The slice `new[end:k+end-1]` is `new[2:2+2-1]`, which is `new[2:3]`. So `part` becomes `[1, 3]`.
      * Since `len([1, 3]) == 2`, this combination is also added to `ran`. Now, `ran = [[1, 2], [1, 3]]`.
      * It hits the `if end + 1 < n` again (`if 2 + 1 < 4` is `True`) and calls itself recursively. `end` becomes `3`, and the call is `com(ran, new, 0, 3, 2)`.

<br>
    
5.  **Inside the Third Call:** `com(ran, [1, 2, 3, 4], 0, 3, 2)`

      * The base case is still `False`.
      * `part` becomes `[1]`. The slice is `new[3:3+2-1]`, which is `new[3:4]`. So `part` becomes `[1, 4]`.
      * This combination is added to `ran`. Now, `ran = [[1, 2], [1, 3], [1, 4]]`.
      * The condition `if end + 1 < n` is `if 3 + 1 < 4`, which is `False`. So this path stops here.


6.  **The Code Resumes (Problem Area \#2):**

      * The previous call to `com` returns. The code now continues from the third recursive call where it last left off.
      * It hits these lines: `start = start + 1`, `end = start + 1`. This is a major issue. You're trying to move to the next starting number (e.g., from `1` to `2`), but you've lost the state of your recursion.
      * `start` becomes `0 + 1 = 1`. `end` becomes `1 + 1 = 2`.
      * It then checks `if start < n`, which is `if 1 < 4`, which is `True`.
      * **It makes a second recursive call:** `com(ran, new, 1, 2, 2)`.
      * This is where the infinite loop begins. You've essentially just told the code to start over from a new `start` point, but the first recursive call's state is completely lost. This pattern repeats indefinitely, creating new combinations but never properly terminating the entire process.









<br><br><br><br><br>

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

