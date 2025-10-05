

#  The `zip()` Function in Python

The `zip()` function combines multiple iterables (lists, tuples, strings, etc.) into a **single iterator of tuples**. Each tuple contains elements from the input iterables at the same position.

---

## 🔹 Basic Usage

```python
names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]

res = zip(names, scores)
print(list(res))
# [('John', 85), ('Alice', 90), ('Bob', 78), ('Lucy', 92)]
````

---

## 🔹 Iterables of Different Lengths

If the input iterables have different lengths, `zip()` stops at the **shortest iterable**:

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [88, 94]

res = zip(names, scores)
print(list(res))
# [('Alice', 88), ('Bob', 94)]
```

---

## 🔹 Looping Through Multiple Iterables

You can loop through pairs (or triples) of elements using slicing:

### Two elements at a time

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for a, b in zip(my_list[::2], my_list[1::2]):
    print(a, b)
# Output:
# 1 2
# 3 4
# 5 6
# 7 8
```

### Three elements at a time

```python
for a, b, c in zip(my_list[::3], my_list[1::3], my_list[2::3]):
    print(a, b, c)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

---

## 🔹 Practical Example: Counting Height Mismatches

Problem: A school lines up students by height.

* `heights` → current order
* `expected` → sorted order
  Count how many students are **not standing in the expected position**.

```python
def height_mismatches(heights: list[int]) -> int:
    sorted_heights = sorted(heights)
    mismatches = 0
    for h, sh in zip(heights, sorted_heights):
        if h != sh:
            mismatches += 1
    return mismatches

# Example
print(height_mismatches([1,1,4,2,1,3]))
# Output: 3
```

**Explanation:**

* Current: `[1,1,4,2,1,3]`
* Sorted: `[1,1,1,2,3,4]`
* Indices 2, 4, 5 do not match → total 3 mismatches.

---

## 🔹 Key Points

| Feature              | Notes                                                             |
| -------------------- | ----------------------------------------------------------------- |
| Basic behavior       | Combines iterables into tuples                                    |
| Different lengths    | Stops at the shortest iterable                                    |
| Can be used in loops | Unpack tuples directly (`for a, b in zip(...)`)                   |
| Common applications  | Pairing elements, comparing sequences, batching elements in pairs |

---

 **Pro Tip:** You can also **unpack zipped iterables** using `*`:

```python
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters)  # ('a', 'b', 'c')
print(numbers)  # (1, 2, 3)
```

```

