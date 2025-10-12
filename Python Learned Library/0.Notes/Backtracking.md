
# Backtracking

Backtracking is a **recursive problem-solving technique** used to build a solution incrementally and undo ("backtrack") choices that don’t lead to a valid or optimal solution.

It tries all possible paths, and if a path doesn't work, it goes back (or “backtracks”) to try the next option.




# Example 1

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








<br><br><br><br><br><br><br><br>

# Example 2


```python
def minPathSum(grid: list[list[int]]) -> int:
    cols = len(grid[0])
    rows = len(grid)
    path = []
    sums = []

    def dfs(r, c):
        # if out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        # add current cell
        path.append(grid[r][c])

        # if we reached bottom-right, record path sum
        if r == rows - 1 and c == cols - 1:
            sums.append(sum(path))
        else:
            # move right
            dfs(r, c + 1)
            # move down
            dfs(r + 1, c)

        # backtrack
        path.pop()

    dfs(0, 0)   # always start top-left

    return min(sums)


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
```


Absolutely! Let’s go **step by step** and see exactly how recursion and `path.pop()` work together in your `minPathSum` function. We’ll use your example grid:

```
grid = [
 [1, 3, 1],
 [1, 5, 1],
 [4, 2, 1]
]
```

---

### Step 0 — Initial state

```python
path = []
sums = []
dfs(0, 0)
```

* We start at the top-left: `r = 0, c = 0`.
* `path = []`

---

### Step 1 — Visit (0,0)

```python
path.append(grid[0][0])  # append 1
```

* `path = [1]`
* Not bottom-right, so we recurse **right** first: `dfs(0, 1)`

---

### Step 2 — Visit (0,1)

```python
path.append(grid[0][1])  # append 3
```

* `path = [1, 3]`
* Not bottom-right → recurse **right**: `dfs(0, 2)`

---

### Step 3 — Visit (0,2)

```python
path.append(grid[0][2])  # append 1
```

* `path = [1, 3, 1]`
* Not bottom-right → try **right**: `dfs(0, 3)` → **out of bounds**, returns.
* Then try **down**: `dfs(1, 2)`

---

### Step 4 — Visit (1,2)

```python
path.append(grid[1][2])  # append 1
```

* `path = [1, 3, 1, 1]`
* Not bottom-right → recurse right: `dfs(1,3)` → out of bounds → returns.
* Then recurse down: `dfs(2,2)`

---

### Step 5 — Visit (2,2) → Bottom-right

```python
path.append(grid[2][2])  # append 1
```

* `path = [1, 3, 1, 1, 1]`
* Bottom-right reached → compute sum: `sum(path) = 7`
* Append to `sums`: `sums = [7]`

---

### Step 6 — Backtrack from (2,2)

```python
path.pop()
```

* Remove last element (1) from `path`
* `path = [1, 3, 1, 1]`
* Control returns to the call at (1,2)

---

### Step 7 — Backtrack from (1,2)

```python
path.pop()
```

* Remove last element (1)
* `path = [1, 3, 1]`
* Control returns to the call at (0,2)
* Now DFS explores other directions (down already tried, right already done) → backtrack again

---

### Step 8 — Backtrack from (0,2)

```python
path.pop()
```

* Remove last element (1)
* `path = [1, 3]`
* Control returns to the call at (0,1)
* Now explore **down**: `dfs(1,1)`

---

### Step 9 — DFS explores new path (0,1 → 1,1)

```python
path.append(grid[1][1])  # append 5
```

* `path = [1, 3, 5]`
* And recursion continues similarly…

---

### 🔑 How `pop()` works

* **Every recursive call has its own “stack frame”**, but they **share the same `path` list**.
* `.append()` adds a value as you go deeper.
* When a call finishes exploring all options from that cell, `.pop()` **removes the last element**, restoring `path` to the state before this cell was added.
* This **undoes the move**, allowing other branches to explore without leftover values.

Think of it like:

```
path = []  # start
dfs(0,0)  # append 1
  dfs(0,1)  # append 3
    dfs(0,2)  # append 1
      dfs(1,2)  # append 1
        dfs(2,2)  # append 1, reached end, sum=7
        pop()  # remove last 1
      pop()  # remove 1 from (1,2)
    pop()  # remove 1 from (0,2)
  pop()  # remove 3 from (0,1)
pop()  # remove 1 from (0,0)
```

