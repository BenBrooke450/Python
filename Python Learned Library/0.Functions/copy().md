


Python lists are mutable — if we just did list1.append(path_so_far), every item in list1 would point to the same list, which keeps getting changed in recursion.

So we use .copy() to freeze the current state of the path before it changes in the next recursion step.

```python
a = [1, 2]
b = a         # b is not a new list; it's a reference to a
b.append(3)
print(a)      # Output: [1, 2, 3]  ← changed!

a = [1, 2]
b = a.copy()  # b is now a separate copy
b.append(3)
print(a)      # Output: [1, 2]    ← not changed!
```


