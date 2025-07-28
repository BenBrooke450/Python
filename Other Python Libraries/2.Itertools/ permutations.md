

🔹 itertools.permutations(iterable, r)
	• Generates r-length tuples of all possible orderings of elements from the iterable.
	• Order matters.
	• No repeated elements (by default, unless your iterable has duplicates).
Example:

```python
from itertools import permutations
list(permutations([1, 2, 3], 2))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

🔹 itertools.combinations(iterable, r)
	• Generates r-length tuples of all possible combinations without regard to order.
	• Order does not matter.
	• No repeated elements.

```python
from itertools import combinations
list(combinations([1, 2, 3], 2))
# Output: [(1, 2), (1, 3), (2, 3)]
```





```python
from itertools import permutations

s = "abc"

for p in permutations(s):
    print(''.join(p))


abc
acb
bac
bca
cab
cba




list2 = ["".join(x) for y in range(0,len(tiles)) for x in permutations(tiles[y:])]
print(numTilePossibilities("AAABBC"))
#['AAABBC', 'AAABCB', 'AAABBC', 'AAABCB', 'AAACBB', 'AAACBB', 'AABABC', 'AABACB', 'AABBAC', 'AABBCA', 'AABCAB', 'AABCBA', 'AABABC', 'AABACB', 'AABBAC', 'AABBCA', 'AABCAB', 'AABCBA', 'AACABB', 'AACABB', 'AACBAB', 'AACBBA'....
```