* At each pop, the **list returns to the previous state**, allowing DFS to explore **all possible paths**.

---

### ✅ Final Result

All paths from top-left to bottom-right are explored, sums collected, and the **minimum path sum** is returned:

```
print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
```

```python
"""
In bounds: (0, 0)
In bounds: (0, 1)
In bounds: (0, 2)
Returning: (0, 3) out of bounds
In bounds: (1, 2)
Returning: (1, 3) out of bounds
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Removing: (1, 2)
Removing: (0, 2)
In bounds: (1, 1)
In bounds: (1, 2)
Returning: (1, 3) out of bounds
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Removing: (1, 2)
In bounds: (2, 1)
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Returning: (3, 1) out of bounds
Removing: (2, 1)
Removing: (1, 1)
Removing: (0, 1)
In bounds: (1, 0)
In bounds: (1, 1)
In bounds: (1, 2)
Returning: (1, 3) out of bounds
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Removing: (1, 2)
In bounds: (2, 1)
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Returning: (3, 1) out of bounds
Removing: (2, 1)
Removing: (1, 1)
In bounds: (2, 0)
In bounds: (2, 1)
In bounds: (2, 2)
Reached the end (2, 2)
Removing: (2, 2)
Returning: (3, 1) out of bounds
Removing: (2, 1)
Returning: (3, 0) out of bounds
Removing: (2, 0)
Removing: (1, 0)
Removing: (0, 0)
7"""




Start: [1]  (0,0)
├─ Right → [1,3]  (0,1)
│   ├─ Right → [1,3,1]  (0,2)
│   │   ├─ Down → [1,3,1,1]  (1,2)
│   │   │   ├─ Down → [1,3,1,1,1]  (2,2) ✔ sum=7
│   │   │   └─ Backtrack → [1,3,1,1]
│   │   └─ Backtrack → [1,3,1]
│   └─ Down → [1,3,5]  (1,1)
│       ├─ Right → [1,3,5,1]  (1,2)
│       │   ├─ Down → [1,3,5,1,1]  (2,2) ✔ sum=11
│       │   └─ Backtrack → [1,3,5,1]
│       └─ Down → [1,3,5,2]  (2,1)
│           ├─ Right → [1,3,5,2,1]  (2,2) ✔ sum=12
│           └─ Backtrack → [1,3,5,2]
│       └─ Backtrack → [1,3,5]
│   └─ Backtrack → [1,3]
└─ Down → [1,1]  (1,0)
    ├─ Right → [1,1,5]  (1,1)
    │   ├─ Right → [1,1,5,1]  (1,2)
    │   │   ├─ Down → [1,1,5,1,1]  (2,2) ✔ sum=9
    │   │   └─ Backtrack → [1,1,5,1]
    │   └─ Down → [1,1,5,2]  (2,1)
    │       ├─ Right → [1,1,5,2,1]  (2,2) ✔ sum=10
    │       └─ Backtrack → [1,1,5,2]
    │   └─ Backtrack → [1,1,5]
    └─ Down → [1,1,4]  (2,0)
        ├─ Right → [1,1,4,2]  (2,1)
        │   ├─ Right → [1,1,4,2,1]  (2,2) ✔ sum=9
        │   └─ Backtrack → [1,1,4,2]
        └─ Down → [1,1,4]  (3,0) → out of bounds → return
    └─ Backtrack → [1,1]
└─ Backtrack → [1]
```




<br><br><br><br><br><br><br>

# Example 2


