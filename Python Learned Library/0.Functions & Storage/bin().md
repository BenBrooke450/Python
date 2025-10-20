

you're working with binary conversion, and you'd like to go from binary back to the original integer.

You've already done this:

```python
x = 5
binary = bin(x)                   # '0b101'
stripped_binary = binary.lstrip('-0b')  # '101'
print(stripped_binary)           # '101'
```

<br>

Convert binary string '101' back to integer:

```python
binary_str = '101'
x = int(binary_str, 2)
print(x)  # Output: 5
```


```python
x = 10
binary = bin(x)                  
stripped_binary = binary.lstrip('-0b')  
print(stripped_binary)           
#1010


binary_str = str(stripped_binary)
x = int(binary_str, 2)
print(x)  # Output: 5
#10
```



# Example 1

```python


"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.



Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

"""

def hammingDistance(x: int, y: int) -> int:

    return bin(x ^ y).count("1")

print(hammingDistance(1,4))
2
```