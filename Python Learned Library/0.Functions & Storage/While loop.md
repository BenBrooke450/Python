
````markdown
# Python While Loops

**Key Idea**:  
While loops are **boolean-driven** — they run only while the condition evaluates to `True`.  

---

### Example: Getting Player Position

```python
def player_position():
    choice = "PLACE HOLDER"

    while choice not in ["0","1","2","3","4","5","6","7","8"]:
        choice = input("Pick your number for position 0-8: ")

        if choice not in ["0","1","2","3","4","5","6","7","8"]:
            print("You must pick a number between 0 and 8: ")

    return int(choice)
````

Alternate version (using integers directly):

```python
def player_position():
    choice = "PLACE HOLDER"

    while choice not in [0,1,2,3,4,5,6,7,8]:
        choice = input("Pick your number for position 0-8: ")

        if choice not in ["0","1","2","3","4","5","6","7","8"]:
            print("You must pick a number between 0 and 8: ")

    return int(choice)
```

---

# Level 2 Problems

### Find 33

> Given a list of integers, return True if the array contains a `3` next to a `3` somewhere.

```python
def has_33(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        i = i + 1
        if nums[i-1] == nums[i]:
            print("True Has33")
            break

# Tests
has_33([1, 3, 3])          # True
has_33([1,3,2,3,4,5,3,3])  # True
has_33([1,3,1])            # False
```

---

### Ask for an Integer (with try/except)

```python
def ask():
    while True:
        try:
            v = int(input("Please give a number"))
            print(v**2)
        except:
            print("please input a number")
            continue
        else:
            print("Yea that´s an integer")
            break

ask()
```

**Example Run**:

```
Please give a number f
please input a number
Please give a number 4
16
Yea that´s an integer
```

---

### Look Ahead in a String (checking mismatched brackets)

```python
i = 0
while i < (len(text) - 1):
    if text[i] == "[" and (text[i + 1] == "}" or text[i + 1] == ")"):
        return False
    elif text[i] == "(" and (text[i + 1] == "}" or text[i + 1] == "]"):
        return False
    elif text[i] == "{" and (text[i + 1] == "]" or text[i + 1] == ")"):
        return False
    i = i + 1
```

---

### Replace Values with 0 Until Larger Found

```python
j = 0
while j < len(prices):
    if prices[j] > prices[j + 1]:
        prices[j] = 0
        j = j + 1
    else:
        prices
```

**Example**:

```python
print(max_num([7,4,1,2]))
# [0, 0, 1, 2]
```

---

### Single Number (Every Element Appears Twice Except One)

> Given a non-empty array of integers, every element appears twice except for one.
> Find that single one.
> Must be O(n) time with O(1) space.

```python
def only_one(list_number: list[int]):
    sort_list = sorted(list_number)
    j = 0

    while j < len(sort_list):
        try:
            if sort_list[j] == sort_list[j + 1]:
                j = j + 2
            else:
                return sort_list[j]
        except IndexError:
            return sort_list[j]

# Example
print(only_one([1,1,2,2]))  # None (because no single element)
print(only_one([4,1,2,1,2])) # 4
print(only_one([1]))         # 1
```



