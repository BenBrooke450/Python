 


#  `try` / `except` in Python — Comprehensive Summary

## 1. **What is it?**

* A **control flow structure** that lets you handle **runtime errors (exceptions)** gracefully.
* Instead of your program crashing when something goes wrong, you can “catch” the error and decide what to do.

---

## 2. **Basic Syntax**

```python
try:
    # code that might raise an error
    risky_code()
except SomeError:
    # code that runs if that error happens
    handle_error()
```

---

## 3. **How it works**

* Python runs the `try` block **line by line**.
* If no error → `except` block is skipped.
* If an error happens:

  * Execution jumps immediately to the `except` block.
  * Remaining lines in `try` are skipped.

---

## 4. **Types of `except`**

### (a) Catch any error (not recommended in most cases):

```python
try:
    print(10 / 0)
except:
    print("Something went wrong")
```

### (b) Catch a specific error:

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### (c) Multiple exceptions:

```python
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion!")
except ZeroDivisionError:
    print("Zero division issue!")
```

### (d) Grouped exceptions:

```python
try:
    num = int("abc")
except (ValueError, TypeError):
    print("Bad input type or value")
```

---

## 5. **Optional Blocks**

Python allows more than just `try`/`except`:

* **`else`** → runs if no error occurs.
* **`finally`** → always runs (good for cleanup).

Example:

```python
try:
    num = int("42")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", num)
finally:
    print("Done!")
```

➡️ Output:

```
Conversion successful: 42
Done!
```

---

## 6. **Raising Errors Yourself**

You can deliberately raise exceptions:

```python
x = -1
if x < 0:
    raise ValueError("x must be non-negative")
```

---

## 7. **Why use `try` / `except`?**

* Prevents your program from crashing.
* Lets you handle different types of errors differently.
* Makes code more **robust and user-friendly**.

---

## 8. **Common Pitfalls**

❌ Catching all exceptions without handling properly:

```python
try:
    risky_code()
except:
    pass  # hides the problem — bad practice
```

❌ Too broad exception handling can make debugging impossible.
✅ Always prefer **specific exceptions** like `FileNotFoundError`, `ValueError`, etc.

---

## 9. **Real-World Examples**

### (a) File handling:

```python
try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
```

### (b) Network request:

```python
import requests

try:
    r = requests.get("https://example.com")
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Network error:", e)
```

---

✅ **In short**:

* `try` → code that might fail.
* `except` → handle the failure.
* `else` → if nothing failed.
* `finally` → always run (cleanup).

---

Do you want me to **compare `try/except` with `if/else` checks** (when to use one vs the other)?


<br><br><br><br><br>



# Examples

```python
####################################################################
###               Validating User Input
####################################################################

 

def user_choose():
    choice = "WRONG"
    while type(choice) != int:
        choice = input("Please enter a number between 0-10: ")
        try:
            return int(choice)
        except ValueError:
            print("Sorry that is not a digit")
    return choice
print(user_choose())

 

#Please enter a number between 0-10: five
#Sorry that is not a digit

#Please enter a number between 0-10: 6

6

 

####################################################################

 

 

 

while type(choice) != int:
    choice = input("Please enter a number between 0-10: ")
    try:
        a = int(choice)
        if type(a) == int and 0 < a < 10:
            return choice
        else:
            print("That is not within 0 to 10")
    except ValueError:
        print("Sorry that is not a digit")
return choice


print(user_choose())



#Please enter a number between 0-10: 11
That is not within 0 to 10

 

#Please enter a number between 0-10: five
Sorry that is not a digit

 

#Please enter a number between 0-10: 3
3

 

 

####################################################################



for index, nums in enumerate(prices):
    try:
        index_start = position_of_max + i

        max_num = max(prices[position_of_max + i:])
        position_of_max = prices.index(max_num,index_start)
        min_num = min(prices[position_of_min:position_of_max])
        position_of_min = prices.index(min_num,position_of_min)
        i = 1
        diff = max_num - min_num
        if diff > max_diff:
            max_diff = diff
    except ValueError as e:
        print(e)
        break
    else:
        pass
```
 

 