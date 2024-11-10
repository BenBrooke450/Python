
"""Write a function that computes the volume of a
sphere given its radius."""
from more_itertools.more import sample


def sphere(r):
    v = (4/3)*3.14*((r)**3)
    return v

print(sphere(10))
4186.66


####################################################################

"""Write a function that checks whether a number
 is in a given range (inclusive of high and low)
 
 def ran_check(num,low,high):
 
 """


def ran_check(num,low,high):
    if low < num < high:
        print(True)
    else:
        print(False)


ran_check(10,2,20)
#True

ran_check(13,2,10)
#False

####################################################################

"""Write a Python function that accepts a string and 
calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

"""

Sample_String = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up(string):
    i = 0
    k = 0
    string = string.split(" ")
    print(string)
    string = "".join(string)
    print(string)
    for letter in string:
        print(letter)
        if letter.isupper():
            i = i + 1
        elif letter.islower():
            k = k + 1
    print(f"No. of Upper case {i}","\n",f"No. of Lower case {k}")

up(Sample_String)

#['Hello', 'Mr.', 'Rogers,', 'how', 'are', 'you', 'this', 'fine', 'Tuesday?']
#HelloMr.Rogers,howareyouthisfineTuesday?
#H
#e
#l
#l
#o
#M
#r
#.
#R
#o
#g
#e
#r
#s
#,
#h
#o
#w
#a
#r
#e
#y
#o
#u
#t
#h
#i
#s
#f
#i
#n
#e
#T
#u
#e
#s
#d
#a
#y
#?
#No. of Upper case 4
 #No. of Lower case 33



####################################################################

"""Write a Python function that takes a list and returns 
a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

"""

Sample_List = [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(list):
    new_list = []
    unique = set(list)
    for str in unique:
        new_list.append(str)
    print(new_list)

unique_list(Sample_List)

####################################################################

"""Write a Python function that checks whether a word 
or phrase is palindrome or not."""

def pen(string):
    list1 = []
    list2 = list(string)
    print(list2)
    for let in string[::-1]:
        list1.append(let)
    if list1 == list2:
        print(True)
    else:
        print(False)

pen("helleh")
#['h', 'e', 'l', 'l', 'e', 'h']
#True


####################################################################

"""Write a Python function to check whether a string is 
pangram or not. (Assume the string passed in does not 
have any punctuation)

Note : Pangrams are words or sentences containing every 
letter of the alphabet at least once.

For example : "The quick brown fox jumps over the lazy dog"

"""
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z']

string = ("The quick brown fox jumps over the lazy dog")

def pena(string):
    list1 = string.split(" ")
    list1 = "".join(list1)
    print(list1)
    list2 = []

    for let in list1:
        lowerlet = let.lower()
        list2.append(lowerlet)

    if set(list2) == set(alpha):
        print(True)
    else:
        print(False)

    print(list2)


pena(string)
#Thequickbrownfoxjumpsoverthelazydog
#True
#['t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b',
# 'r', 'o', 'w', 'n', 'f', 'o', 'x', 'j', 'u',
# 'm', 'p', 's', 'o', 'v', 'e', 'r', 't', 'h',
# 'e', 'l', 'a', 'z', 'y', 'd', 'o', 'g']



