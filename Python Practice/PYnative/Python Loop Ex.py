from itertools import count

for num in range(1,11):
    print(num)

####################################################################

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



####################################################################

"""For example, if the user entered 10, 
the output should be 55 (1+2+3+4+5+6+7+8+9+10)"""

x=0

number = input("Pick number:",)
numin = int(number) + 1
mylist = []

for num in range(1,numin):
    mylist.append(num)
    x = sum(mylist)
    print(x)



####################################################################

"""Print multiplication table of a given number"""

num1 = input("Times table",)
number = int(num1)

for num in range(10):
    a = number*num
    print(a)

####################################################################


"""Write a Python program to display only those
 numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the following number
If the number is greater than 500, then stop the loop

"""

numbers = [12, 75, 150, 180, 145, 525, 50]
mylist1 = []

for nums in numbers:
    if nums % 5 == 0:
        mylist1.append(nums)
        print(mylist1)

for num1 in mylist1:
    if num1 <= 150:
        print(num1)
    elif 150 < num1 < 500:
        pass
    elif num1 > 500:
        break




numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)


###################################################################


"""Count the total number of digits in a number"""

num1 = input("Count Digits",)
number = int(num1)
z = 0

for digits in number:
    z = z + 1

