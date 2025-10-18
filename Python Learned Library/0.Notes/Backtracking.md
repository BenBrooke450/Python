
# Backtracking

Backtracking is a **recursive problem-solving technique** used to build a solution incrementally and undo ("backtrack") choices that don’t lead to a valid or optimal solution.

It tries all possible paths, and if a path doesn't work, it goes back (or “backtracks”) to try the next option.




# Example 1

#### In this example it's important to understand the difference between taking the path through the recursion and not.

```python
nums = [1,2,3]
def backtrack(start, path):
    print()
    print("------ENTER BACKTRACK--------")
    print("TRYING", f"Start: {start}, End_len: {len(nums)}")
    print()
    for i in range(start, len(nums)):
        print(f"append: {[nums[i]]}      Start: {start}, End_len: {len(nums)}")
        path.append(nums[i])
        print("Path:  ",path)


        backtrack(i + 1, path)
        print()
        print("-----DROP OUT----- :",f"Start: {start+1}, End_len: {len(nums)}")
        print()

        print(f"Path before drop {path}")
        path.pop()
        print(f"Path after drop {path}")
        print()
        
        
        
        

------ENTER BACKTRACK--------
TRYING Start: 0, End_len: 3

append: [1]      Start: 0, End_len: 3
Path:   [1]

------ENTER BACKTRACK--------
TRYING Start: 1, End_len: 3

append: [2]      Start: 1, End_len: 3
Path:   [1, 2]

------ENTER BACKTRACK--------
TRYING Start: 2, End_len: 3

append: [3]      Start: 2, End_len: 3
Path:   [1, 2, 3]

------ENTER BACKTRACK--------
TRYING Start: 3, End_len: 3


#### HERE WE HAVE REACHED THE MAX POINT AND THE INTERATION HAS FAILED CAUSING THE RETURN


-----DROP OUT----- : Start: 3, End_len: 3

Path before drop [1, 2, 3]

```

#### We don't pop the last element here, because we have taken the path through the recursion, when it failes we go back to the previous path which is simply [1,2] and then we pop again as we retuned 

```python

Path after drop [1, 2]


-----DROP OUT----- : Start: 2, End_len: 3

Path before drop [1, 2]
Path after drop [1]

append: [3]      Start: 1, End_len: 3
Path:   [1, 3]

------ENTER BACKTRACK--------
TRYING Start: 3, End_len: 3


-----DROP OUT----- : Start: 2, End_len: 3

Path before drop [1, 3]
Path after drop [1]


-----DROP OUT----- : Start: 1, End_len: 3

Path before drop [1]
Path after drop []

append: [2]      Start: 0, End_len: 3
Path:   [2]

------ENTER BACKTRACK--------
TRYING Start: 2, End_len: 3

append: [3]      Start: 2, End_len: 3
Path:   [2, 3]

------ENTER BACKTRACK--------
TRYING Start: 3, End_len: 3


-----DROP OUT----- : Start: 3, End_len: 3

Path before drop [2, 3]
Path after drop [2]


-----DROP OUT----- : Start: 1, End_len: 3

Path before drop [2]
Path after drop []

append: [3]      Start: 0, End_len: 3
Path:   [3]

------ENTER BACKTRACK--------
TRYING Start: 3, End_len: 3


-----DROP OUT----- : Start: 1, End_len: 3

Path before drop [3]
Path after drop []
```



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

Excellent question again 👏 — and now you’re asking the *deep* conceptual one:


<br><br><br><br>

> “What happens if I don’t take the list (`path`) into the recursion, and instead only pass the pointer or current index?”

Let’s unpack that carefully, because it changes the **entire nature of recursion** and **how state is maintained**.

---

## 🧩 Original: list *passed down* the recursion

Here’s your version again:

```python
nums = [1,2,3]

def backtrack(start, path):
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

backtrack(0, [])
```

### How it behaves

* Each recursive call *shares and mutates* the same `path` list.
* The append/pop pattern ensures the same list object tracks the *current path*.
* The recursion tree looks like this:

```
[]
 ├── [1]
 │    ├── [1,2]
 │    │    └── [1,2,3]
 │    └── [1,3]
 └── [2]
      └── [2,3]
           └── [3]
```

Each `backtrack` call represents a “branch” that can grow (append) and shrink (pop).

---

## 🧩 Now imagine: you *don’t* carry the list — only the pointer (index)

Let’s say you did this:

