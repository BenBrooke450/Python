A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

 

 

 
```python
# Python3 program introducing f-string

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

 

 

name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")

 

 

 

# /n Gives you a new line
newline = ord('\n')

print(f"newline: {newline}")
```