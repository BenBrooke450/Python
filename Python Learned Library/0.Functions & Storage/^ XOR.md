
## 1. What is `^=` in Python?

* `^` is the **bitwise XOR operator** (exclusive OR).
* `^=` is the **in-place XOR assignment operator**.
* It updates the variable on the left-hand side with the result of XORing it with the right-hand side.

So:

```python
a ^= b
```

is exactly the same as:

```python
a = a ^ b
```

---

## 2. Reminder: XOR (`^`) rules

* **0 ^ 0 = 0**
* **0 ^ 1 = 1**
* **1 ^ 0 = 1**
* **1 ^ 1 = 0**

In short: **XOR is 1 if the bits differ, 0 if they’re the same.**

---

## 3. Properties of XOR useful with `^=`

* `x ^ 0 = x` (XOR with 0 does nothing)
* `x ^ x = 0` (XOR cancels itself out)
* Order doesn’t matter: `a ^ b = b ^ a`

---

## 4. Examples with `^=`

### Example 1: Basic use

```python
x = 5   # (binary 0101)
y = 3   # (binary 0011)

x ^= y  # same as x = x ^ y
print(x)  # 6

"""
 - XOR highlights the bits where numbers differ.

 - 5 (101) and 3 (011) differ in the first two bits, so the result has those bits set (110 = 6).

 - 5(1##) 3(0##)  = (1..) >  5(#0#) 3(#1#) = (11.) > 5(##1) 3(##1) = 6(110)

"""

```

**Explanation in binary:**

```
0101 (5)
0011 (3)
----
0110 (6)


* `x ^ 0 = x` (XOR with 0 does nothing)
* `x ^ x = 0` (XOR cancels itself out)
* Order doesn’t matter: `a ^ b = b ^ a`


 - 5(101) and 3(011) differ in the first two bits, so the result has those bits set (110 = 6).

 - 5(1##) 3(0##)  = (1..) >  5(#0#) 3(#1#) = (11.) > 5(##1) 3(##1) = 6(110)

```

---

### Example 2: Looping through an array

```python
nums = [3, 0, 1]
xor_all = 0

for num in nums:
    xor_all = xor_all ^ num # or xor_all ^= num

print(xor_all)  # 2
```

Step-by-step expansion:

* Start: `xor_all = 0`
* Iteration 1: `xor_all = 0 ^ 3 = 3`
* Iteration 2: `xor_all = 3 ^ 0 = 3`
* Iteration 3: `xor_all = 3 ^ 1 = 2`

Final result = **2**.

---

### Example 3: Cancelling duplicates

```python
nums = [4, 7, 4]
xor_all = 0

for num in nums:
    xor_all = xor_all ^ num # or xor_all ^= num

print(xor_all)  # 7
```

Why?

* 0 ^ 4 = 4
* 4 ^ 7 = 3 (binary: 100 ^ 111 = 011)
* 3 ^ 4 = 7 (binary: 011 ^ 100 = 111)

So the two `4`s cancel, leaving `7`.

---

## 5. When to use `^=`

* When you want to **accumulate XOR results** in a loop.
* When solving problems like:

  * Find the **single unique number** when others are duplicates.
  * Find a **missing number** in a range.
  * Swap two variables without using extra space (classic trick with XOR).

---

 **Summary in one line:**
`x ^= y` means `x = x ^ y` → it updates `x` to be the XOR of itself and `y`.







<br><br><br><br><br><br>


# Example

```python
def find_duplicate(nums):
    n = len(nums) - 1  # one duplicate
    xor_all = 0
    
    # XOR all elements in nums
    for num in nums:
        xor_all ^= num
    
    # XOR with numbers 1..n
    for i in range(1, n+1):
        xor_all ^= i
    
    return xor_all
```

---

## Line-by-line explanation

1. `def find_duplicate(nums):`
   Defines a function named `find_duplicate` that accepts one parameter `nums` (a list of integers).

2. `n = len(nums) - 1  # one duplicate`
   Assumption: `nums` contains integers from `1` to `n` but one value in that range appears **twice**, so the list length is `n + 1`.
   Example: if `nums` has 5 elements, `n = 4` (we expect numbers `1..4` with one duplicate).

3. `xor_all = 0`
   Initialize an accumulator `xor_all` to zero. We will XOR values into this variable.

4. `for num in nums:` / `xor_all ^= num`
   Loop over every element in the list and do an in-place XOR: `xor_all = xor_all ^ num`.
   This accumulates the XOR of all elements in `nums`.