```python
nums = [1,2,3]

def backtrack(start):
    for i in range(start, len(nums)):
        print(nums[i])
        backtrack(i + 1)

backtrack(0)
```

### What happens now

* You’re no longer carrying a list (`path`).
* You print or process *individual elements*.
* Each call only knows its **current position**, not the path taken to reach it.

So the output looks like this:

```
1
2
3
2
3
3
```

and not structured combinations.

That’s because nothing is keeping track of “what led to this point” —
each recursion just says “here’s the next element,” not “here’s the whole path so far.”

---

### If you *simulate* the same recursion but rebuild path at each step

You could still build the path locally (without mutating the same list) like this:

```python
def backtrack(start, path):
    for i in range(start, len(nums)):
        new_path = path + [nums[i]]  # new list each time
        print(new_path)
        backtrack(i + 1, new_path)
```

Now `path` is *not shared* between calls — every call owns its own list.

### Output:

```
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
```

Same logical result, but no `pop()` needed.

---

## Key difference explained

| Version               | What’s Passed        | Shared State? | Needs pop()? | Memory Use | Notes                      |
| --------------------- | -------------------- | ------------- | ------------ | ---------- | -------------------------- |
| **Your version**      | Same `path` list     | ✅ Yes         | ✅ Yes        | Low        | Classic backtracking style |
| **Copy-on-recursion** | New list each call   | ❌ No          | ❌ No         | Higher     | Simpler mentally           |
| **Pointer-only**      | Just index (`start`) | ❌ No          | ❌ No         | Lowest     | Can’t reconstruct path     |

---

## Intuitive analogy

Think of it like a trail in a maze:

* **Original (`path` shared)**: you walk with a notepad, writing down each turn (`append`) and erasing when backtracking (`pop`).
* **Copy each time (`path + [x]`)**: you make a photocopy of your notepad at every junction — more memory, but each copy is independent.
* **Pointer-only (`start`)**: you walk without writing anything — you know where you are, but not how you got there.

---

## TL;DR

If you only carry the *pointer* (like `start`) and don’t take the list (`path`):

* You **lose memory of the path** you took to get there.
* You can still recurse through indices, but you can’t build combinations or sequences.
* To reconstruct combinations, you must either:

  * Carry a shared `path` (and backtrack with `pop()`), **or**
  * Create a new list each recursive call (`path + [nums[i]]`).








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

# Example 3

