





## Example 1
```python

def frequencySort(s: str) -> str:


    dict2 = {x: s.count(x) for x in s}

    items = dict2.items()

    # Sort the list of tuples based on the second element (the count)
    s = sorted(items, key=lambda x: x[1], reverse=True)

    s = "".join(x[0]*x[1]  for x in s)

    return s

print(frequencySort("tree"))
#eetr

print(frequencySort("trrreerrrroooooiifg"))
#rrrrrrroooooeeiitfg

```

<br><br>

## Example 2
```python

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']

sorted_ids = sorted(ids, key=lambda x: int(x[2:]))

print(sorted_ids) 
# Output: ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

```

<br><br>

## Example 3
```python
a = [[1, 3], [2, 1], [4, 2], [3, 5]]
# Sorts by the second element
a = sorted(a, key=lambda x: x[1])  
print(a)
```