

# List Comprehension in Python

List comprehension is a **concise way to create lists** by applying an expression to each item of an iterable (e.g., list, range, tuple) with optional filtering conditions.

It often replaces verbose `for` loops, making the code shorter and easier to read.

---

## Syntax

```python
[expression for item in iterable if condition]
```

* **expression** → The value or transformation to add to the new list.
* **item** → The variable representing the current element.
* **iterable** → Any sequence (list, tuple, set, range, string).
* **if condition** (optional) → A filter to decide whether to include the item.

---

## Example: Squaring Numbers

```python
a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)  
# [4, 9, 16, 25]
```

---

## For Loop vs. List Comprehension

**Using a `for` loop:**

```python
a = [1, 2, 3, 4, 5]
res = []
for val in a:
    res.append(val * 2)
print(res)
# [2, 4, 6, 8, 10]
```

**Using list comprehension:**

```python
res = [val * 2 for val in a]
print(res)
# [2, 4, 6, 8, 10]
```

 Both give the same result, but list comprehension is more compact.

---

## Conditional Filtering

### Filter items with `if`

```python
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)
# [2, 4]
```

### Apply different expressions with `if-else`

```python
numbers = ['even' if x % 2 == 0 else 'odd' for x in range(1, 11)]
print(numbers)
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
```

**Summary:**

* `if` **after `for`** → filters items.
* `if-else` **before `for`** → applies conditional expression.

---

## More Examples

### Range

```python
nums = [i for i in range(10)]
print(nums)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Nested Loops

```python
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

### Flatten a Matrix

```python
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in mat for val in row]
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Real Problems (LeetCode-style)

### 1. Kids With Candies

```python
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    return [x + extraCandies >= max(candies) for x in candies]

print(kidsWithCandies([2,3,5,1,3], 3))
# [True, True, True, False, True]
```

---

### 2. Largest Odd Number in String

```python
def largestOddNumber(num: str) -> str:
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]
    return ""

print(largestOddNumber("4206"))  
# ""
print(largestOddNumber("35427"))  
# "35427"
```

⚡ Optimized vs. brute force substring list comprehension (which was in your draft).

---

### 3. Increasing Removable Subarrays

```python
import numpy as np

def incremovableSubarrayCount(nums: list[int]) -> int:
    subs = [nums[:i] + nums[j:] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]
    return sum(all(np.diff(s) > 0) for s in subs)

print(incremovableSubarrayCount([8,7,6,6]))
# 0
```

---

## Pros & Cons

 Pros:

* Concise and elegant.
* Usually faster than traditional `for` loops.
* Easy to combine transformations and filters.

 Cons:

* Can become unreadable if too complex (e.g., deeply nested loops).
* Debugging inside a comprehension is harder.

---

## Quick Recap

* **Basic:** `[expr for item in iterable]`
* **Filter:** `[expr for item in iterable if condition]`
* **If-Else:** `[expr_if_true if cond else expr_if_false for item in iterable]`
* **Nested:** `[expr for i in iter1 for j in iter2]`

