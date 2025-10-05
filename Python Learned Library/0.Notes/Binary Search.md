

# Binary Search in Python

Binary Search is a **divide and conquer** algorithm that finds the position of a target element in a **sorted list** by repeatedly halving the search space.

---

## 🔹 Key Idea

1. Start with two pointers → `low = 0`, `high = len(list) - 1`.
2. Find the middle index → `mid = (low + high) // 2`.
3. Compare:

   * If `list[mid] == target` → found.
   * If `list[mid] < target` → search right (`low = mid + 1`).
   * If `list[mid] > target` → search left (`high = mid - 1`).
4. Repeat until `low > high`.

If not found → return `None`.

---

## 🔹 Iterative Approach

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return None

print(binary_search([1,2,3,4,5,6,7,8,9,10], 3))
# 2
```

---

## 🔹 Recursive Approach

```python
def binary_search_recursive(nums, target, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)

nums = [1,2,3,4,5,6,7,8,9,10]
print(binary_search_recursive(nums, 7, 0, len(nums)-1))
# 6
```

---

## 🔹 Example Walkthrough (Target = 3)

For `nums = [1,2,3,4,5,6,7,8,9,10]`:

1. `low = 0, high = 9 → mid = 4 → nums[4] = 5`. Target < 5 → search left.
2. `low = 0, high = 3 → mid = 1 → nums[1] = 2`. Target > 2 → search right.
3. `low = 2, high = 3 → mid = 2 → nums[2] = 3`. ✅ Found at index `2`.

---

## 🔹 Binary Search Applications

### 1. Square Root without `math.sqrt`

Use binary search to approximate square root:

```python
def mySqrt(x: int) -> int:
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid > x:
            high = mid - 1
        elif mid * mid < x:
            low = mid + 1
        else:
            return mid
    return high   # floor value

print(mySqrt(8))   # 2
print(mySqrt(103)) # 10
```

---

### 2. Find First and Last Position of Element

```python
def search_range(nums, target):
    def find_bound(is_first):
        low, high = 0, len(nums) - 1
        bound = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return bound
    
    return [find_bound(True), find_bound(False)]

print(search_range([5,7,7,8,8,10], 8))
# [3, 4]
```

---

### 3. Find Insert Position

```python
def search_insert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

print(search_insert([1,3,5,6], 5))  # 2
print(search_insert([1,3,5,6], 2))  # 1
```

---

## Pros & Cons

✅ Very efficient: O(log n).
✅ Works great for **sorted arrays**.
⚠️ Cannot be used for unsorted data.
⚠️ Recursive version may hit recursion depth for very large arrays (iterative is safer).

