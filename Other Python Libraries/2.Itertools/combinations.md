
🔹 itertools.permutations(iterable, r)
	• Generates r-length tuples of all possible orderings of elements from the iterable.
	• Order matters.
	• No repeated elements (by default, unless your iterable has duplicates).
Example:

from itertools import permutations
list(permutations([1, 2, 3], 2))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


🔹 itertools.combinations(iterable, r)
	• Generates r-length tuples of all possible combinations without regard to order.
	• Order does not matter.
	• No repeated elements.

```python
from itertools import combinations
list(combinations([1, 2, 3], 2))
# Output: [(1, 2), (1, 3), (2, 3)]
```

🧮 Summary Table:
Feature	combinations()	permutations()
Order matters?	❌ No	✅ Yes
Repeats allowed?	❌ No (unless duplicates in input)	❌ No (unless duplicates in input)
Example input	[1, 2, 3]	[1, 2, 3]
Example output (r=2)	(1, 2), (1, 3), (2, 3)	(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)


<br><br>

## Example 1

```python
#Returns every combination of k subets, with the overlap
from itertools import combinations
def minimumDifference(nums: list[int], k: int) -> int:
    if k == 1:
        return 0
    else:
        t = 10000000
        combinations_of_k = list(combinations(nums, k))
        for n in combinations_of_k:
            x = max(n) - min(n)
            if x < t:
                t = x
    return t




```


<br><br>

## Example 2

```python

# Combinations Of string "GeEKS" OF SIZE 3.
 
 
from itertools import combinations
 
letters ="GeEKS"
 
# size of combination is set to 3
a = combinations(letters, 3) 
y = [' '.join(i) for i in a]
 
print(y)
#['G e E', 'G e K', 'G e S', 'G E K', 'G E S', 'G K S', 'e E K', 'e E S', 'e K S', 'E K S']



```


<br><br>

## Example 3

```python

import itertools as it
import numpy as np
def checkPowersOfThree(n: int) -> bool:
    t = 0
    for x in range(1000):
        if 3**x >= n:
            t = x
            break
    threes = np.array([3**x for x in range(t+1)])
    for x in range(1,len(threes)+1):
        t = list(it.combinations(threes,x))
        print(t)
        if any(n == sum(y) for y in t):
            return True
    return False
print(checkPowersOfThree(27))


```

<br><br>

## Example 4

```python

"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

"""

from itertools import combinations,permutations
def combine(n: int, k: int) -> list[list[int]]:

    numbers = list(range(1,n+1))

    print(list(combinations(numbers,k)))

print(combine(4,3))
#[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
```


