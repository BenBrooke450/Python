


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




<br><br><br><br><br><br><br><br><br><br><br>



Here is a **clear, deep, and very detailed explanation** of the difference between:

1. **A normal Python class**
2. **A PyTorch model class (`class ABC(nn.Module)`)**

This is one of the most important things to fully understand when using PyTorch.

---

# ✅ **1. Normal Python Class (`class ABC:`)**

### ✔ What is it?

A normal Python class is *just a blueprint for creating objects*.
It has **no special behavior** beyond what you define yourself.

Example:

```python
class ABC:
    def __init__(self):
        print("I am a normal class")
        self.value = 10

    def add(self, x):
        return self.value + x
```

### ✔ What happens when you call it?

```python
obj = ABC()
```

Python does:

1. Creates an empty object in memory
2. Calls `__init__()` on that object
3. Returns the object and assigns it to `obj`

### ✔ Key properties of a normal class

| Feature                               | Behavior                    |
| ------------------------------------- | --------------------------- |
| `__init__`                            | Only initializes the object |
| Contains functions                    | You call them manually      |
| No special integration with libraries | Just pure Python            |

### ✔ Example use

```python
obj = ABC()
result = obj.add(5)
```

You must call methods manually.
Nothing happens behind the scenes.

---

# 🔥 **2. PyTorch Model Class (`class ABC(nn.Module)` )**

This is **NOT** just a normal Python class.
It inherits from `torch.nn.Module`, which gives it **deep learning behavior**.

Example:

```python
import torch.nn as nn

class ABC(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)
```

### ✔ What happens when you call it?

```python
model = ABC()
```

Behind the scenes PyTorch does MUCH more than Python normally does:

1. Creates the object
2. Calls `__init__()`
3. Registers every layer (e.g., `nn.Linear`)
4. Tracks all parameters (weights, biases)
5. Makes the model ready for:

   * `.forward()` execution
   * `.backward()` gradients
   * `.parameters()` for the optimizer
   * `.train()` and `.eval()`
   * Moving to GPU via `.to(device)`
   * Saving/Loading using `state_dict`

### ✔ Most important part: calling the model calls `forward()`

In PyTorch this:

```python
output = model(x)
```

automatically calls:

```python
output = model.forward(x)
```

(through magic methods implemented in `nn.Module`)

You should **NEVER** call `forward()` manually.

---

# 🧠 Detailed Comparison Table

| Feature            | Normal Python Class    | PyTorch `nn.Module` Class       |
| ------------------ | ---------------------- | ------------------------------- |
| Inherits from      | `object`               | `nn.Module`                     |
| `__init__()`       | Only sets up variables | Registers layers and parameters |
| Calling the object | Does nothing special   | Automatically calls `forward()` |
| Tracks parameters  | No                     | Yes (`model.parameters()`)      |
| Optimizer works?   | No                     | Yes                             |
| Backpropagation?   | No                     | Yes                             |
| GPU support        | No                     | Yes (`model.to(device)`)        |
| Save/Load          | Not special            | `model.state_dict()`            |
| Used for ML?       | No                     | Yes                             |

---

# 🧪 Example — Seeing the difference

### Normal class

```python
class Normal:
    def __init__(self):
        self.x = 1

    def forward(self, a):
        return a + 1

obj = Normal()
print(obj(10))   # ❌ ERROR — object is not callable
```

You **cannot** call `obj(10)` → normal classes are NOT callable unless you override `__call__`.

---

### PyTorch model class

```python
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

model = Model()
print(model(torch.randn(1, 10)))  # ✔ WORKS — calls forward()
```

A PyTorch model **acts like a function** because `nn.Module` overrides `__call__`.

---

# 🧩 Why this matters in practice

**Only PyTorch model classes:**

* participate in gradient updates
* integrate with optimizers
* implement autograd
* behave like functions when called
* allow `model.train()` / `model.eval()`
* know how to save and load weights

Normal classes do NONE of this.

---

# 🎯 Final Summary

### Normal Class (`class ABC:`)

* Pure Python
* `__init__` only initializes variables
* No deep learning features
* Calling the object does not call any method
* No automatic tracking of parameters

### PyTorch Model Class (`class ABC(nn.Module)`)

* Inherits neural-network behaviors from `nn.Module`
* `__init__` registers layers and parameters
* Calling the object *automatically calls forward()*
* Supports autograd, optimizers, GPU, saving/loading
* Designed for training neural networks

---

If you want, I can create an illustrated diagram showing the internal call flow:
`model(x) → __call__ → forward() → output`.

Just let me know.


