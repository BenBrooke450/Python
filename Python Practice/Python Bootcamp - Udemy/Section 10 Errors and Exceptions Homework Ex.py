

"""Problem 1
Handle the exception thrown by the code below
 by using try and except blocks."""
from lxml.etree import ErrorTypes
from statsmodels.sandbox.distributions.sppatch import expect

for i in ["a","b","c"]:
    try:
        print(i**2)

    except:
        TypeError
        print("String and integer opposits")

#String and integer opposits
#String and integer opposits
#String and integer opposits

####################################################################

"""Handle the exception thrown by the code below by 
using try and except blocks. Then use a finally block 
to print 'All Done.'"""


x = 5
y = 0

try:
    z = x/y
    print(z)

except:
    ZeroDivisionError
    print("Can´t divide by 0")

finally:
    print("Please double check bore running again")


#Can´t divide by 0
#Please double check bore running again


####################################################################


"""Write a function that asks for an integer and
 prints the square of it. Use a while loop with a 
 try, except, else block to account for incorrect inputs."""

def ask():
    while True:
        try:
            v = int(input("Please give a number"))
            print(v**2)
        except:
            TypeError
            print("please input a number")
            continue
        else:
            print("Yea that´s an interger")
            break

ask()

#Please give a number  f
#please input a number

#Please give a number4
16
#Yea that´s an interger

