
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

 - 5(1##) 3(0##)  = (1..) >  5(#0#) 3(#1#) = (11.) > 5(##1) 3(##1) = (110)

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

 - 5(1##) 3(0##)  = (1..) >  5(#0#) 3(#1#) = (11.) > 5(##1) 3(##1) = (110)

```

---

### Example 2: Looping through an array

```python
nums = [3, 0, 1]
xor_all = 0

for num in nums:
    xor_all ^= num   # same as xor_all = xor_all ^ num

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
    xor_all ^= num

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

