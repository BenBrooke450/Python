

# 1. The `open()` Function

`open()` is the built-in function used to create a **file object** so you can read from or write to a file.

Basic syntax:

```python
file = open("filename.txt", mode)
```

`mode` determines what you want to do with the file.

### Most common modes:

| Mode   | Meaning         | Behavior                         |
| ------ | --------------- | -------------------------------- |
| `'r'`  | Read text       | File must exist or error         |
| `'w'`  | Write text      | Overwrites file or creates new   |
| `'a'`  | Append text     | Adds to end of file              |
| `'r+'` | Read and write  | File must exist                  |
| `'w+'` | Write and read  | Overwrites or creates new        |
| `'a+'` | Append and read | Reads existing and writes at end |
| `'rb'` | Read binary     | For images, videos, etc.         |
| `'wb'` | Write binary    | Binary output                    |
| `'ab'` | Append binary   | Append binary data               |

---

# If you leave "r" blank it will auto defult to r

# 2. Using `open()` without `with`

```python
file = open("example.txt", "r")
data = file.read()
file.close()
```

But this is unsafe because:

* If the program crashes before `close()`, the file stays open.
* Open files can cause memory leaks or locking issues.

This is why we use `with`.

---

# 3. The `with` Statement (Context Manager)

`with` guarantees the file is closed automatically, even if errors occur.

```python
with open("example.txt", "r") as f:
    text = f.read()

# here the file is automatically closed
```

**Why use `with`?**

* It is safer.
* It is cleaner.
* It automatically handles file closing.

Essentially:

* `open()` creates a file object.
* `with` ensures cleanup using the context manager protocol.

---

# 4. File Reading Methods

Python’s file object provides many reading options.

---

## 4.1 `read()`

Reads **entire file** as a single string.

```python
with open("example.txt", "r") as f:
    data = f.read()

print(data)
```

Optional argument: `read(n)` reads only **n characters**.

---

## 4.2 `readline()`

Reads **one line at a time**.

```python
with open("example.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
```

Useful for memory-efficient line-by-line processing.

---

## 4.3 `readlines()`

Reads **all lines into a list**.

```python
with open("example.txt", "r") as f:
    lines = f.readlines()

print(lines)   # ['line1\n', 'line2\n', ...]
```

Better for small files, not recommended for very large ones.

---

## 4.4 Iterating through file lines (most memory-efficient)

```python
with open("example.txt", "r") as f:
    for line in f:
        print(line)
```

The file object is an iterator.

---

# 5. File Writing Methods

---

## 5.1 `write()`

Writes a string to the file.

```python
with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World")
```

Remember: `'w'` overwrites the entire file.

---

## 5.2 `writelines()`

Writes a list of strings.

```python
lines = ["line1\n", "line2\n"]

with open("output.txt", "w") as f:
    f.writelines(lines)
```

You must include newline characters manually.

---

# 6. Positioning Functions: `seek()` and `tell()`

These allow you to manipulate file pointer position.

---

## `tell()`

Returns the current position in the file.

```python
with open("example.txt", "r") as f:
    print(f.tell())   # usually 0
    f.read(5)
    print(f.tell())   # now at position 5
```

---

## `seek(offset, from_what)`

Moves the pointer.

* `offset` = number of bytes to move
* `from_what`:

  * `0` = beginning (default)
  * `1` = current position
  * `2` = end of file

Example: reset to start:

```python
with open("example.txt", "r") as f:
    f.read()
    f.seek(0)
    print(f.read())   # reads again
```

---

# 7. Binary Files

Binary mode is required for:

* images
* pdf files
* zip files
* audio
* video

Example reading an image:

```python
with open("image.png", "rb") as f:
    data = f.read()
```

Writing binary:

```python
with open("copy.png", "wb") as f:
    f.write(data)
```

---

# 8. Checking File Existence

Using `os.path`:

```python
import os

if os.path.exists("example.txt"):
    print("File exists")
```

---

# 9. Summary Table

| Operation       | Description        | Example                 |
| --------------- | ------------------ | ----------------------- |
| Open file       | Create file object | `open("file.txt", "r")` |
| Read whole file | Load entire text   | `f.read()`              |
| Read line       | One line           | `f.readline()`          |
| Read all lines  | List of lines      | `f.readlines()`         |
| Write           | Overwrite text     | `f.write("text")`       |
| Append          | Add to end         | `open(..., "a")`        |
| Iterate lines   | Efficient reading  | `for line in f:`        |
| Seek            | Move pointer       | `f.seek(0)`             |
| Tell            | Get pointer        | `f.tell()`              |
| Binary mode     | Non-text           | `open("file", "rb")`    |
| `with`          | Auto-close         | `with open(...)`        |

---

# 10. Complete Example Combining Everything

```python
# Writing a file
with open("data.txt", "w") as f:
    f.write("line1\n")
    f.write("line2\n")

# Reading
with open("data.txt", "r") as f:
    print("Position:", f.tell())
    print(f.read(5))     # partial read
    print("Position:", f.tell())

    f.seek(0)            # reset
    print(f.readline())  # line1
    print(f.readline())  # line2

# Appending
with open("data.txt", "a") as f:
    f.write("line3\n")

# Reading all lines
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