5. `for i in range(1, n+1):` / `xor_all ^= i`
   XOR into the accumulator every integer from `1` to `n` (inclusive). This effectively XORs the full expected set `1..n` into the same accumulator.

6. `return xor_all`
   After both loops, the accumulator holds the duplicate value — return it.

---

## Why this works (algebraic explanation)

Let `X_nums` = XOR of every element in `nums`.
Let `X_range` = XOR of `1 ^ 2 ^ ... ^ n`.

If the `nums` list contains the numbers `1..n` **plus one extra copy of some value `d`**, then:

```
X_nums = (1 ^ 2 ^ ... ^ n) ^ d    # because one value appears twice
```

Now compute `X_nums ^ X_range`:

```
X_nums ^ X_range = ((1^2^...^n) ^ d) ^ (1^2^...^n)
                 = d ^ ((1^2^...^n) ^ (1^2^...^n))
                 = d ^ 0
                 = d
```

So the final XOR equals the duplicated number `d`.

---

## Full numeric trace (line-by-line, bit by bit)

Use example: `nums = [1, 3, 4, 2, 2]`

* `len(nums) = 5` → `n = 4`
* `xor_all` starts at `0` (binary `000` for illustration — we’ll use 3 bits because max value here is 4)

### Loop 1 — XOR all elements in `nums`

| Step | `num` | `xor_all` before (bin) | operation (bin)   | `xor_all` after (dec / bin) |
| ---- | ----- | ---------------------- | ----------------- | --------------------------- |
| init | —     | 0 `000`                | —                 | 0 `000`                     |
| 1    | 1     | 0 `000`                | `000 ^ 001 = 001` | 1 `001`                     |
| 2    | 3     | 1 `001`                | `001 ^ 011 = 010` | 2 `010`                     |
| 3    | 4     | 2 `010`                | `010 ^ 100 = 110` | 6 `110`                     |
| 4    | 2     | 6 `110`                | `110 ^ 010 = 100` | 4 `100`                     |
| 5    | 2     | 4 `100`                | `100 ^ 010 = 110` | 6 `110`                     |

After processing all elements of `nums`, `xor_all = 6` (binary `110`).

### Loop 2 — XOR with `1..n` (i = 1..4)

Start `xor_all = 6` (`110`)

| i | `xor_all` before (bin) | operation (bin)   | `xor_all` after (dec / bin) |
| - | ---------------------- | ----------------- | --------------------------- |
| 1 | 6 `110`                | `110 ^ 001 = 111` | 7 `111`                     |
| 2 | 7 `111`                | `111 ^ 010 = 101` | 5 `101`                     |
| 3 | 5 `101`                | `101 ^ 011 = 110` | 6 `110`                     |
| 4 | 6 `110`                | `110 ^ 100 = 010` | 2 `010`                     |

After XORing with `1..4`, `xor_all = 2`. The function returns `2` — which is the duplicated value in the original list.

---

## Expanded code (no `^=` operator — fully explicit assignment)

```python
def find_duplicate_explicit(nums):
    n = len(nums) - 1
    xor_all = 0

    # explicit expansion of xor loop
    for num in nums:
        xor_all = xor_all ^ num   # same as xor_all ^= num

    # explicit expansion of range loop
    for i in range(1, n + 1):
        xor_all = xor_all ^ i     # same as xor_all ^= i

    return xor_all
```

---

## Complexity & assumptions

* **Time complexity:** `O(len(nums))` — two linear passes.
* **Space complexity:** `O(1)` — only a few integer variables.
* **Assumptions (critical):**

  * `nums` contains integers in the range `1..n` and has length `n+1` (i.e., exactly one duplicate).
  * If these assumptions are violated (e.g., multiple different duplicates, missing values, or values outside `1..n`), the method **does not** produce a meaningful answer.
  * If your values are in `0..n` instead of `1..n`, you must XOR `0..n` (i.e., `range(0, n+1)`) instead of `1..n`.

---

## Pitfalls / Edge cases

* **Multiple duplicates**: XOR alone will not find all duplicates — use `Counter` or a `set` in that case.
* **Values not in 1..n**: the math breaks; adjust which numbers you XOR in the second loop to match the expected range.
* **Zero-based ranges**: if the desired values are `0..n-1`, adapt `range(...)` accordingly.

---

## Short summary

* The function uses XOR cancellation: identical values XOR to `0`, unique leftover is the duplicate.
* We first XOR every element of the array, then XOR every number in the expected range; everything that appears once in both cancels out, leaving the duplicated value.


