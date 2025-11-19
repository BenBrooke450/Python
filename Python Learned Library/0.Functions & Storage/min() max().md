


# Using `min()` and `max()` in Python

The built-in functions **`min()`** and **`max()`** are used to find the smallest and largest values in an iterable or among arguments. They also support a `key` parameter, which allows for custom comparison logic.

---

## `min()` Function

The `min()` function returns the smallest value from an iterable or given arguments.

### Example 1: Smallest Number
```python
print(min(5, 2, 9, -1, 7))
# Output: -1
````

### Example 2: Smallest String by Lexicographical Order

```python
strings = ["apple", "banana", "cherry", "date"]
print(min(strings))
# Output: "apple" (alphabetically smallest)
```

### Example 3: Smallest String by Length

```python
strings = ["apple", "banana", "cherry", "date"]
smallest_string = min(strings, key=len)
print("The smallest string is:", smallest_string)
# Output: "date"
```

---

## `max()` Function

The `max()` function returns the largest value from an iterable or given arguments.

### Example 1: Largest Number

```python
print(max(-10, 5, -3, 2))
# Output: 5
```

### Example 2: Largest Value by Absolute Value

```python
numbers = [-10, 5, -3, 2]
print(max(numbers, key=abs))
# Output: -10 (largest absolute value)
```

### Example 3: Using a Lambda with `key`

```python
words = ["apple", "banana", "cherry", "date"]
longest_word = max(words, key=lambda x: len(x))
print(longest_word)
# Output: "banana"
```

---

## Example: Finding the Majority Element

Problem: Given an array `nums`, return the majority element (the element that appears more than ⌊n/2⌋ times).

```python
def highest(list1: list[int]):
    dic1 = {}
    for index, num in enumerate(list1):
        if num not in dic1:
            dic1[num] = 1
        else:
            dic1[num] = dic1.get(num) + 1
    return max(dic1, key=dic1.get)

nums = [2, 2, 1, 1, 1, 1, 1, 2, 2]
print(highest(nums))
# Output: 1
```

Here:

* `dic1` counts occurrences of each number.
* `max(dic1, key=dic1.get)` finds the key with the highest frequency.

---

## Example: Using `max()` with a Pandas Series

You can use `max()` on a Pandas DataFrame column to get the most frequent value:

```python
print(max(set(df["Sales"]), key=list(df["Sales"]).count))
```

* `set(df["Sales"])` → gets unique values.
* `list(df["Sales"]).count` → counts occurrences.
* `max(..., key=...)` → finds the value with the maximum count.

---

## Quick Summary

* **`min(iterable)`** → returns the smallest element.
* **`max(iterable)`** → returns the largest element.
* Both support `key=`, allowing custom comparison logic (e.g., `len`, `abs`, lambda functions).
* Great for tasks like **finding longest/shortest strings, largest by absolute value, or most frequent values**.






<br><br><br><br>


## WRONG

```python
remainders = {abs(sum(x)-target):sum(x) for x in combinations(nums,3)}

min_remainders = min(remainders, key=remainders.keys())
```

## CORRECT

```python
min_remainder_key = min(remainders.keys())

closest_sum = remainders[min_remainder_key]
```