```python
def letterCasePermutation(s: str) -> list[str]:
    result = []
    path = []

    def backtrack(index: int):
        print("---- PASS THROUGH ----")
        if index == len(s):
            print("ADDED TO RESULT (NO CAP):  ",path)
            result.append("".join(path))
            return

        char = s[index]

        print("Path: ",path)

        path.append(char)
        backtrack(index + 1)
        path.pop()
        print("POP", char)
        print("AFTER POP:  ", path)

        if char.isalpha():
            print("IT'S A LETTER, it now passes the through:  ",char)
            path.append(char.swapcase())
            print("Added to the path:  ",char.swapcase())
            print("ADDED TO RESULT (CAP):  ", path)
            backtrack(index + 1)
            print("POP (CAP)", char.swapcase())
            path.pop()

    backtrack(0)
    return result


print(letterCasePermutation("a1b2"))





---- PASS THROUGH ----
Path:  []

---- PASS THROUGH ----
Path:  ['a']

---- PASS THROUGH ----
Path:  ['a', '1']

---- PASS THROUGH ----
Path:  ['a', '1', 'b']

---- PASS THROUGH ----
ADDED TO RESULT (NO CAP):   ['a', '1', 'b', '2']
POP 2
AFTER POP:   ['a', '1', 'b']
POP b
AFTER POP:   ['a', '1']
IT'S A LETTER, it now passes the through:   b
Added to the path:   B
ADDED TO RESULT (CAP):   ['a', '1', 'B']

---- PASS THROUGH ----
Path:  ['a', '1', 'B']

---- PASS THROUGH ----
ADDED TO RESULT (NO CAP):   ['a', '1', 'B', '2']
POP 2
AFTER POP:   ['a', '1', 'B']
POP (CAP) B
POP 1
AFTER POP:   ['a']
POP a
AFTER POP:   []
IT'S A LETTER, it now passes the through:   a
Added to the path:   A
ADDED TO RESULT (CAP):   ['A']

---- PASS THROUGH ----
Path:  ['A']

---- PASS THROUGH ----
Path:  ['A', '1']

---- PASS THROUGH ----
Path:  ['A', '1', 'b']

---- PASS THROUGH ----
ADDED TO RESULT (NO CAP):   ['A', '1', 'b', '2']
POP 2
AFTER POP:   ['A', '1', 'b']
POP b
AFTER POP:   ['A', '1']
IT'S A LETTER, it now passes the through:   b
Added to the path:   B
ADDED TO RESULT (CAP):   ['A', '1', 'B']

---- PASS THROUGH ----
Path:  ['A', '1', 'B']

---- PASS THROUGH ----
ADDED TO RESULT (NO CAP):   ['A', '1', 'B', '2']
POP 2
AFTER POP:   ['A', '1', 'B']
POP (CAP) B
POP 1
AFTER POP:   ['A']
POP (CAP) A
['a1b2', 'a1B2', 'A1b2', 'A1B2']
````





<br><br><br><br><br><br><br>

# Example 4

```python
def solveNQueens(n: int) -> list[list[str]]:
    grid = [["." for _ in range(n)] for _ in range(n)]
    all_q = []

    def dfs(r: int):
        if r == n:  # base case: placed queens in all rows
            # make a copy of the board as strings
            solution = ["".join(row) for row in grid]
            all_q.append(solution)
            return

        for y in range(n):
            valid = True

            # check column
            for x in range(r):
                if grid[x][y] == "Q":
                    valid = False
                    break

            # check diagonal ↖
            i, j = r - 1, y - 1
            while i >= 0 and j >= 0:
                if grid[i][j] == "Q":
                    valid = False
                    break
                i -= 1
                j -= 1

            # check diagonal ↗
            i, j = r - 1, y + 1
            while i >= 0 and j < n:
                if grid[i][j] == "Q":
                    valid = False
                    break
                i -= 1
                j += 1

            if not valid:
                continue

            # place queen
            grid[r][y] = "Q"

            # recurse
            dfs(r + 1)

            # backtrack (reset state)
            grid[r][y] = "."

    dfs(0)
    return all_q
```




<br><br><br><br><br>

# Example 5


```python
def uniquePathsIII(grid: list[list[int]]) -> int:

    visted = list()
    col_b = len(grid[0])
    row_b = len(grid)
    full_walk = []
    ones = sum(1 for x in grid for y in x if y == -1)

    def dfs(r,c):
        if (r,c) in visted or r < 0 or r >= row_b or c < 0 or c >= col_b or grid[r][c] == -1:
            print("out: ",(r, c))
            return

        visted.append((r,c))

        print((r,c))

        if grid[r][c] == 2 and len(visted) == col_b * row_b - ones:
            print("got it",(r,c))
            full_walk.append(visted[:])

        else:
            dfs(r,c+1)
            print((r, c))
            dfs(r+1,c)
            print((r, c))
            dfs(r,c-1)
            print((r, c))
            dfs(r-1,c)

        visted.pop()

    # r, c = next((i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 1)
    x = [[i,j] for i,x in enumerate(grid) for j,y in enumerate(x) if y ==1]
    r = x[0][0]
    c = x[0][1]
    dfs(r,c)

    print(full_walk)

    return len(full_walk)
```