```python


def combinationSum3(k: int, n: int) -> list[list[int]]:

    nine = []
    result = []

    def sum_nums_back(start,path):
        for i in range(start,n+1):
            print(i)
            print("Path:  ", path)
            new_path = path + [i]
            print("New path:  ",new_path)

            if sum(new_path) == n and len(new_path) == k:
                result.append(new_path)
                continue

            if len(new_path) < k:
                print("----Next Step----  ", new_path)
                sum_nums_back(i + 1, new_path)
                print("-----DROPPING out of the loop------")

            new_path.pop()
            print("Pop:  ", new_path)

    sum_nums_back(start=1,path=[])

    return result

print(combinationSum3(3,9))
    

1
Path:   []
New path:   [1]
----Next Step----   [1]
2
Path:   [1]
New path:   [1, 2]
----Next Step----   [1, 2]
3
Path:   [1, 2]
New path:   [1, 2, 3]
Pop:   [1, 2]
4
Path:   [1, 2]
New path:   [1, 2, 4]
Pop:   [1, 2]
5
Path:   [1, 2]
New path:   [1, 2, 5]
Pop:   [1, 2]
6
Path:   [1, 2]
New path:   [1, 2, 6]
7
Path:   [1, 2]
New path:   [1, 2, 7]
Pop:   [1, 2]
8
Path:   [1, 2]
New path:   [1, 2, 8]
Pop:   [1, 2]
9
Path:   [1, 2]
New path:   [1, 2, 9]
Pop:   [1, 2]
-----DROPPING out of the loop------
Pop:   [1]
3
Path:   [1]
New path:   [1, 3]
----Next Step----   [1, 3]
4
Path:   [1, 3]
New path:   [1, 3, 4]
Pop:   [1, 3]
5
Path:   [1, 3]
New path:   [1, 3, 5]
6
Path:   [1, 3]
New path:   [1, 3, 6]
Pop:   [1, 3]
7
Path:   [1, 3]
New path:   [1, 3, 7]
Pop:   [1, 3]
8
Path:   [1, 3]
New path:   [1, 3, 8]
Pop:   [1, 3]
9
Path:   [1, 3]
New path:   [1, 3, 9]
Pop:   [1, 3]
-----DROPPING out of the loop------
Pop:   [1]
4
Path:   [1]
New path:   [1, 4]
----Next Step----   [1, 4]
5
Path:   [1, 4]
New path:   [1, 4, 5]
Pop:   [1, 4]
6
Path:   [1, 4]
New path:   [1, 4, 6]
Pop:   [1, 4]
7
Path:   [1, 4]
New path:   [1, 4, 7]
Pop:   [1, 4]
8
Path:   [1, 4]
New path:   [1, 4, 8]
Pop:   [1, 4]
9
Path:   [1, 4]
New path:   [1, 4, 9]
Pop:   [1, 4]
-----DROPPING out of the loop------
Pop:   [1]
5
Path:   [1]
New path:   [1, 5]
----Next Step----   [1, 5]
6
Path:   [1, 5]
New path:   [1, 5, 6]
Pop:   [1, 5]
7
Path:   [1, 5]
New path:   [1, 5, 7]
Pop:   [1, 5]
8
Path:   [1, 5]
New path:   [1, 5, 8]
Pop:   [1, 5]
9
Path:   [1, 5]
New path:   [1, 5, 9]
Pop:   [1, 5]
-----DROPPING out of the loop------
Pop:   [1]
6
Path:   [1]
New path:   [1, 6]
----Next Step----   [1, 6]
7
Path:   [1, 6]
New path:   [1, 6, 7]
Pop:   [1, 6]
8
Path:   [1, 6]
New path:   [1, 6, 8]
Pop:   [1, 6]
9
Path:   [1, 6]
New path:   [1, 6, 9]
Pop:   [1, 6]
-----DROPPING out of the loop------
Pop:   [1]
7
Path:   [1]
New path:   [1, 7]
----Next Step----   [1, 7]
8
Path:   [1, 7]
New path:   [1, 7, 8]
Pop:   [1, 7]
9
Path:   [1, 7]
New path:   [1, 7, 9]
Pop:   [1, 7]
-----DROPPING out of the loop------
Pop:   [1]
8
Path:   [1]
New path:   [1, 8]
----Next Step----   [1, 8]
9
Path:   [1, 8]
New path:   [1, 8, 9]
Pop:   [1, 8]
-----DROPPING out of the loop------
Pop:   [1]
9
Path:   [1]
New path:   [1, 9]
----Next Step----   [1, 9]
-----DROPPING out of the loop------
Pop:   [1]
-----DROPPING out of the loop------
Pop:   []
2
Path:   []
New path:   [2]
----Next Step----   [2]
3
Path:   [2]
New path:   [2, 3]
----Next Step----   [2, 3]
4
Path:   [2, 3]
New path:   [2, 3, 4]
5
Path:   [2, 3]
New path:   [2, 3, 5]
Pop:   [2, 3]
6
Path:   [2, 3]
New path:   [2, 3, 6]
Pop:   [2, 3]
7
Path:   [2, 3]
New path:   [2, 3, 7]
Pop:   [2, 3]
8
Path:   [2, 3]
New path:   [2, 3, 8]
Pop:   [2, 3]
9
Path:   [2, 3]
New path:   [2, 3, 9]
Pop:   [2, 3]
-----DROPPING out of the loop------
Pop:   [2]
4
Path:   [2]
New path:   [2, 4]
----Next Step----   [2, 4]
5
Path:   [2, 4]
New path:   [2, 4, 5]
Pop:   [2, 4]
6
Path:   [2, 4]
New path:   [2, 4, 6]
Pop:   [2, 4]
7
Path:   [2, 4]
New path:   [2, 4, 7]
Pop:   [2, 4]
8
Path:   [2, 4]
New path:   [2, 4, 8]
Pop:   [2, 4]
9
Path:   [2, 4]
New path:   [2, 4, 9]
Pop:   [2, 4]
-----DROPPING out of the loop------
Pop:   [2]
5
Path:   [2]
New path:   [2, 5]
----Next Step----   [2, 5]
6
Path:   [2, 5]
New path:   [2, 5, 6]
Pop:   [2, 5]
7
Path:   [2, 5]
New path:   [2, 5, 7]
Pop:   [2, 5]
8
Path:   [2, 5]
New path:   [2, 5, 8]
Pop:   [2, 5]
9
Path:   [2, 5]
New path:   [2, 5, 9]
Pop:   [2, 5]
-----DROPPING out of the loop------
Pop:   [2]
6
Path:   [2]
New path:   [2, 6]
----Next Step----   [2, 6]
7
Path:   [2, 6]
New path:   [2, 6, 7]
Pop:   [2, 6]
8
Path:   [2, 6]
New path:   [2, 6, 8]
Pop:   [2, 6]
9
Path:   [2, 6]
New path:   [2, 6, 9]
Pop:   [2, 6]
-----DROPPING out of the loop------
Pop:   [2]
7
Path:   [2]
New path:   [2, 7]
----Next Step----   [2, 7]
8
Path:   [2, 7]
New path:   [2, 7, 8]
Pop:   [2, 7]
9
Path:   [2, 7]
New path:   [2, 7, 9]
Pop:   [2, 7]
-----DROPPING out of the loop------
Pop:   [2]
8
Path:   [2]
New path:   [2, 8]
----Next Step----   [2, 8]
9
Path:   [2, 8]
New path:   [2, 8, 9]
Pop:   [2, 8]
-----DROPPING out of the loop------
Pop:   [2]
9
Path:   [2]
New path:   [2, 9]
----Next Step----   [2, 9]
-----DROPPING out of the loop------
Pop:   [2]
-----DROPPING out of the loop------
Pop:   []
3
Path:   []
New path:   [3]
----Next Step----   [3]
4
Path:   [3]
New path:   [3, 4]
----Next Step----   [3, 4]
5
Path:   [3, 4]
New path:   [3, 4, 5]
Pop:   [3, 4]
6
Path:   [3, 4]
New path:   [3, 4, 6]
Pop:   [3, 4]
7
Path:   [3, 4]
New path:   [3, 4, 7]
Pop:   [3, 4]
8
Path:   [3, 4]
New path:   [3, 4, 8]
Pop:   [3, 4]
9
Path:   [3, 4]
New path:   [3, 4, 9]
Pop:   [3, 4]
-----DROPPING out of the loop------
Pop:   [3]
5
Path:   [3]
New path:   [3, 5]
----Next Step----   [3, 5]
6
Path:   [3, 5]
New path:   [3, 5, 6]
Pop:   [3, 5]
7
Path:   [3, 5]
New path:   [3, 5, 7]
Pop:   [3, 5]
8
Path:   [3, 5]
New path:   [3, 5, 8]
Pop:   [3, 5]
9
Path:   [3, 5]
New path:   [3, 5, 9]
Pop:   [3, 5]
-----DROPPING out of the loop------
Pop:   [3]
6
Path:   [3]
New path:   [3, 6]
----Next Step----   [3, 6]
7
Path:   [3, 6]
New path:   [3, 6, 7]
Pop:   [3, 6]
8
Path:   [3, 6]
New path:   [3, 6, 8]
Pop:   [3, 6]
9
Path:   [3, 6]
New path:   [3, 6, 9]
Pop:   [3, 6]
-----DROPPING out of the loop------
Pop:   [3]
7
Path:   [3]
New path:   [3, 7]
----Next Step----   [3, 7]
8
Path:   [3, 7]
New path:   [3, 7, 8]
Pop:   [3, 7]
9
Path:   [3, 7]
New path:   [3, 7, 9]
Pop:   [3, 7]
-----DROPPING out of the loop------
Pop:   [3]
8
Path:   [3]
New path:   [3, 8]
----Next Step----   [3, 8]
9
Path:   [3, 8]
New path:   [3, 8, 9]
Pop:   [3, 8]
-----DROPPING out of the loop------
Pop:   [3]
9
Path:   [3]
New path:   [3, 9]
----Next Step----   [3, 9]
-----DROPPING out of the loop------
Pop:   [3]
-----DROPPING out of the loop------
Pop:   []
4
Path:   []
New path:   [4]
----Next Step----   [4]
5
Path:   [4]
New path:   [4, 5]
----Next Step----   [4, 5]
6
Path:   [4, 5]
New path:   [4, 5, 6]
Pop:   [4, 5]
7
Path:   [4, 5]
New path:   [4, 5, 7]
Pop:   [4, 5]
8
Path:   [4, 5]
New path:   [4, 5, 8]
Pop:   [4, 5]
9
Path:   [4, 5]
New path:   [4, 5, 9]
Pop:   [4, 5]
-----DROPPING out of the loop------
Pop:   [4]
6
Path:   [4]
New path:   [4, 6]
----Next Step----   [4, 6]
7
Path:   [4, 6]
New path:   [4, 6, 7]
Pop:   [4, 6]
8
Path:   [4, 6]
New path:   [4, 6, 8]
Pop:   [4, 6]
9
Path:   [4, 6]
New path:   [4, 6, 9]
Pop:   [4, 6]
-----DROPPING out of the loop------
Pop:   [4]
7
Path:   [4]
New path:   [4, 7]
----Next Step----   [4, 7]
8
Path:   [4, 7]
New path:   [4, 7, 8]
Pop:   [4, 7]
9
Path:   [4, 7]
New path:   [4, 7, 9]
Pop:   [4, 7]
-----DROPPING out of the loop------
Pop:   [4]
8
Path:   [4]
New path:   [4, 8]
----Next Step----   [4, 8]
9
Path:   [4, 8]
New path:   [4, 8, 9]
Pop:   [4, 8]
-----DROPPING out of the loop------
Pop:   [4]
9
Path:   [4]
New path:   [4, 9]
----Next Step----   [4, 9]
-----DROPPING out of the loop------
Pop:   [4]
-----DROPPING out of the loop------
Pop:   []
5
Path:   []
New path:   [5]
----Next Step----   [5]
6
Path:   [5]
New path:   [5, 6]
----Next Step----   [5, 6]
7
Path:   [5, 6]
New path:   [5, 6, 7]
Pop:   [5, 6]
8
Path:   [5, 6]
New path:   [5, 6, 8]
Pop:   [5, 6]
9
Path:   [5, 6]
New path:   [5, 6, 9]
Pop:   [5, 6]
-----DROPPING out of the loop------
Pop:   [5]
7
Path:   [5]
New path:   [5, 7]
----Next Step----   [5, 7]
8
Path:   [5, 7]
New path:   [5, 7, 8]
Pop:   [5, 7]
9
Path:   [5, 7]
New path:   [5, 7, 9]
Pop:   [5, 7]
-----DROPPING out of the loop------
Pop:   [5]
8
Path:   [5]
New path:   [5, 8]
----Next Step----   [5, 8]
9
Path:   [5, 8]
New path:   [5, 8, 9]
Pop:   [5, 8]
-----DROPPING out of the loop------
Pop:   [5]
9
Path:   [5]
New path:   [5, 9]
----Next Step----   [5, 9]
-----DROPPING out of the loop------
Pop:   [5]
-----DROPPING out of the loop------
Pop:   []
6
Path:   []
New path:   [6]
----Next Step----   [6]
7
Path:   [6]
New path:   [6, 7]
----Next Step----   [6, 7]
8
Path:   [6, 7]
New path:   [6, 7, 8]
Pop:   [6, 7]
9
Path:   [6, 7]
New path:   [6, 7, 9]
Pop:   [6, 7]
-----DROPPING out of the loop------
Pop:   [6]
8
Path:   [6]
New path:   [6, 8]
----Next Step----   [6, 8]
9
Path:   [6, 8]
New path:   [6, 8, 9]
Pop:   [6, 8]
-----DROPPING out of the loop------
Pop:   [6]
9
Path:   [6]
New path:   [6, 9]
----Next Step----   [6, 9]
-----DROPPING out of the loop------
Pop:   [6]
-----DROPPING out of the loop------
Pop:   []
7
Path:   []
New path:   [7]
----Next Step----   [7]
8
Path:   [7]
New path:   [7, 8]
----Next Step----   [7, 8]
9
Path:   [7, 8]
New path:   [7, 8, 9]
Pop:   [7, 8]
-----DROPPING out of the loop------
Pop:   [7]
9
Path:   [7]
New path:   [7, 9]
----Next Step----   [7, 9]
-----DROPPING out of the loop------
Pop:   [7]
-----DROPPING out of the loop------
Pop:   []
8
Path:   []
New path:   [8]
----Next Step----   [8]
9
Path:   [8]
New path:   [8, 9]
----Next Step----   [8, 9]
-----DROPPING out of the loop------
Pop:   [8]
-----DROPPING out of the loop------
Pop:   []
9
Path:   []
New path:   [9]
----Next Step----   [9]
-----DROPPING out of the loop------
Pop:   []
[[1, 2, 6], [1, 3, 5], [2, 3, 4]]

Process finished with exit code 0

```









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

# Example 4


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





