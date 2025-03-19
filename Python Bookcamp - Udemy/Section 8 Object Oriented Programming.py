from pickle import FALSE

from networkx.algorithms.distance_measures import radius



class NameofClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

        def some_method(self):
            print(self.param1)






class Dog():

    def __init__(self,breed):

        self.breed = breed

my_dog = Dog(breed = "husky")

print(my_dog.breed)
#husky

print(type(my_dog))
#<class '__main__.Dog'>





class Dog():

    def __init__(self,breed,name,spots):

        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = "husky", name = "Sammy", spots=False)
print(my_dog)
#<__main__.Dog object at 0x105685160>

print(my_dog.name)
#Sammy

print(type(my_dog))
#<class '__main__.Dog'>



####################################################################
#                Class Object Attributes and Methods
####################################################################


class Dog():

    species = "mammal"

    def __init__(self,breed,name,spots):

        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self):
        print("Woof! My name is {}".format(self.name))




my_dog = Dog(breed = "Lab", name = "Sam", spots=True)
print(type(my_dog))
#<class '__main__.Dog'>

print(my_dog.species)
#mammal

print(my_dog.name)
#Sam

my_dog.bark()
#Woof! My name is Sam


####################################################################


class Dog():

    species = "mammal"

    def __init__(self,breed,name):

        self.breed = breed
        self.name = name

    def bark(self,number):
        print("Woof! My name is {} and the number is {}".format(self.name,number))




my_dog = Dog(breed = "Lab", name = "Sam")
print(type(my_dog))
#<class '__main__.Dog'>

print(my_dog.breed)
#lab

print(my_dog.name)
#Sam

my_dog.bark(10)
#Woof! My name is Sam and the number is 10



####################################################################


class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radiuss =1 ):
        self.radiuss = radiuss
        self.area = radiuss*radiuss*self.pi #OR Circle.pie

    def get_circumference(self):
        return self.radiuss * Circle.pi * 2

my_circle = Circle()
my_radius = Circle(10)

print(my_radius.radiuss)
#10

print(my_circle.radiuss)
#1

print(my_circle.pi)
#3.14

print(my_circle.get_circumference())
#6.48

print(my_circle.area)
#3.14


####################################################################
#                Inheritance and Polymorphism
####################################################################


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_I(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

print(Animal().who_am_I())
#ANIMAL CREATED
#I am an animal
#None

An = Animal()
print(An.eat())
#ANIMAL CREATED
#I am eating
#None

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")


mydog = Dog()
#ANIMAL CREATED
#Dog created

myanimal = Animal()
#ANIMAL CREATED


####################################################################


class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + "says woof!"



class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says meow!"

niko = Dog("niko ")
print(niko)
#<__main__.Dog object at 0x102a4c8f0>

print(niko.speak())
#nikosays woof!


felix = Cat("felix ")
print(felix)
#<__main__.Cat object at 0x1052e0ad0>

print(felix.speak())
#felix says meow!


for pet in [niko,felix]:

    print(type(pet))
    print(type(pet.speak()))

#<class '__main__.Dog'>
#<class 'str'>
#<class '__main__.Cat'>
#<class 'str'>

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
#niko says woof!

pet_speak(felix)
#felix says meow!



####################################################################

class Animal():

    def __init__(self,name):

        self.name = name

    def speak(self):
        raise NotImplementedError("bla bla bla")



an = Animal(name = "Ben")
print(an.name)
#Ben



class Dog(Animal):

    def speak(self):
        return self.name  + " says woof!"



class Cat(Animal):

    def speak(self):
        return self.name  + " says meow!"



bob = Dog("bob")
print(bob.speak())
#bob says woof!


betty = Cat("betty")
print(betty.speak())
#betty says meow!




####################################################################
#                Special (Magic/Dunder) Methods
####################################################################




mylist = [1,2,3]

print(len(mylist))
3


class Sample():
    pass


mysample =  Sample()
print(mysample)
#<__main__.Sample object at 0x104b62660>







class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages =  pages


b = Book("Python rocks","Jose",200)

print(b)
#<__main__.Book object at 0x103738a10>






class Book2():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages =  pages


    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

b = Book2("Python rocks","Jose",200)


print(str(b))
#Python rocks by Jose

print(len(b))
200


del b

b

