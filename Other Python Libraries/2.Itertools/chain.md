

Great question! itertools.chain() is used to combine multiple 
    iterables into a single sequence (like flattening).


```python
from itertools import chain
a = [1, 2]
b = [3, 4]

result = list(chain(a, b))
print(result)  # Output: [1, 2, 3, 4]
```

