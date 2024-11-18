


"""OOP Exercise 1: Create a Class with instance attributes

Write a Python program to create a Vehicle class
 with max_speed and mileage instance attributes."""
from turtle import Vec2D

from sympy.strategies.branch import condition


class nothing:

    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage


BMW = nothing(120,800)

print(BMW.mileage)
800

print(BMW.max_speed)
120

####################################################################


"""OP Exercise 2: Create a Vehicle class without any variables 
and methods"""



class Car_nothing:

    def __init__(self):
        self.tinted_windows = True

BMW2 = Car_nothing()

print(BMW2.tinted_windows)
True



####################################################################

"""OOP Exercise 3: Create a child class Bus that
 will inherit all of the variables and methods of 
 the Vehicle class"""


#Given:

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage



class Extra_part(Vehicle):


    def __init__(self,age,condition,name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        self.age = age
        self.condition = condition

    def car(self):
        print(f"Name: {self.name} | Speed: {self.max_speed} | milage: {self.mileage}")
        print(f"Age: {self.age} | Condition: {self.condition}")


Mini = Extra_part(2, "bad","Mini",120,800)


print(Mini.car())
#Name: Mini | Speed: 120 | milage: 800
#Age: 2 | Condition: bad




####### Attempt 2


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def hours(self):
        return self.mileage/self.max_speed



class More(Vehicle):
    def hours(self):
        print("How long:",
        self.mileage / self.max_speed)

Mini = Vehicle("Mini",120,700)

print(Mini.max_speed)
120

Mini2 = More(BMW,180,600)
print(Mini2.hours())
#How long: 3.3333333333333335



####### Attempt ANSWER



class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)



####################################################################

"""OOP Exercise 4: Class Inheritance
Given:

Create a Bus class that inherits from
 the Vehicle class. Give the capacity
  argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class."""


class Vehicle_three:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


redbus = Bus("blue",120,100)

print(redbus.seating_capacity(100))
#The seating capacity of a blue is 100 passengers

####################################################################

"""OOP Exercise 5: Define a property that must 
have the same value for every class instance (object)

Define a class attribute”color” with a default 
value white. I.e., Every Vehicle should be white.

Use the following code for this exercise."""

class Vehicle_four:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle_four):
    def white(self, color = "White"):
        print(f"Color: {color} | Name: {self.name} | Speed: {self.max_speed} | milage: {self.mileage}")


class Car(Vehicle_four):
    def white(self, color = "White"):
        print(f"Color: {color} | Name: {self.name} | Speed: {self.max_speed} | milage: {self.mileage}")

mycar = Car("bob",120,1000)

print(mycar.white())
#Color: White | Name: bob | Speed: 120 | milage: 1000


####### Attempt ANSWER

class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


####################################################################

"""OOP Exercise 6: Class Inheritance
Given:

Create a Bus child class that inherits from the Vehicle class.
 The default fare charge of any vehicle is seating capacity * 100.
  If Vehicle is Bus instance, we need to add an extra 10% on full
   fare as a maintenance charge. So total fare for bus instance
    will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount 
should be 5500. You need to override the fare() method of 
a Vehicle class in Bus class.

Use the following code for your parent Vehicle class. We 
need to access the parent class from inside a method of a 
child class.

"""


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return self.capacity * 100 + ((self.capacity*100)*0.1)


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
#Total Bus fare is: 5500.0



####################################################################



"""OOP Exercise 7: Check type of an object

Write a program to determine which class a 
given Bus object belongs to."""



class Vehicle_five:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def typr_class(self):
        print(type(self.name),type(self.mileage),type(self.capacity))

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))
#<class '__main__.Bus'>

print(isinstance(School_bus,Vehicle_five))








