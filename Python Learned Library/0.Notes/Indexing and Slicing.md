
````markdown
# Understanding Indexing and Slicing in Python

In Python, indexing and slicing are vital concepts that allow you to access and manipulate sequences like strings, lists, and tuples efficiently.

---

## Indexing in Python

Indexing refers to accessing individual elements of a sequence. In Python, indexing starts at `0`, meaning the first element is at index `0`, the second at index `1`, and so on. To access an element, you use square brackets `[]` with the index number. For example:

```python
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[0]) # Outputs: 'apple'
print(my_list[1]) # Outputs: 'banana'
````

Negative indexing is also possible, where `-1` refers to the last element, `-2` to the second last, and so on:

```python
print(my_list[-1]) # Outputs: 'date'
print(my_list[-2]) # Outputs: 'cherry'
```

---

## Slicing in Python

Slicing allows you to access a range of elements within a sequence.
The syntax for slicing is:

```
sequence[start_index:end_index:step]
```

* `start_index` → inclusive (defaults to 0 if omitted)
* `end_index` → exclusive (defaults to length of sequence if omitted)
* `step` → how many items to skip (defaults to 1)

Examples:

```python
print(my_list[1:3])   # Outputs: ['banana', 'cherry']
print(my_list[:2])    # Outputs: ['apple', 'banana']
print(my_list[2:])    # Outputs: ['cherry', 'date']
print(my_list[::2])   # Outputs: ['apple', 'cherry']
print(my_list[::-1])  # Outputs: ['date', 'cherry', 'banana', 'apple']
```

---

## Practical Examples

### Extracting Substrings from a String

```python
sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[:3]

print(first_word) 
# Outputs: "The"
```

---

### Filtering a List

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = numbers[::2]

print(odd_numbers) 
# Outputs: [1, 3, 5, 7, 9]
```

---

### Extracting Columns from a 2D List

```python
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column = [row[1] for row in data]

print(column) 
# Outputs: [2, 5, 8]
```

---

### Modifying Parts of a List

```python
numbers[1:4] = [10, 20, 30]
print(numbers) 
# Outputs: [1, 10, 20, 30, 5, 6, 7, 8, 9]
```

---

## Palindrome Example

```python
"""Write a Python function that checks whether a word 
or phrase is palindrome or not."""

def pen(string):
    list1 = []
    list2 = list(string)
    print(list2)
    for let in string[::-1]:
        list1.append(let)
    if list1 == list2:
        print(True)
    else:
        print(False)

pen("helleh")
# ['h', 'e', 'l', 'l', 'e', 'h']
# True
```

```


