"""Input() PART 1"""
"""This is how an input function works, Input() always returns a string"""

IDnumber = input("Please enter your ID number: ")

print("Welcome, " + IDnumber + "!")




"""Input() PART 2"""

x = input("Enter first number:-")
y = input("Enter second number:-")

def smaller_num(x, y): ## Can be rephrased to  def smaller_num(x, y):
    if x > y:          ##                          if x > y:
        number = y     ##                              return y
    else:              ##                          else:
        number = x     ##                              return x
    return number

print(smaller_num(x, y))


"""Input() PART 3"""


def even(str):
    for i in str:
        print(i)

str = input("Your string:")

print(even(str))

#Both of these work and one simply connects to the input() function

print(even("No_Input"))