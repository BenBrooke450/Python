from anaconda_project.internal.conda_api import result
from conda_build.metadata import TRUES
from sympy import false
from zmq import EVENTS

mylist = [1,2,3]
print(mylist)
#[1, 2, 3]

mylist.append(4)
print(mylist)
#[1, 2, 3, 4]

mylist.pop()
print(mylist)
#[1, 2, 3]

help(mylist.pop)
#Remove and return item at index (default last).


####################################################################
#                           Functions
####################################################################


def name_of_function(name):
    print("Hello" + name)

name_of_function("Ben")
#HelloBen




def say_hello(name):
    print(f"Hello {name}")

say_hello("benn")
#Hello benn

####################################################################

def add_num(num1,num2):
    return num1 + num2

print(add_num(10,20))
30

####################################################################


def add_num(num1,num2):
    print(num1 + num2)

add_num(20,20)
40


print(20 % 2)
0


print(20 % 3)
2

####################################################################

def even_check(number):
    result = number % 2 == 0
    return result

print(even_check(11))
#False


####################################################################

def even_check(number):
    return number % 2 == 0

print(even_check(11))
#False

####################################################################

def even_check(number):
    a = number % 2
    return a


print(even_check(11))
1

print(even_check(4))
0

####################################################################

num_list = list(range(0,70))
print(num_list)

#This function returns true if any number divided by 2 returns remainder 0
def check_even(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return false

print(check_even(num_list))
#True

print(check_even([1,3,5,7,9]))
#False


####################################################################


def check_even(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(num)
        else:
            pass
    return false

check_even(num_list)

0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68


print(check_even([1,3,5,7,9]))
#False

####################################################################

def check_even(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers


print(check_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
#[2, 4, 6, 8, 10, 12, 14]

####################################################################

def check_even(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass

print(check_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
#None

####################################################################

num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

even_numbers = []

def check_even(num_list):
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)

check_even(num_list)

print(even_numbers)
#[2, 4, 6, 8, 10, 12, 14]


####################################################################
#                           Tuple
####################################################################

stock_prices = [("APPLE",200),("GOOGLE",300),("MSFT",700)]

for items in stock_prices:
    print(items)

#('APPLE', 200)
#('GOOGLE', 300)
#('MSFT', 700)


for ticker,prices in stock_prices:
    print(prices)

200
300
700

####################################################################


work_hours = [("Abby",100),("Billy",400),("Cassie",800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return(employee_of_month,current_max)

print(employee_check(work_hours))
#('Cassie', 800)

name,hours = employee_check(work_hours)
print(name)
#Cassie

print(hours)
800


####################################################################
#               Interactions between Python Functions
####################################################################

example = [1,2,3,4,5]

from random import shuffle

shuffle(example)

print(example)
#[5, 1, 4, 2, 3]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print(shuffle_list(example))
#[4, 1, 3, 5, 2]


####################################################################

def guess_number():
    number = ""
    while number not in ["0","1","2"]:
        number = input("Guess 0, 1 or 2")
    return int(number)


def check_guess(mylist,number):
    if mylist[number] == "o":
        print("Correct!")
    else:
        print("Wrong guess!", mylist)


mylist = [" ","o"," "]

mixedup_list = shuffle_list(mylist)
guess = guess_number()
check_guess(mixedup_list,guess)


#Guess 0, 1 or 23
#Guess 0, 1 or 21
#Wrong guess! ['o', ' ', ' ']


####################################################################
#               *args and **Kwargs
####################################################################

def myfunc(a,b):
    return  sum((a,b)) * 0.05

print(myfunc(5,5))
#0.5


def myfunc(*args):
    return args

print(myfunc(50,50))
#(50, 50)


def myfunc(*ben):
    return ben

print(myfunc(50,50))
#(50, 50)


def myfunc(*ben):
    for nums in ben:
        print(nums)

myfunc(50,50,30,20,10)

#50
#50
#30
#20
#10


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs}")

myfunc(fruit = "apple")


####################################################################
#            Lambda Expressions, Map, and Filter Functions
####################################################################

def square(num):
    return num**2

mynums = [1,2,3,4,5]

print(map(square,mynums))
#<map object at 0x101809750>

print(list(map(square,mynums)))
#[1, 4, 9, 16, 25]

for nums in map(square,mynums):
    print(nums)
1
4
9
16
25




def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return "ODD"

names = ["Ben","Ana","Jack","Tayl"]

print(list(map(splicer,names)))
#['ODD', 'ODD', 'EVEN', 'EVEN']





### LAMBDA

def square(num):
    result = num ** 2
    return result

print(square(3))
9


def square(num): return num ** 2

#SAME

lambda num: num ** 2



num = [1,2,3,4,5,6]

print(list(map(lambda num:  num ** 2,mynums)))
#[1, 4, 9, 16, 25]


####################################################################
#                Nested Statements and Scope
####################################################################















