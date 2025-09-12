
`ord()` is a built-in Python function that converts a **character** into its **Unicode code point** (basically an integer representation).

---

### Example

```python
print(ord('a'))   # 97
print(ord('b'))   # 98
print(ord('z'))   # 122
print(ord('A'))   # 65
```

So:

* `'a'` → `97`
* `'b'` → `98`
* `'z'` → `122`

---

### Why is this useful?

If you want to map letters to numbers starting at `0`, you can do:

```python
ord('a') - ord('a')  # 0
ord('b') - ord('a')  # 1
ord('c') - ord('a')  # 2
```

This way `'a' → 0`, `'b' → 1`, ..., `'z' → 25` without needing a whole alphabet dictionary.

---

In your code, instead of building this:

```python
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
dic_alphabet = {x: i for i,x in enumerate(alphabet)}
```

you can just do:

```python
value = ord(c) - ord('a')
```

Much shorter and faster! 

