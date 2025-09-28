
````markdown
# Python For Loops

A **for loop** is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).  
This is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-oriented programming languages.  

With the `for` loop we can execute a set of statements, once for each item in a list, tuple, set, etc.  

---

## Loop Statements

| Statement | Description |
|-----------|-------------|
| `break`   | Terminate the current loop. Use the break statement to come out of the loop instantly. |
| `continue`| Skip the current iteration of a loop and move to the next iteration. |
| `pass`    | Do nothing. Ignore the condition in which it occurred and proceed to run the program as usual. |
| `return`  | Exit the entire method you are currently executing (and possibly return a value to the caller, optional). |

---

## Examples

```python
seq = [1,2,3,4,5]

for num in seq:
    print(num)
````

Output:

```
1
2
3
4
5
```

---

```python
# This will print 'hello' five times 
for num in seq:
    print("hello")
```

Output:

```
hello
hello
hello
hello
hello
```

---

```python
# This will show you what to expect
for num in seq:
    print(num, "hello")
```

Output:

```
1 hello
2 hello
3 hello
4 hello
5 hello
```

---

```python
# Multiply each item by 2
for num in seq:
    bum = num*2
    print(bum)
```

---

```python
# Add each item to itself
for num in seq:
    bum = num + num
    print(bum)
```

---

```python
# This range() creates numbers from 0 to 100 stepping by 5
for i in range(0,100,5):
    print(i)
```

---

```python
# Demonstrating break
for i in range(10):
    if i < 5:
        print(i)
    else:
        break
```

Output:

```
0
1
2
3
4
```

---

```python
# Demonstrating if-else inside for loop
for i in range(10):
    if i < 5:
        print(i)
    else:
        print('above 5')
```

Output:

```
0
1
2
3
4
above 5
above 5
above 5
above 5
above 5
```

---

## Exercise: Sum of Current and Previous Number

```python
for i in range(10):
    print("Current Number", i, "Previous Number", i-1, "Sum:", i+(i-1))
```

---

```python
previous_num = 0
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum:", x_sum)
    previous_num = i
```

---

## Simple For Loop

```python
# Traditional for loop
for number in range(1, 5):
    print(number)

# One-liner
[print(number) for number in range(1, 5)]
```

---

## For Loop with a List

```python
mylist = ["b", "a", "s", "h"]

# Traditional for loop
for i in mylist:
    print(i)

# One-liner
[print(i) for i in mylist]
```

---

## List Comprehension

```python
# Traditional for loop
squares = []
for x in range(10):
    squares.append(x**2)

# One-liner
squares = [x**2 for x in range(10)]
```

---

## For Loop with Condition

```python
mylist = [200, 300, 400, 500]

# Traditional for loop
result = []
for x in mylist:
    if x > 250:
        result.append(x)

# One-liner
result = [x for x in mylist if x > 250]
```

---

## Nested For Loops

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# Traditional nested for loops
combined = []
for num in numbers:
    for letter in letters:
        combined.append((num, letter))

# One-liner
combined = [(num, letter) for num in numbers for letter in letters]
```

---

# Coding Exercises

---

## Maximum Profit from Stock Prices

```python
def max_num(prices : list[int]):
    min_num = min(prices)
    position_of_min = prices.index(min_num)
    max_diff = 0
    for index, nums in enumerate(prices):
        if index >= position_of_min:
            diff = nums - min_num
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_num([7,1,5,3,6,4]))
```

---

## Palindrome Checker

```python
def isPalindrome(self, string: str) -> bool:
    alpha =  ['a','b','c','d','e','f','g','h',
              'i','j','k','l','m','n','o','p',
              'q','r','s','t','u','v','w','x','y','z',
              "0","1","2","3","4","5","6","7","8","9"]

    string_split = [x.lower() for x in string if x.lower() in alpha]

    return "".join(string_split) == "".join(string_split[::-1])
```

---

## FizzBuzz

```python
def fizzbuzz(number : int):
    list1 = list(range(1, number + 1))
    for index, num in enumerate(list1):
        if num % 3 == 0 and num % 5 == 0:
            list1[index] = "FizzBuzz"
        elif num % 3 == 0:
            list1[index] = "Fizz"
        elif num % 5 == 0:
            list1[index] = "Buzz"
    return list1

print(fizzbuzz(15))
```

---

## Web Page Dimensions

```python
def web_page(number: int):
    every_number = [x for x in list(range(1,number+1)) if number % x == 0]
    combo = [[x,y] for x in every_number for y in every_number if x*y == number and x >= y]
    return min(combo)

print(web_page(100))
```

---

## Looping Through Elements in Groups

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through two elements at a time
for a, b in zip(my_list[::2], my_list[1::2]):
    print(a, b)

# Loop through three elements at a time
for a, b, c in zip(my_list[::3], my_list[1::3], my_list[2::3]):
    print(a, b, c)
```

---

## Run-Length Encoding Decompression

```python
def decomp(list1:list[int]):
    i = 0
    list2 = []
    while i < len(list1) - 1:
        for x in range(0, list1[i]):
            list2.append(list1[i+1])
        i = i + 2
    return list2

print(decomp([1,1,2,3]))
# [1, 3, 3]
```

---

```

