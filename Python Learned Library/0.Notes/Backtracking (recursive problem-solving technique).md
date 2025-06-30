
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