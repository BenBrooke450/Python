from dask.dataframe.methods import index_count
from sympy import false


####################################################################
#                                IF
####################################################################

if 3>2:
    print("true")
#true


####################################################################


hungry = false

if hungry:
    print("FEED ME")
else:
    print("I´m not hungry")

#I´m not hungry
####################################################################

loc = "Bank"

if loc == "Auto Shop":
    print("Cars are cool")
elif loc == "Bank":
    print("money is cool")
else:
    print("I do not know")

#money is cool


####################################################################
#                               FOR LOOP
####################################################################

my_list = [1,2,3]

for nums in my_list:
    print("a")
#a
#a
#a

for nums in my_list:
    print(nums)
#1
#2
#3


####################################################################

my_list2 = [1,2,3,4,5,6,7,8,9,10]

for nums in my_list2:
    if nums % 2 == 0:
        print(nums)

#2
#4
#6
#8
#10


for index,nums in enumerate(my_list2):
    if nums % 2 == 0:
        print(index,nums)

#1 2
#3 4
#5 6
#7 8
#9 10

####################################################################

#TUPLES

mylist = [(1,2),(3,4),(5,6)]

print(len(mylist))
#3

for (a,b) in mylist:
    print(a)
#1
#3
#5

for (a,b) in mylist:
    print(a)
#2
#4
#6

####################################################################

#DICTIONARY

d = {"k":1,"K2":2,"K3":3}

for values in d.values():
    print(values)
#1
#2
#3



for values in d.keys():
    print(values)
#k
#K2
#K3


####################################################################
#                           WHILE LOOP
####################################################################

x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x = x + 1
#The current value of x is 0
#The current value of x is 1
#The current value of x is 2
#The current value of x is 3
#The current value of x is 4


x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x = x + 1
else:
    print("NOT BIGGER THAN FIVE")

#The current value of x is 0
#The current value of x is 1
#The current value of x is 2
#The current value of x is 3
#The current value of x is 4
#NOT BIGGER THAN FIVE

x = [1,2,3,4,5]

for item in x:
    pass


for item in x:
    if item == 3:
        continue
    print(item)
#1
#2
#4
#5



for item in x:
    if item == 4:
        break
    print(item)
#1
#2
#3

####################################################################
#                           Useful Operators
####################################################################

for num in range(5):
    print(num)
0
1
2
3
4

for num in range(1,6):
    print(num)
1
2
3
4
5

for num in range(0,10,2):
    print(num)
0
2
4
6
8



index_count = 0
word = "abcde"
for letter in word:
    print(index_count,word[index_count])
    index_count = index_count + 1
#0 a
#1 b
#2 c
#3 d
#4 e



for index,letter in enumerate("abcde"):
    print([index],letter)
#[0] a
#[1] b
#[2] c
#[3] d
#[4] e




for index,letter in enumerate("abcde"):
    print([index],letter)
    print("\n")
#[0] a

#[1] b

#[2] c

#[3] d

#[4] e



a = [1,2,3,4,5]
b = ["a","b","c","d","e"]

for item in zip(a,b):
    print(item)
#(1, 'a')
#(2, 'b')
#(3, 'c')
#(4, 'd')
#(5, 'e')


print("x" in ["x","y","z"])
#True

print("mykey" in {"mykey":1,"my2key":2})
#True


d2 = {"mykey":1,"my2key":2}
print(1 in d.values())
#True


####################################################################
#                      List Comprehensions
####################################################################


mystring = "hello"

mylist = []

for letter in mystring:
    mylist.append(letter)
    print(letter)
#h
#e
#l
#l
#o

print(mylist)
#['h', 'e', 'l', 'l', 'o']


list = [letter for letter in mystring]
print(list)
#['h', 'e', 'l', 'l', 'o']

list = [print(letter) for letter in "abcde"]
#a
#b
#c
#d
#e

list = [print(num) for num in [1,2,3,4,5,6]]
1
2
3
4
5
6

list3 = [print(x) for x in range(1,10) if x%2==0]

2
4
6
8


list3 = [print(x**2) for x in range(1,10) if x%2==0]

4
16
36
64




