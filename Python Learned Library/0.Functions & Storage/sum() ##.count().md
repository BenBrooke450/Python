


```python                                             SUM() VS COUNT()
Using sum()
The sum() function in Python is used to add up all the numerical values in an iterable, such as a list. Here’s a basic example:
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  
# Output: 15

You can also use sum() with a starting value:
numbers = [1, 2, 3, 4, 5]
total = sum(numbers, 10)
print(total)  
# Output: 25


Using count()
To count the occurrences of a specific element in a list, you can use the count() method of a list:
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
apple_count = fruits.count('apple')
print(apple_count)
# Output: 3

If you want to count elements based on a condition, you can use a list comprehension with sum():
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = sum(1 for x in numbers if x % 2 == 0)
print(even_count)  # Output: 5
```


```python 

tuple_of_pets = ["dog","cat","bear","bear","hamster","cat"]

tuple_tuple_of_pets = tuple(tuple_of_pets)

print(tuple_tuple_of_pets.count())

```



