

## **1. What is Extra Space?**

* **Extra space** is **any additional memory** your algorithm uses **beyond the input**.
* Input: `nums` (or whatever data you are given) → does **not** count.
* Anything you create yourself that grows with input size → **extra space**.

---

## **2. Constant Extra Space (O(1))**

* Space used does **not depend on input size**.
* Examples of allowed variables:

```python
n = len(nums)        # integer
slow = 0             # pointer
fast = 0             # pointer
duplicate = 0        # integer
```

* **Why allowed?** These are fixed-size, no matter how big `nums` is.

✅ Examples that **use constant space**:

```python
# Find maximum element
max_val = nums[0]
for x in nums:
    if x > max_val:
        max_val = x
print(max_val)
```

* Only `max_val` is used → O(1) space.

```python
# Tortoise and Hare for finding duplicate
slow = nums[0]
fast = nums[0]
# moves pointers → still O(1) space
```

---

## **3. Extra Space That Grows With Input (O(n))**

* **Any data structure that can grow with input size** counts as extra space.
* Examples:

```python
abc = []             # list can grow up to size n
seen = set()         # set can grow up to size n
count = {}           # dictionary can grow with n
res = [x*2 for x in nums]  # new list of size n
```

* These **violate constant space constraint** in problems like LeetCode 287.

---

### **4. Examples in Context**

| Task                                        | Constant Space? | Why/Why Not                   |
| ------------------------------------------- | --------------- | ----------------------------- |
| Finding max in a list                       | ✅ O(1)          | Only one variable for max     |
| Using `nums.index(x)`                       | ✅ O(1)          | No new list or set is created |
| Using a set to detect duplicates            | ❌ O(n)          | Set grows with input          |
| Creating a new list with list comprehension | ❌ O(n)          | New list grows with input     |
| Using pointers (slow/fast)                  | ✅ O(1)          | Only a few variables          |
| Slicing array (`nums[::-1]`)                | ❌ O(n)          | Creates a new list of size n  |

---

### **5. Key Rule of Thumb**

* **Allowed:** A fixed number of variables (int, float, pointer).
* **Not allowed:** Any structure (list, set, dict, new array) that **scales with input size**.

---

If you want, I can make a **super short cheat-sheet table of “allowed vs not allowed extra space tricks”** for LeetCode 287 and similar problems — it’s very handy when solving them.

Do you want me to do that?




<br><br><br><br><br><br><br>


# **Modifying the Array**

### **Definition**

Modifying means **changing the contents of `nums`** so it isn’t the same afterward.
If the problem says *“do not modify nums”*, you must leave the array unchanged.

---

### Modifies the array

```python
nums = [3, 1, 3, 4, 2]
nums.sort()
print(nums)  # [1, 2, 3, 3, 4]
```

* Sorting rearranges elements permanently.
* The array is changed.

---

### Modifies the array

```python
nums = [3, 1, 3, 4, 2]
nums[0] = -1
print(nums)  # [-1, 1, 3, 4, 2]
```

* Overwrites values in `nums`.

---

### Does not modify

```python
nums = [3, 1, 3, 4, 2]
for num in nums:
    print(num)
```

* Only *reads* from `nums`.
* Original array is untouched.

---

### Sorting a copy (technically not modifying `nums`, but not constant space)

```python
nums = [3, 1, 3, 4, 2]
sorted_nums = sorted(nums)   # makes a new list
print(nums)        # [3, 1, 3, 4, 2] (unchanged)
print(sorted_nums) # [1, 2, 3, 3, 4]
```

* `nums` is not changed.
* But `sorted(nums)` creates a new array → **extra space O(n)**.

---

---

# **Summary**

* **Constant extra space** = only a fixed number of variables. No lists, sets, dicts, slices, or new arrays.
* **Modifying array** = sorting in place, swapping, overwriting, or altering `nums`.

 The “Find the Duplicate Number” problem is tricky because:

* Using `set` or sorting a copy = not constant space.
* Sorting in place = modifies array.
* So you need a clever trick like **XOR** or **Floyd’s cycle detection** to meet the strict rules.

