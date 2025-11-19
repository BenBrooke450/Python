Python comes with a large set of **built-in classes** — these are classes that are part of the language itself and are available **without importing anything**.

Below is a **complete, structured list** of the most important built-in classes in Python, grouped by category, with explanations.

---

# **1. Core Built-in Data Type Classes**

These are the most commonly used built-in classes:

### **Numbers**

| Class     | Description            | Example             |
| --------- | ---------------------- | ------------------- |
| `int`     | Integer numbers        | `x = int(5)`        |
| `float`   | Floating point numbers | `x = float(1.23)`   |
| `complex` | Complex numbers        | `x = complex(2, 3)` |

---

### **Text**

| Class | Description    |
| ----- | -------------- |
| `str` | Strings (text) |

Example:

```python
s = str("hello")
```

---

### **Sequence Containers**

| Class   | Description         |             |
| ------- | ------------------- | ----------- |
| `list`  | Mutable sequence    | `[]`        |
| `tuple` | Immutable sequence  | `()`        |
| `range` | Sequence of numbers | `range(10)` |

---

### **Mapping**

| Class  | Description            |      |
| ------ | ---------------------- | ---- |
| `dict` | Stores key-value pairs | `{}` |

---

### **Set Types**

| Class       | Description   |           |
| ----------- | ------------- | --------- |
| `set`       | Mutable set   | `{1,2,3}` |
| `frozenset` | Immutable set |           |

---

# **2. Built-in Classes Used Internally by Python**

### **Boolean**

* `bool` → subclass of int (`True`, `False`)

### **Binary Data**

| Class        | Description           |
| ------------ | --------------------- |
| `bytes`      | Immutable byte array  |
| `bytearray`  | Mutable byte array    |
| `memoryview` | View into binary data |

---

# **3. Built-in IO and File Classes**

### **file class**

Represented by the type returned by `open()`:

```python
f = open("file.txt")
type(f)  # <class '_io.TextIOWrapper'>
```

---

# **4. Built-in Utility Classes**

### **iterators and generators**

| Class       | Description                        |
| ----------- | ---------------------------------- |
| `iterator`  | Generated when you call iter()     |
| `generator` | Created by functions using `yield` |

---

### **functions and methods**

| Class                        | Description            |
| ---------------------------- | ---------------------- |
| `function`                   | User-defined functions |
| `builtin_function_or_method` | e.g., `len`, `sum`     |

---

# **5. Abstract Base Classes (from `collections.abc`)**

Available after importing:

```python
from collections.abc import Iterable, Mapping, Sequence
```

Common abstract classes:

| Class       | Meaning                        |
| ----------- | ------------------------------ |
| `Iterable`  | Something you can iterate over |
| `Iterator`  | Something that produces items  |
| `Sequence`  | List-like                      |
| `Mapping`   | Dict-like                      |
| `Container` | Supports `in`                  |
| `Sized`     | Has `__len__`                  |
| `Callable`  | Has `__call__`                 |

These define **interfaces** (abstract methods), not concrete behavior.

---

# **6. Special Purpose Built-in Classes**

| Class       | Purpose                          |
| ----------- | -------------------------------- |
| `type`      | Meta-class of all classes        |
| `object`    | Base class of all Python classes |
| `Exception` | Base class for all exceptions    |
| `slice`     | Used for indexing (`x[1:5]`)     |
| `ellipsis`  | The `...` object                 |

---

# A More Complete Table of Built-in Classes

| Class                                    | Category           |
| ---------------------------------------- | ------------------ |
| `int`                                    | numbers            |
| `float`                                  | numbers            |
| `complex`                                | numbers            |
| `str`                                    | text               |
| `list`                                   | sequences          |
| `tuple`                                  | sequences          |
| `range`                                  | sequences          |
| `dict`                                   | mapping            |
| `set`                                    | sets               |
| `frozenset`                              | sets               |
| `bool`                                   | logical values     |
| `bytes`                                  | binary             |
| `bytearray`                              | binary             |
| `memoryview`                             | binary             |
| `object`                                 | base class         |
| `type`                                   | metaclass          |
| `slice`                                  | helper class       |
| `staticmethod`                           | decorator utility  |
| `classmethod`                            | decorator utility  |
| `property`                               | descriptor utility |
| `Exception` and subclasses               | error-handling     |
| `BaseException`                          | root of exceptions |
| `file` / `_io.TextIOWrapper`             | file objects       |
| `dict_keys`, `dict_values`, `dict_items` | view classes       |

---

# Final Summary

### **Yes — Python has many built-in classes.**

The most important and commonly used ones are:

* `int`
* `float`
* `str`
* `list`
* `tuple`
* `dict`
* `set`
* `object`
* `Exception`
* `type`

