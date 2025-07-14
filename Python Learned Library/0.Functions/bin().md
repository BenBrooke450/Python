

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