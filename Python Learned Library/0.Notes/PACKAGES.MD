

# **1. What is a Python package?**

A **Python package** is a **directory containing Python modules (`.py` files) and an `__init__.py` file**.

* A **module** = a single `.py` file with functions, classes, or variables.
* A **package** = a folder of modules (can have sub-packages).

Packages allow you to:

* Organize code logically
* Import code easily in other projects
* Share code with others or across multiple projects

---

### **1.1 Minimal package example**

```
my_package/
    __init__.py
    module1.py
    module2.py
```

* `__init__.py` can be empty, or it can **expose certain classes/functions for easier import**.

**Example:**

`module1.py`:

```python
def greet(name):
    return f"Hello, {name}!"
```

`module2.py`:

```python
def add(a, b):
    return a + b
```

`__init__.py` (optional):

```python
# Makes importing easier
from .module1 import greet
from .module2 import add
```

**Usage in another script or notebook**:

```python
# If the folder is in sys.path or installed
from my_package import greet, add

print(greet("Ben"))
print(add(3, 4))
```

Without `__init__.py`, you would have to do:

```python
from my_package.module1 import greet
from my_package.module2 import add
```

---

# **2. How to create a package**

### **Step 1: Create a folder**

```
mkdir my_package
cd my_package
```

### **Step 2: Add `__init__.py`**

```
touch __init__.py
```

* Can be empty
* Or can contain initialization code (imports, constants, etc.)

### **Step 3: Add modules**

```
touch module1.py module2.py
```

* Each `.py` file is a module
* Put your functions or classes inside


<br><br><br><br><br>

# IMPORTANT TO UNDERSTAND, look further down for when you want to build an actual python package to call from anywhere

### **Step 4: Test imports**

* Either put your package in the **same folder as your notebook**
* Or **add it to `sys.path`**:

```python
import sys
sys.path.append("/path/to/my_package")

from my_package import greet, add
```


<br><br><br><br><br><br><br><br><br><br>


---

# **3. Adding to a package**

You can **add modules or functions anytime**.

Example:

```
my_package/
    __init__.py
    module1.py
    module2.py
    module3.py  # new module added
```

* Update `__init__.py` if you want `module3`’s content available at the package level:

```python
from .module3 import new_function
```

* Now you can do:

```python
from my_package import new_function
```

* Or without updating `__init__.py`:

```python
from my_package.module3 import new_function
```

**Key point:** Python doesn’t require you to “rebuild” the package; just add files and update imports as needed.

---

# **4. Using sub-packages**

Packages can contain **subfolders that are also packages**:

```
my_package/
    __init__.py
    module1.py
    sub_package/
        __init__.py
        module3.py
```

Importing:

```python
from my_package.sub_package.module3 import my_func
```

---

# **5. Installing a package locally (editable install)**

If you want to **use a package across multiple projects**:

1. Add a `setup.py` file in your package root:

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
)
```

2. Install it **editable**:

```bash
pip install -e /path/to/my_package
```

* `-e` = editable → any changes in the source code are reflected immediately
* After this, you can do:

```python
from my_package import greet, add
```

from **anywhere**, no need for `sys.path.append`.

---

# **6. Best practices for packages**

1. **Use `__init__.py` to control the public API**: only expose what’s needed.
2. **Organize logically**: group related functions/classes into modules.
3. **Use relative imports inside the package**:

```python
# Inside module2.py
from .module1 import greet  # relative import within package
```

4. **Keep scripts separate**: don’t mix notebooks or scripts in the package folder.
5. **Use editable installs (`pip install -e`)** for development, especially if you update the package frequently.

---

# **7. Real example with your TinyVGG model**

You could turn your `model_builder.py` into a package like this:

```
pytorch_models/
    __init__.py
    tinyvgg/
        __init__.py
        model_builder.py
```

`tinyvgg/__init__.py`:

```python
from .model_builder import TinyVGG
```

Then in your notebook:

```python
import sys
sys.path.append("/Users/benjaminbrooke/PycharmProjects/Python_PyTroch/PyTorch for Deep Learning Bootcamp - Udemy/Section 7 - PyTorch Going Modular")

from pytorch_models.tinyvgg import TinyVGG

model = TinyVGG(input_shape=3, hidden_units=10, output_shape=10)
```

* Later, you can add another model:

```
pytorch_models/
    resnet/
        __init__.py
        resnet_builder.py
