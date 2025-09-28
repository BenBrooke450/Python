

````markdown
# Python OOP Definitions

### Class
- A **template** or blueprint for creating objects.  
- Defines attributes (data) and methods (behavior).  

---

### Attribute
- A **variable inside a class**.  
- Stores information about the object.  
```python
class Dog:
    def __init__(self, name):
        self.name = name   # Attribute
````

---

### Method

* A **function inside a class**.
* Defines behavior an object can perform.

```python
class Dog:
    def bark(self):    # Method
        return "Woof!"
```

---

### Object

* A **particular instance of a class**.
* Created when you call the class.

```python
dog1 = Dog()   # Object (instance of Dog class)
```

---

### Constructor

* Special method `__init__()` that runs when an object is created.
* Used to initialize attributes.

```python
class Dog:
    def __init__(self, name):   # Constructor
        self.name = name
```

---

### Inheritance

* Ability to **extend a class** to make a new one.
* The new class (subclass/child) inherits attributes and methods from the parent class.

```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):   # Inherits from Animal
    def make_sound(self):
        return "Woof!"
```



<br><br><br><br><br>




````markdown
# Python: Creating a Subclass

In Python, a **subclass** is a class that inherits attributes and methods from another class, known as the **superclass** (or parent class).  

This allows you to:
- Create specialized versions of existing classes  
- Reuse code without rewriting functionality  
- Promote modularity and extensibility  

---

## Basic Syntax

```python
class SubclassName(BaseClassName):
    # Class attributes and methods for the subclass
    pass
````

---

## Example 1: Simple Subclass

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


# Creating instances
generic_animal = Animal("Generic Animal")
dog_instance = Dog("Buddy")

# Accessing attributes and methods
print(generic_animal.name)      # Output: Generic Animal
print(dog_instance.name)        # Output: Buddy
print(dog_instance.make_sound()) # Output: Woof!
```

➡️ Here, `Dog` is a subclass of `Animal`.
It **inherits** `name` and `make_sound()` but **overrides** `make_sound()` with its own implementation.

---

## Example 2: Adding Additional Attributes

```python
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)   # Call parent constructor
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Creating instances
generic_shape = Shape("Red")
circle_instance = Circle("Blue", 5)

# Accessing attributes and methods
print(generic_shape.color)     # Output: Red
print(circle_instance.color)   # Output: Blue
print(circle_instance.radius)  # Output: 5
print(circle_instance.area())  # Output: 78.5
```

➡️ `Circle` subclasses `Shape`, adds a **radius attribute**, and overrides the `area()` method.

---

## Example 3: Account Class

```python
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, num):
        if (self.balance - num) < 0:
            print("Sorry not enough in the bank to take that amount")
            print("Only this Account balance:", self.balance)
        else:
            self.balance = self.balance - num
            print("Account balance:", self.balance)

    def deposit(self, num):
        self.balance = self.balance + num
        print("Account balance:", self.balance)

    def __str__(self):
        print(f"Account owner:{self.owner}")
        print(f"Account balance:{self.balance}")
```

### Usage:

```python
Account1 = Account(owner="Ben", balance=1000)

Account1.__str__()
# Account owner: Ben
# Account balance: 1000

Account1.withdraw(100)  # 900
Account1.withdraw(100)  # 800
Account1.withdraw(350)  # 450
print(Account1.balance) # 450

Account1.withdraw(500)
# Sorry not enough in the bank to take that amount
# Only this Account balance: 450

Account1.deposit(400)   # 850
Account1.withdraw(850)  # Account balance: 0
```

---

# Summary

* **Subclassing** lets you inherit and extend existing classes.
* Use `super()` to call the parent class’s constructor.
* You can **override** methods and add **new attributes** in subclasses.
* This makes code reusable and modular.

```

