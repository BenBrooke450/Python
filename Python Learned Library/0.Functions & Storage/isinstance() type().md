

# Checking Types in Python with `type()` and `isinstance()`

When working with Python, you often need to check the type of variables or elements inside a list. There are two common tools for this: **`type()`** and **`isinstance()`**.

---

## Example 1: Using `type()`

```python
# Sample list with different types of elements
elements = [123, 'hello', 45.67, True, None, {'key': 'value'}, [1, 2, 3]]

# Loop through each element and check its type
for element in elements:
    element_type = type(element)
    print(f'The element "{element}" is of type {element_type}')
````

**Output:**

```
The element "123" is of type <class 'int'>
The element "hello" is of type <class 'str'>
The element "45.67" is of type <class 'float'>
The element "True" is of type <class 'bool'>
The element "None" is of type <class 'NoneType'>
The element "{'key': 'value'}" is of type <class 'dict'>
The element "[1, 2, 3]" is of type <class 'list'>
```

The `type()` function returns the exact type of the object.

---

## Example 2: Using `isinstance()`

If you need to **branch your logic depending on the type**, `isinstance()` is usually more flexible:

```python
for element in elements:
    if isinstance(element, int):
        print(f'The element "{element}" is an integer.')
    elif isinstance(element, str):
        print(f'The element "{element}" is a string.')
    elif isinstance(element, float):
        print(f'The element "{element}" is a float.')
    elif isinstance(element, bool):
        print(f'The element "{element}" is a boolean.')
    elif isinstance(element, dict):
        print(f'The element "{element}" is a dictionary.')
    elif isinstance(element, list):
        print(f'The element "{element}" is a list.')
    else:
        print(f'The element "{element}" is of an unknown type.')
```

### Why `isinstance()` is better than `type()`

* `isinstance(obj, Class)` also returns `True` if `obj` is an instance of a **subclass** of `Class`.
* `type(obj) == Class` only matches **exact types**.

**Example:**

```python
# bool is a subclass of int in Python
print(type(True) == int)        # False
print(isinstance(True, int))    # True
```

---

## Example 3: `isinstance()` in Practice

Checking password strength:

```python
def strongPasswordCheckerII(password: str) -> bool:
    if len(password) < 9:
        return False
    elif not any(x.isupper() for x in password):
        return False
    elif not any(x.islower() for x in password):
        return False
    # Note: password chars are strings, so isinstance(x, int) won't work here
    # but isinstance() is perfect for checking types like lists or dicts
    elif not any(x in "!@#$%^&*()-+" for x in password):
        return False
    else:
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
    return True
```

---

## Example 4: Custom Type Checking with `isinstance()`

```python
class LinkedList:
    pass

class Node:
    pass

def double(self, input_list):
    if not isinstance(input_list, LinkedList):
        raise TypeError("Input must be a LinkedList")
    # otherwise perform operation
```

---

## Quick Summary

* **`type(obj)`** → returns the exact type. Use it when you only care about *that* type.
* **`isinstance(obj, Class)`** → checks type *and subclasses*. Use it when you want flexible type checking.
* `isinstance()` is preferred in most real-world code because it plays nicely with **inheritance and polymorphism**.

```

