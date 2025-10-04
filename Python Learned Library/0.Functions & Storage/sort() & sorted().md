

## 1. **`list.sort()` Method**

### **Definition**

`list.sort()` is a **method of list objects** that sorts the list **in place**.

### **Syntax**

```python
list.sort(key=None, reverse=False)
```

### **Parameters**

* **`key`**: A function that extracts a comparison key from each list element. Default is `None`.
* **`reverse`**: Boolean. If `True`, sorts in descending order. Default is `False`.

### **Behavior**

* **Modifies the original list**; does not create a new list.
* **Returns `None`**.
* Sorting is **stable**: elements that compare equal maintain their relative order.

### **Example**

```python
arr = [3, 1, 2]
arr.sort()
print(arr)  # [1, 2, 3]

# With key and reverse
arr = ["apple", "banana", "cherry"]
arr.sort(key=len, reverse=True)
print(arr)  # ['banana', 'cherry', 'apple']
```

---

<br><br><br><br><br><br><br><br><br><br><br>

## 2. **`sorted()` Function**

### **Definition**

`sorted()` is a **built-in function** that works on **any iterable** and returns a **new sorted list**.

### **Syntax**

```python
sorted(iterable, key=None, reverse=False)
```

### **Parameters**

* **`iterable`**: Any iterable object (list, tuple, string, dictionary keys, etc.)
* **`key`**: Function to extract comparison key (default `None`)
* **`reverse`**: Boolean to sort in descending order (default `False`)

### **Behavior**

* **Does not modify the original iterable**.
* Always returns a **new list**.
* Sorting is **stable**.

### **Example**

```python
t = (3, 1, 2)
new_list = sorted(t)
print(new_list)  # [1, 2, 3]
print(t)         # (3, 1, 2)  <-- tuple unchanged

# With key and reverse
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)  # ['banana', 'cherry', 'apple']
print(words)         # ['apple', 'banana', 'cherry']  <-- original list unchanged
```

---

## 3. **Comparison Table**

| Feature                | `list.sort()`                                 | `sorted()`                                                                                 |
| ---------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Modifies original?** | ✅ Yes                                         | ❌ No                                                                                       |
| **Returns**            | `None`                                        | New list                                                                                   |
| **Works on**           | Only lists                                    | Any iterable                                                                               |
| **Stable sort**        | ✅                                             | ✅                                                                                          |
| **Syntax**             | `list.sort(key=..., reverse=...)`             | `sorted(iterable, key=..., reverse=...)`                                                   |
| **Use case**           | When you want to sort in-place to save memory | When you want a new sorted list or need to sort other iterables (tuple, dict keys, string) |

---

### 4. **Memory Considerations**

* `list.sort()` is **more memory-efficient** because it sorts in place.
* `sorted()` creates a **new list**, so it uses extra memory proportional to the size of the iterable.

---

### 5. **Key Takeaways**

1. Use `list.sort()` if you **don’t need the original list** and want **better memory efficiency**.
2. Use `sorted()` if you need a **new sorted list**, or you’re sorting a **non-list iterable**.
3. Both support **custom sorting** via `key` and `reverse` and are **stable**.







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