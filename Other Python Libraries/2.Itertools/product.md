
```python
itertools.product() is like a nested for-loop generator.

from itertools import product

for p in product([0, 1], repeat=3):
    print(p)

(0, 0, 0)
(0, 0, 1)
(0, 1, 0)
(0, 1, 1)
(1, 0, 0)
(1, 0, 1)
(1, 1, 0)
(1, 1, 1)



for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            print((a, b, c))

```

So it's like:
	• All possible sequences of 0s and 1s of length 3.
	• With repeat=3, you're creating a 3-dimensional grid.


For "1234":


```python
for mask in product([0, 1], repeat=3):
    print(mask)

(0, 0, 0) → "1234"
(0, 0, 1) → "123", "4"
(0, 1, 0) → "12", "3", "4"
...
(1, 1, 1) → "1", "2", "3", "4"
```
