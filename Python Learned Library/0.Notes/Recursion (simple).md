# Example 2

```python
"""

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]




Example 2:


Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30

"""


def generate(numRows: int) -> list[list[int]]:

    list1 = []

    def pas(first,incre,numRows):

        list1.append(first[:])
        first.append(incre)
        first = [1] + [sum(first[x:x+2]) for x in range(len(first)-1)]
        if len(list1) >= numRows:
            return list1
        else:
            pas(first,incre,numRows)

    pas(first = [1],incre = 0,numRows = numRows)

    return list1


print(generate(5))
#[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

```






<br><br><br><br><br><br><br>

## 1️⃣ Case A — Mutable containers (list, set, dict)

```python
def outer():
    results = []   # defined outside inner()

    def inner(x):
        results.append(x)   # modifies in-place, no reassignment
        return results

    inner(1)
    inner(2)
    return results

print(outer())  # [1, 2]
```

Works fine because:

* `results` is a **mutable object**.
* Inside `inner`, you call methods like `.append()` → this mutates the same object in memory.
* Python doesn’t treat it as a new variable, so no conflict.

---

## 2️⃣ Case B — Simple variables (int, str, float, tuple)

```python
def outer():
    count = 0   # integer is immutable

    def inner():
        count += 1  # ❌ ERROR: UnboundLocalError
        return count

    return inner()

print(outer())
```

❌ Fails with:

```
UnboundLocalError: local variable 'count' referenced before assignment
```

Why?

* When you **assign** to a variable inside a function (`count += 1`), Python assumes you’re creating a **new local variable**, not modifying the outer one.
* Since `count` isn’t defined *inside* `inner()` before use, Python complains.

---

## 3️⃣ The Fix — `nonlocal` or `global`

If you want to reassign outer variables inside an inner function:

```python
def outer():
    count = 0

    def inner():
        nonlocal count   # tell Python: use outer scope variable
        count += 1
        return count

    inner()
    inner()
    return count

print(outer())  # 2
```

Or if the variable is global:

```python
count = 0

def increment():
    global count
    count += 1
    return count

print(increment())  # 1
print(increment())  # 2
```

---

## 4️⃣ Why the difference?

* **Mutable objects** (list, set, dict): You’re not reassigning the name, you’re mutating the object itself → so Python doesn’t create a new local variable.
* **Immutable objects** (int, str, float, tuple): You can’t mutate them. Any “change” is actually a reassignment → Python treats it as a new local variable unless told otherwise (`nonlocal`/`global`).

---

✅ **Rule of Thumb:**

* If you only call methods like `.append()` or `.add()`, you’re mutating → safe to define outside.
* If you need to **reassign** (e.g. `count = count + 1`), you must declare it `nonlocal` (in closures) or `global` (for module-level).

---

Would you like me to show how this specifically plays out in a **recursive DFS/backtracking example** (like `path.append()` vs `count += 1`)? That’s where this distinction becomes really clear.