```

* Update `pytorch_models/__init__.py` if you want all models accessible via one import.

---

# **8. Summary Table**

| Concept           | Description                                             | Example                              |
| ----------------- | ------------------------------------------------------- | ------------------------------------ |
| Module            | Single `.py` file                                       | `model_builder.py`                   |
| Package           | Folder with `__init__.py`                               | `my_package/`                        |
| Sub-package       | Folder inside a package with `__init__.py`              | `my_package/sub_package/`            |
| `__init__.py`     | Marks folder as package; can control what is imported   | `from .module1 import func`          |
| Editable install  | `pip install -e .` makes package usable across projects | `pip install -e /path/to/my_package` |
| Adding to package | Add new `.py` files or update `__init__.py`             | Add `module3.py`                     |

---

**Key takeaways**:

1. **Packages = folders + `__init__.py`**
2. **Modules = Python files inside packages**
3. **You can add modules anytime**; just update imports
4. **Editable installs** make packages accessible across projects without copying files
5. **Relative imports** help keep the package self-contained




<br><br><br><br><br><br>


Exactly — `__init__.py` is **the key file that turns a folder into a Python package**, and what you put in it controls **how your package can be imported and used**. Let’s break it down carefully.

---

## **1. What `__init__.py` is**

* It’s a **Python file** that is required (even if empty) to make Python treat the folder as a package.
* Python looks for this file when you try to import something from the folder.
* It can be **empty** if you just want the folder to be a package without customizing imports.

Example:

```
my_package/
    __init__.py   <- can be empty
    module1.py
    module2.py
```

You can still import like:

```python
from my_package.module1 import some_function
```

---

## **2. Why you might put code in `__init__.py`**

Putting code in `__init__.py` allows you to **control the public interface of the package**, meaning you can make imports simpler and cleaner.

**Example:**

`module1.py`:

```python
def greet(name):
    return f"Hello, {name}!"
```

`module2.py`:

```python
def add(a, b):
    return a + b
```

Without modifying `__init__.py`, you’d import like this:

```python
from my_package.module1 import greet
from my_package.module2 import add
```

---

### **2.1 Making imports easier**

If you add this to `__init__.py`:

```python
from .module1 import greet
from .module2 import add
```

Now you can do a **single, simpler import**:

```python
from my_package import greet, add
```

* `.` = “relative import” → look inside the same package folder
* This makes it much cleaner, especially if you have many modules in the package

It also allows your package to **hide internal modules**:

* Users of the package don’t need to know the folder structure; they just import the functions/classes you expose in `__init__.py`.

---

### **3. `__init__.py` can also contain actual initialization code**

Sometimes, a package needs setup when it’s imported:

```python
# __init__.py
print("Loading my_package...")
VERSION = "0.1"
```

Then:

```python
import my_package
print(my_package.VERSION)  # 0.1
```

So `__init__.py` is **not just for imports**, it can also **run package-level code**.

---

### **4. Best practice**

* If your package has many modules, **use `__init__.py` to define the public API**.
* Keep internal functions or helper modules hidden by **not importing them in `__init__.py`**.
* Avoid heavy computation in `__init__.py` — just setup and imports.

---

 **Summary**

| Option                   | How import looks                                   | Notes                                            |
| ------------------------ | -------------------------------------------------- | ------------------------------------------------ |
| Empty `__init__.py`      | `from my_package.module1 import greet`             | Package exists, but imports still need full path |
| Imports in `__init__.py` | `from my_package import greet`                     | Cleaner imports, hides folder structure          |
| Initialization code      | `import my_package` triggers code in `__init__.py` | Can set constants, configure package             |







<br><br><br><br><br><br><br><br><br><br><br><br><br><br>




# 🟦 **PART 1 — How to make your own Python package**

A **Python package** is just a folder with an `__init__.py` file.

Example:

```
my_project/
    pyproject.toml    OR    setup.py
    module_nn/
        __init__.py
        model_builder.py
        engine.py
        data_setup.py
```

Where:

* `my_project` → root of your project
* `module_nn` → the actual package
* `__init__.py` → makes Python treat the folder as a package

Your `__init__.py` might contain:

```python
from .model_builder import TinyVGG
from .engine import train_step
from .data_setup import create_dataloaders
```

This allows:

```python
from module_nn import TinyVGG
```

Instead of:

```python
from module_nn.model_builder import TinyVGG
```

<br><br><br>

2.Add a `setup.py` file in your package root:

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
)
```

<br><br><br>



# 🟦 **PART 2 — How to install your package properly**

