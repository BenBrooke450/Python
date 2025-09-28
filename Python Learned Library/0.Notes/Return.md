

# Python Functions & Practice Problems

---

## Return vs Print

* **`print`** → shows a result to the user, but does not store it.
* **`return`** → gives a result back to the program so it can be reused later.

```python
# Using print
def add_numbers(num1, num2):
    result = num1 + num2
    print("Sum:", result)

add_numbers(5, 4)   # Output: Sum: 9

# Using return
def add_numbers_2(num1, num2):
    result = num1 + num2
    return result

print(add_numbers_2(3, 3))  # Output: 6
```

Use `return` for reusable values.
Use `print` for display only.

---

## Checking Numbers

```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"  # Only reached if num == 0
```

```python
print(check_number(3))   # Positive
print(check_number(-2))  # Negative
print(check_number(0))   # Zero
```

---

## Product vs Sum

Return the **product** if ≤ 1000, else the **sum**.

```python
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

print(multiplication_or_sum(30, 30))  # 900
print(multiplication_or_sum(40, 40))  # 80
```

---

## Characters at Even Index

```python
def even_chars(text):
    for i in range(len(text)):
        if i % 2 == 0:
            print(text[i])

even_chars("Not Hello")

# OR using slicing (shorter)
def even_chars(text):
    return text[::2]

print(even_chars("Not Hello"))  # NtHlo
```

---

## Remove First N Characters

```python
def remove_chars(text, n):
    return text[n:]

print(remove_chars("HelloWorld", 5))  # World
```

⚠️ Don’t name variables `str` — it overwrites Python’s built-in string type.

---

## First & Last Number Same?

```python
def first_last(num_list):
    return num_list[0] == num_list[-1]

print(first_last([10, 20, 30, 40, 10]))  # True
print(first_last([75, 65, 35, 75, 30]))  # False
```

---

## Merge Odd & Even Numbers from Two Lists

```python
def merge_list(list1, list2):
    result = []
    for num in list1:
        if num % 2 != 0:   # odd numbers
            result.append(num)
    for num in list2:
        if num % 2 == 0:   # even numbers
            result.append(num)
    return result

print(merge_list([1, 2, 3, 4], [10, 11, 12]))  
# [1, 3, 10, 12]
```

---

## Old MacDonald Problem

Capitalize the **1st** and **4th** letters of a word.

```python
def old_macdonald(name):
    if len(name) > 3:
        return name[:1].upper() + name[1:3] + name[3].upper() + name[4:]
    return name.capitalize()

print(old_macdonald("macdonald"))  # MacDonald
```

---

## Paper Doll Problem

Return a string where **each character appears 3 times**.

```python
def paper_doll(text):
    result = ""
    for char in text:
        result += char * 3
    return result

print(paper_doll("Hello"))       # HHHeeellllllooo
print(paper_doll("Mississippi")) # MMMiiissssssiiippppppiii
```

---

# Extra Notes

* **Avoid reserved words** like `str`, `list`, `sum` as variable names.
* Use **list comprehensions** for shorter code:

  ```python
  [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
  ```
* Use **string slicing** whenever possible — it’s powerful and concise.
* Debugging tip: add `print()` inside loops to check step-by-step logic.

