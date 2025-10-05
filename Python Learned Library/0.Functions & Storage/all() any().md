

# Using `all()` and `any()` in Python

Python provides two powerful built-in functions, **`all()`** and **`any()`**, for evaluating iterables (like lists, tuples, sets, generators).

---

## `all()` Function

The **`all()`** function returns `True` if **all elements** of an iterable are `True` (or the iterable is empty).  

### Syntax
```python
all(iterable)
````

* Returns `True` if every element is truthy.
* Returns `False` if at least one element is falsy.

---

### Examples

#### Example 1: All True

```python
nums = [1, 2, 3, 4]
print(all(nums))  
# Output: True (all are nonzero, hence truthy)
```

#### Example 2: At Least One False

```python
nums = [1, 0, 3]
print(all(nums))  
# Output: False (0 is falsy)
```

#### Example 3: Empty Iterable

```python
print(all([]))  
# Output: True (vacuous truth: nothing is False)
```

---

## `any()` Function

The **`any()`** function returns `True` if **at least one element** of an iterable is `True`.

### Syntax

```python
any(iterable)
```

* Returns `True` if at least one element is truthy.
* Returns `False` if all elements are falsy or the iterable is empty.

---

### Examples

#### Example 1: Some True

```python
nums = [0, 0, 3, 0]
print(any(nums))  
# Output: True (3 is truthy)
```

#### Example 2: All False

```python
nums = [0, False, None, ""]
print(any(nums))  
# Output: False (no truthy elements)
```

#### Example 3: Empty Iterable

```python
print(any([]))  
# Output: False
```

---

## Real-World Use Cases

### Example 1: Checking Password Conditions

```python
password = "HelloWorld123!"

conditions = [
    any(ch.isupper() for ch in password),  # has uppercase
    any(ch.islower() for ch in password),  # has lowercase
    any(ch.isdigit() for ch in password),  # has digit
    any(ch in "!@#$%^&*()-+" for ch in password)  # has special char
]

print(all(conditions))
# Output: True (all conditions satisfied)
```

### Example 2: Validating Input

```python
responses = ["yes", "ok", "sure"]

print(any(r.lower() == "yes" for r in responses))  
# Output: True (at least one "yes")
```

---

## Quick Summary

| Function | Returns `True` if…                          | Example                                        |
| -------- | ------------------------------------------- | ---------------------------------------------- |
| `all()`  | All elements are truthy (or iterable empty) | `all([1, 2, 3]) → True` <br> `all([]) → True`  |
| `any()`  | At least one element is truthy              | `any([0, 0, 3]) → True` <br> `any([]) → False` |

---

 **Pro Tips**:

* Use `all()` when **everything must be true**.
* Use `any()` when **at least one must be true**.
* Works great with **generator expressions** for memory-efficient checks.