Navigate to your project root:

```bash
cd /path/to/my_project


cd "/Users/benjaminbrooke/PycharmProjects/Python_PyTroch/PyTorch for Deep Learning Bootcamp - Udemy/Section 7 - PyTorch Going Modular/Package Module"
```

Then run:

```bash
pip install -e .
```

This installs the package in **editable mode** — meaning:

* It does **not** copy files.
* It creates an **egg-link** that points to your folder.
* Python can now import your module from *anywhere*.

After this, you can open **any notebook, anywhere on your system** and write:

```python
from module_nn import TinyVGG
```

It works globally.

---

# 🟦 **PART 3 — How this compares to using `sys.path.append()`**

## 🔹 What `sys.path.append()` does

Example:

```python
import sys
sys.path.append("/Users/ben/module_nn")
from model_builder import TinyVGG
```

This temporarily adds a folder to Python’s import search path.

Python looks for modules in:

```
sys.path = [
    current_working_directory,
    system site-packages,
    virtual environment site-packages,
    anything added via sys.path.append(),
]
```

So `sys.path.append()`:

* Only works **while your script/notebook is running**
* Only affects **that one environment/session**
* Is **not permanent**
* Must be repeated in every notebook or project

It is basically a "hack" or temp fix.

---

# 🟥 **PART 4 — MAJOR DIFFERENCES (real talk)**

| Feature                                  | `pip install -e .` | `sys.path.append()`         |
| ---------------------------------------- | ------------------ | --------------------------- |
| **Permanent import path**                | ✔ Yes              | ❌ No                        |
| **Works everywhere**                     | ✔ Yes              | ❌ Only in that script       |
| **Professional practice**                | ✔ Standard         | ❌ Avoid in real projects    |
| **Allows versioning**                    | ✔ Yes              | ❌ No                        |
| **Editable updates reflect immediately** | ✔ Yes              | ✔ Yes                       |
| **No need to modify code each time**     | ✔ Yes              | ❌ Must repeat in every file |
| **Works for deployment**                 | ✔ Yes              | ❌ No                        |
| **Works in Jupyter without hacks**       | ✔ Yes              | ❌ Must append manually      |
| **Uses Python packaging system**         | ✔ Yes              | ❌ No                        |
| **Good for large multi-module projects** | ✔ Yes              | ❌ No                        |
| **Easy collaboration**                   | ✔ Yes              | ❌ No                        |

### 🔥 Final verdict:

* `sys.path.append()` → **quick hack, temporary fix**
* `pip install -e .` → **proper, scalable, professional solution**

---

# 🟦 **PART 5 — When to use each**

## ✔ Use `pip install -e .` when:

* You are building a real multi-module project
* You have multiple `.py` files and classes
* You want clean imports
* You want it to work from any directory
* You want PyCharm, VSCode, Jupyter to auto-complete imports
* You want a reusable library (like `torchvision` or `sklearn`)

This is the **industry-standard approach**.

---

## ✔ Use `sys.path.append()` only when:

* You are experimenting in a quick notebook
* You don’t want to create a package
* You are doing rapid prototyping
* You don’t care about clean structure
* You need a fast one-off fix

It’s not scalable and doesn’t belong in real projects.

---

# 🟦 **PART 6 — Why packaging is better**

Think of it this way:

### `sys.path.append()`

You manually shout:

> “Hey Python, also look over there!”

Every time, in every notebook, forever.

---

### `pip install -e .`

You give Python a permanent map:

> “This is a library. Here’s where it lives. Always load it from here.”

This is how real libraries are made.

---

# 🟦 **PART 7 — Where your package is stored**

When using:

```bash
pip install -e .
```

**Your package stays in your project directory.**
Python saves *only* a tiny `.egg-link` file in `site-packages` that points to it.

Nothing is copied.
Everything updates instantly.
Imports work everywhere.

---

# 🟦 **PART 8 — TL;DR Summary**

## How packaging works

* Make a folder
* Add `__init__.py`
* Add your modules
* Run `pip install -e .`

## Why it’s better than `sys.path.append()`

* No hacks
* Permanent
* Cleaner
* Works everywhere
* Real development workflow

## When to use `sys.path.append()`

* Quick experiments
* Not for real code

---

If you want, I can also:

✔ check your folder structure
✔ help you write a clean `pyproject.toml`
✔ show how to make **subpackages** like:

```
module_nn/models/
module_nn/utils/
module_nn/train/
```


