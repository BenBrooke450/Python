

"""
Problem 1
Create a generator that generates the squares of numbers up
to some number N.

"""



def gensquare(n):
    for x in range(n):
       yield x**2

for number in gensquare(10):
    print(number)

0
1
4
9
16
25
36
49
64
81


####################################################################

"""Problem 2

Create a generator that yields "n" random numbers between 
a low and high number (that are inputs).

Note: Use the random library. For example:"""


import random

def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

7
5
1
10
9
4
2
5
5
1
6
7


####################################################################

"""Problem 3

Use the iter() function to convert
 the string below into an iterator:"""


s = 'hello'

s_inter = iter(s)

print(next(s_inter))
#h





"""Can you explain what gencomp is in the code below?"""

y_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

