
####################################################################
# Perfect Numbers and Generators in Python
####################################################################

## Perfect Number

A **perfect number** is a positive integer that is equal to the sum of its **positive divisors**, excluding the number itself.  

- **Divisor**: An integer that divides another integer evenly.  

**Problem:** Given an integer `n`, return `True` if `n` is a perfect number, otherwise return `False`.

**Example 1:**
```text
Input: num = 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
````

**Example 2:**

```text
Input: num = 7
Output: False
```

**Python implementation:**

```python
def diviser(number: int):
    total = sum(x for x in range(1, number) if number % x == 0)
    return total == number

print(diviser(27))  # Output: False
```

---

## Yield Keyword in Python

* The `yield` keyword turns a function into a **generator**, producing values lazily, one at a time.
* **Difference between `return` and `yield`:**

  * `return` ends the function and returns a value.
  * `yield` pauses the function, saving its state, and returns a generator object. Execution resumes when the generator is iterated again.

**Advantages:**

* Memory-efficient: Generates values one at a time.
* Can pause and resume, keeping variable states.

**Disadvantages:**

* Harder to trace control flow.
* Generator functions need careful handling.

---

## Problem 1: Generator for Squares

```python
def gensquare(n):
    for x in range(n):
        yield x**2

for number in gensquare(10):
    print(number)
```

**Output:**

```
0
1
4
9
16
25
36
49
64
81
```

---

## ✅ Problem 2: Generator for Random Numbers

```python
import random

def rand_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)
```

**Output (example, random each time):**

```
7
5
1
10
9
4
2
5
5
1
6
7
```

---

## Problem 3: Using `iter()` on a string

```python
s = 'hello'
s_iter = iter(s)
print(next(s_iter))  # Output: h
```

---

## Generator Comprehension

```python
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
```

**Output:**

```
4
5
```

* `gencomp` is a **generator comprehension** that yields items lazily.

---

## Advanced Example: Maximum Profit with Generators and Numpy

```python
import numpy as np
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = np.array(np.diff(prices))  # daily differences
        substrings = (
            sum(diff[i:j])
            for i in range(len(diff)) if diff[i] > 0
            for j in range(i + 1, len(diff) + 1)
        )
        return int(max(substrings))

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
```

**Explanation:**

1. `np.diff(prices)` calculates daily price changes.
2. `substrings` generator sums all possible positive profit segments.
3. `max()` finds the maximum profit.

---