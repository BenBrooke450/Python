



## Example 1

Let’s visualize **why your original code is incorrect** using a diagram. I’ll show each step for your input `[1, 2, 3, 4, 5]` and highlight where the recursion fails.

---

<br>

### **Step 1: Initial call**

```
triangularSum([1, 2, 3, 4, 5])
       │
       ▼
    trin_add([1, 2, 3, 4, 5])
```

---

<br>

### **Step 2: Build next\_layer**

* Your code creates `next_layer` as:

```
[ (1+2)%10, (2+3)%10, (3+4)%10, (4+5)%10 ]
= [3, 5, 7, 9]
```

* Then you do:

```
nums = next_layer
trin_add(nums)   # recursive call
return nums      # ⚠ Problem: returns [3, 5, 7, 9] instead of final value
```

---

<br>

### **Step 3: Recursion happens but result is ignored**

```
trin_add([3, 5, 7, 9])
       │
       ▼
next_layer = [ (3+5)%10, (5+7)%10, (7+9)%10 ] 
           = [8, 2, 6]
trin_add([8, 2, 6])  # recursive call
return nums           # ⚠ Still returns [3, 5, 7, 9] from previous layer
```

* Notice how the **final single number never propagates up**.
* Each recursive call calculates the next layer but **its return is never used**.

---

<br>

### **Step 4: Why the final result is wrong**

```
Original call returns:
    return nums  → [3, 5, 7, 9]
```

* The function never returns `6` (the correct triangular sum) because it ignores the recursive result.

---

✅ **Summary of the Problem in Diagram Form**

```
[1, 2, 3, 4, 5]  <- initial nums
       │
       ▼
 next_layer = [3, 5, 7, 9] 
       │
       ▼
trin_add([3, 5, 7, 9])  <- recursion
       │
       ▼
 next_layer = [8, 2, 6]
       │
       ▼
trin_add([8, 2, 6])  <- recursion
       │
       ▼
 next_layer = [0, 8]
       │
       ▼
trin_add([0, 8])  <- recursion
       │
       ▼
 next_layer = [8]
       │
       ▼
trin_add([8])  <- recursion
       │
       ▼
 returns 8
       │
       ▼
But ignored in previous layers → original call returns [3, 5, 7, 9] ❌
```

---


