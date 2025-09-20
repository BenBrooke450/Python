


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




<br><br><br><br>
---


Great question 🚀 — this goes to the **heart of backtracking**.

When you do something like:

```python
if (r,c) == end:
    solutions.append(path.copy())
```

the important part is the `.copy()`.

---

### Why?

* In **backtracking**, you usually maintain a single mutable list `path` that you **push** onto (append) and **pop** off as you explore.
* If you just do `solutions.append(path)`, then every entry in `solutions` would point to the **same underlying list object**.
* That means when you later backtrack (pop items), all the "solutions" would change too — you'd end up with multiple references to the same evolving list.

---

### ✅ Example

Without `.copy()`:

```python
path = [1, 2]
solutions = []
solutions.append(path)
path.append(3)   # mutates path
print(solutions)  # [[1, 2, 3]]   <-- changed!
```

With `.copy()`:

```python
path = [1, 2]
solutions = []
solutions.append(path.copy())
path.append(3)
print(solutions)  # [[1, 2]]   <-- frozen in time
```

---

### Rule of Thumb in Backtracking

* Use `.append(item)` and `.pop()` to explore.
* When you want to **save a snapshot** of your current path, use `.copy()` (or `list(path)`) to store an **independent version**.

---

In short: `.copy()` ensures that when you reach a solution, you lock in that exact state of the path — otherwise your stored solutions would all mutate as backtracking continues.

