

def func():
    return 1

print(func())
1


####################################################################

def hello():
        return "Heeeeloo!"

print(hello())
#Heeeeloo!






def hello(name = "Jose"):
    print("Hello function")

    def greet():
        return "\t This is the greet() func"

    print(greet())

hello()
"""Hello function
	 This is the greet() func"""






def hello(name = "Jose"):
    print("Hello function")

    def greet():
        return "\t This is the greet() func"

    def welcome():
        return "\t This is welcome() inside hello"

    print(greet())
    print(welcome())
    print("This is the end of helloo")

print(hello())
"""Hello function
	 This is the greet() func
	 This is welcome() inside hello
This is the end of helloo"""


#welcome()
"""Traceback (most recent call last):
  File "/Users/benjaminbrooke/PycharmProjects/Python Bookcamp/Section 12 Python Decorators.py", line 57, in <module>
    welcome()
    ^^^^^^^
NameError: name 'welcome' is not defined"""



####################################################################



def hello(name = "Jose"):
    print("Hello function")

    def greet():
        return "\t This is the greet() func"

    def welcome():
        return "\t This is welcome() inside hello"

    if name  == "Jose":
        return greet
    else:
        return welcome


my_new_func = hello("Jose")
print(my_new_func)
#<function hello.<locals>.greet at 0x10163ab60>

print(my_new_func())
"""Hello function
	 This is the greet() func"""


####################################################################



def new_decorator(original_func):

    def wrap_func():

        print("Some extra code, before the original function")

        original_func()

        print("Some extra code, after the original function")

    return wrap_func




def my_other_func():
    print("I'm placed inbetween")

my_other_func()
#I´m placed inbetween





new = new_decorator(my_other_func)

print(new())
"""Some extra code, before the original function
I'm placed inbetween
Some extra code, after the original function"""




@new_decorator
def my_other_func():
    print("I'm placed inbetween")

my_other_func()
"""Some extra code, before the original function
I'm placed inbetween
Some extra code, after the original function"""
