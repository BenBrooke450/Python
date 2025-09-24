

## Depth-First Search (DFS)

* **Definition**: Explore as far as possible along one path before going back.
* **IMPORTANT**: Will not remove prior paths so once point has been visited can't return.
* **How**: Implemented recursively or with a stack.
* **Use cases**:

  * Traversing trees and graphs.
  * Checking connectivity.
  * Topological sort.
* **Key point**: Dives deep before exploring siblings.

---

## Backtracking

* **Definition**: A refinement of DFS used to solve **constraint problems** (like puzzles).
* **How**: Explore one option → if it fails, undo (backtrack) and try another.
* **Use cases**:

  * Sudoku, N-Queens, word search.
  * Pathfinding with constraints.
* **Key point**: DFS + undo state >> **(so you can reuse choices).** <<

---

## Breadth-First Search (BFS)

* **Definition**: Explore neighbors first, then their neighbors — layer by layer.
* **How**: Implemented with a queue (FIFO).
* **Use cases**:

  * Shortest path in an unweighted graph.
  * Level-order traversal of a tree.
  * Social network “friend of a friend” problems.
* **Key point**: Expands outward evenly instead of diving deep.

---

### Quick analogy

* **DFS**: Explore one corridor in a maze until you hit a dead end.
* **Backtracking**: Like DFS, but erase your steps when you go back so you can try other corridors.
* **BFS**: Explore all corridors 1 step long, then all 2 steps long, etc.






<br><br><br><br><br><br><br>


## Examples


We’ll use a **2D grid (maze)** where `0 = free` and `1 = wall`.
Goal: find a path from **start (0,0)** to **end (2,2)**.

Grid:

```
S 0 1
0 0 0
1 0 E
```

---

## 1️⃣ Depth-First Search (DFS)

DFS explores as far as it can before backtracking naturally (via recursion).

```python
grid = [
    [0,0,1],
    [0,0,0],
    [1,0,0]
]
rows, cols = len(grid), len(grid[0])
end = (2,2)

def dfs(r, c, visited):
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1 or (r,c) in visited:
        return False
    
    if (r,c) == end:
        print("Reached end with DFS!")
        return True
    
    visited.add((r,c))
    
    # explore neighbors (down, right, up, left)
    return (dfs(r+1,c,visited) or 
            dfs(r,c+1,visited) or 
            dfs(r-1,c,visited) or 
            dfs(r,c-1,visited))

print("DFS result:", dfs(0,0,set()))
```

DFS will dive deep until it finds the goal (but it doesn’t guarantee shortest path).




---

<br>

## 2️⃣ Backtracking

Same as DFS, but explicitly **undo choices** to explore multiple paths (collecting all possible solutions).

```python

grid = [
    [0,0,1],
    [0,0,0],
    [1,0,0]
]
rows, cols = len(grid), len(grid[0])
end = (2,2)

path = []
solutions = []

def backtrack(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1 or (r,c) in path:
        return
    
    path.append((r,c))
    
    if (r,c) == end:
        solutions.append(path.copy())
    else:
        backtrack(r+1,c)
        backtrack(r,c+1)
        backtrack(r-1,c)
        backtrack(r,c-1)
    
    path.pop()  # undo choice

backtrack(0,0)
print("Backtracking found paths:", solutions)
```

Backtracking finds **all possible paths**, because it undoes each move (`path.pop()`).

---

<br>

## 3️⃣ Breadth-First Search (BFS)

BFS explores **level by level** → guarantees shortest path in unweighted grids.

```python
from collections import deque

def bfs(start):
    queue = deque([(start, [start])])  # (position, path)
    visited = set([start])
    
    while queue:
        (r,c), path = queue.popleft()
        
        if (r,c) == end:
            print("BFS shortest path:", path)
            return path
        
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                queue.append(((nr,nc), path+[(nr,nc)]))

bfs((0,0))
```

BFS will return the **shortest path**:

```
[(0,0), (1,0), (1,1), (2,1), (2,2)]
```

---

### Summary

* **DFS**: goes deep, stops when it finds one path.
* **Backtracking**: DFS + undo → finds **all paths**.
* **BFS**: explores level by level → finds the **shortest path**.

---

Would you like me to also make a **side-by-side visualization (like Plotly or ASCII)** so you can *see* how DFS vs BFS explores the grid differently?


