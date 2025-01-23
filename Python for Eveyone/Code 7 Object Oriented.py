



class Number:

    x = 0

    def __init__(self,name):
        self.nam = name
        print(self.nam)

    def party(self):
        self.x = self.x + 1


number1 = Number(name = "Ben")
#Ben

print(number1.nam)
#Ben




####################################################################

class Number:

    x = 0

    def __init__(self,nam):
        self.name = nam
        print(self.name)

    def party(self):
        self.x = self.x + 1

number2 = Number("Bob")
#Bob

print(number2.name)
#Bob


####################################################################


class Math:

    def __init__(self,number1,number2):
        self.number1 = 1
        self.number2 = 2
        print(self.number1,self.number2)

num = Math(4,3)
#1 2

print(num.number1)
1

"""
The inputs within the functions number1 and number2 don´t connect
self.number1 and self.number2 like:

self.number1 = number1

So the input aren´t connecting to anything, so anytime you call .number1
you will only ever get 1

"""


####################################################################


class Math_round_2:


    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
        print(number1,number2)

more_numbers = Math_round_2(5,6)
#5 6

print(more_numbers.number1)
#5




