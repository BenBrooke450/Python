
"""Given two integer numbers, write a Python code to return their product
only if the product is equal to or lower than 1000. Otherwise, return their sum."""
from numba.cuda.printimpl import print_item
from tenacity import retry_unless_exception_type


def sumreturn(number1,number2):
    if number1*number2 <= 1000:
        print(number1*number2)
    else:
        print(number1 + number2)

sumreturn(30,30)
sumreturn(40,40)



def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2







"""Write a Python code to iterate the first 10 numbers,
 and in each iteration, print the sum of the current and previous number."""

for i in range(10):
    print("Current Number",i,"Previous Numbner",i-1,"Sum:",i+(i-1))


print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i


"""Write a Python code to accept a string from the 
user and display characters present at an even index number."""

str = input("Your string:")
x = 0

def even(str):
    for i in range(len(str)):
        if i % 2 ==0:
            print(str[i])

even(str)

#Or

even("Not Hello")



"""Write a Python code to remove characters
 from a string from 0 to n and return a new string."""

str = input("Please write your input:")
x = int(input())

def remove(str,x):
    print(str[x:])

remove(str,x)



"""Write a code to return True if the list’s first and last numbers
 are the same. If the numbers are different, return False."""

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def first_last(num):
    if num[0] == num[-1]:
        print("true")
    else:
        print("False")

first_last(numbers_x)







"""Write a Python code to display numbers from a list divisible by 5"""

list = [10, 20, 33, 46, 55]

def five(num):
    for num in list:
        if num % 5 == 0:
            print(num)

five(list)



"""Write a Python code to find how often the substring 
“Emma” appears in the given string."""


str_x = "Emma is good developer. Emma is a writer"

def emma(text):
    n = 0
    words = text.split()
    for word in words:
        if word == "Emma":
            n = n + 1
    return n


print(emma(str_x))



for num in range(1,2):
    print(num)
    for num1 in range(2,3):
        print(num1,num1)
        for num2 in range(3,4):
            print(num2,num2,num2)
            for num3 in range(4,5):
                print(num3,num3,num3,num3)
                for num4 in range(5,6):
                    print(num4,num4,num4,num4,num4)



"""Write a Python code to check if the given number is palindrome. 
A palindrome number is a number that is the same after reverse.
 For example, 545 is the palindrome number."""

def pan(x):
    y = int(x)
    if 1000 > y > 100:
        z = y.__str__()
        if z[0] == z[2]:
            print("THIS IS A PALINDROME:",x)
        else:
            print("THIS IS NOT A PALINDROME")
    else:
        print("NEEDS TO BE BETWEEN 100 & 1000")


print(pan(123))
print(pan(252))



"""Given two lists of numbers, write a Python code to create a new list 
such that the latest list should contain odd numbers from the first list 
and even numbers from the second list.
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def oddeven(list1,list2):
    mylist = []
    for num1 in list1:
        if num1 % 2 == 0:
            pass
        else:
            print(num1)
    for num2 in list2:
        if num2 % 2 == 0:
            print(num2)

oddeven(list1,list2)




def merge_list(list1, list2):
    result_list = []

    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)

    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list


"""For example, If the given integer number is 7536, the
 output shall be “6 3 5 7“, with a space separating the digits."""


def number(number):
    string = number.__str__()
    MYLIST = []
    for nums in reversed(string):
        MYLIST.append(nums)
    return MYLIST

print(number(12345))


def income(pay):
    if pay < 10000:
        print("NO TAX")
    elif 0 < pay <20000:
        y = pay -10000
        z = y*0.10
        print("TAX NEEDED TO PAY:",z)
    else:
        q = (pay - 20000)*0.2
        print("TAX NEEDED TO PAY:",q + 1000)


income(18500)
income(27000)




def times(num):
    for nums in range(num):
        print(nums,nums*2,nums*3,nums*4,nums*5,nums*6,nums*7)

times(10)





