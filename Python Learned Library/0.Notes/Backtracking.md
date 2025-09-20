
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
