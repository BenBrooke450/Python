
####################################################################
#                   Python Collections Module
####################################################################


from collections import Counter

mylist = [1,1,1,1,2,2,3,3,4,5,5,6]

print(Counter(mylist))
#Counter({1: 4, 2: 2, 3: 2, 5: 2, 4: 1, 6: 1})


mylist2 = ["a","a","b",10,10,10]

print(Counter(mylist2))
Counter({10: 3, 'a': 2, 'b': 1})



sentence = "How many times does this word show up in this sentence"
print(Counter(sentence.lower().split()))
Counter({'this': 2, 'how': 1, 'many': 1, 'times': 1, 'does': 1, 'word': 1, 'show': 1, 'up': 1, 'in': 1, 'sentence': 1})



letters = "aaaaabbbbcccvvghdtfy"

c = Counter(letters)

print(c)
#Counter({'a': 5, 'b': 4, 'c': 3, 'v': 2, 'g': 1, 'h': 1, 'd': 1, 't': 1, 'f': 1, 'y': 1})


print(c.most_common())
#[('a', 5), ('b', 4), ('c', 3), ('v', 2), ('g', 1), ('h', 1), ('d', 1), ('t', 1), ('f', 1), ('y', 1)]


####################################################################


from collections import defaultdict

d = {"a":10}

print(d)
{'a': 10}


print(d["a"])
10






####################################################################


mytuple = (10,20,30)

print(mytuple[1])
20


from collections import namedtuple

Dog = namedtuple("Dog",["age","breed","name"])

sammy  = Dog(age = 5, breed = "BOB", name = "Sam")

print(sammy)
#Dog(age=5, breed='BOB', name='Sam')

print(sammy.age)
5










####################################################################
#                       Math and Random Module
####################################################################



import math

help(math)
"""DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.........."""


value = 4.35
print(math.floor(value))
4


print(math.ceil(value))
5


print(round(4.56777))
5


print(math.pi)
3.141592653589793


print(math.e)
2.718281828459045



print(math.log(math.e))
1.0


print(math.log(100,10))
2.0


####################################################################

import random

print(random.randint(1,100))
79
...


mylist = list(range(0,20))

print(random.choice(mylist))
2

random.shuffle(mylist)

print(mylist)
[17, 5, 2, 10, 14, 11, 19, 4, 13, 0, 16, 6, 8, 18, 3, 1, 12, 15, 9, 7]




####################################################################
#                       Python Regular Expressions
####################################################################


text = "The agent's phone number is 408-555-1234"

print("phone" in text)
#True


import re

pattern  = "phone"

print(re.search(pattern,text))
#<re.Match object; span=(12, 17), match='phone'>


print(text[12:17])
#phone








text = "The agent's phone number is 408-555-1234, phone is long"

matches = re.search("phone",text)


print(matches)
#<re.Match object; span=(12, 17), match='phone'>


print(re.findall("phone",text))
#['phone', 'phone']



for match in re.finditer("phone",text):
    print(match)

"""
<re.Match object; span=(12, 17), match='phone'>
<re.Match object; span=(42, 47), match='phone'>
"""



for match in re.finditer("phone",text):
    print(match.span())
"""
(12, 17)
(42, 47)
"""











text  = "My number is 408-555-1234"

phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d",text)

print(phone)
#<re.Match object; span=(13, 25), match='408-555-1234'>





phone = re.search(r"\d{3}-\d{3}-\d{4}",text)

print(phone)
#<re.Match object; span=(13, 25), match='408-555-1234'>




phone_pattern  = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

results = re.search(phone_pattern,text)

print(results)
#<re.Match object; span=(13, 25), match='408-555-1234'>

print(results.group())
#408-555-1234


print(results.group(1))
#408















print(re.search(r"cat","The cat is here"))
#<re.Match object; span=(4, 7), match='cat'>

print(re.findall(r"...at","The cat in the hat went splat"))
#['e cat', 'e hat', 'splat']


print(re.findall(r"\d","The cat 2 in the hat went splat"))
#['2']



text  = "This string is here! but it has punctuation?, How can we."

print(re.findall(r'[^!?.]',text))
#['T', 'h', 'i', 's', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 'i', 's', ' ', 'h', 'e', 'r', 'e', ' ', 'b', 'u', 't', ' ', 'i', 't', ' ', 'h', 'a', 's', ' ', 'p', 'u', 'n', 'c', 't', 'u', 'a', 't', 'i', 'o', 'n', ',', ' ', 'H', 'o', 'w', ' ', 'c', 'a', 'n', ' ', 'w', 'e']

print(re.findall(r'[^!?.]+',text))
#['This string is here', ' but it has punctuation', ', How can we']

print(re.findall(r'[^!?. ]+',text))
#['This', 'string', 'is', 'here', 'but', 'it', 'has', 'punctuation', ',', 'How', 'can', 'we']















