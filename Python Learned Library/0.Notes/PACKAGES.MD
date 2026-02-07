<br><br><br><br>

If you don't want to deal with `setup.py` or formal packaging, you can use a few "shortcuts" to tell Python where to look for your code. Python's import system primarily looks in the **Current Working Directory** and the **System Path (`sys.path`)**.

Here are the three most common ways to retrieve functions from another folder without building a package.

---

### **1. The "Standard Hack": `sys.path.append()**`

This is the most common method for quick projects. You manually add the folder containing your functions to the list of places Python looks for modules.

**Structure:**

```text
project/
├── folder_a/
│   └── functions.py  (contains def my_func()...)
└── folder_b/
    └── main.py       (wants to use my_func)

```

**In `main.py`:**

```python
import sys
import os

# 1. Get the absolute path to 'folder_a'
# This logic finds the parent directory and then points to folder_a
path_to_functions = os.path.abspath(os.path.join('..', 'folder_a'))

# 2. Add it to the system path
if path_to_functions not in sys.path:
    sys.path.append(path_to_functions)

# 3. Now you can import normally
from functions import my_func
my_func()

```

---

### **2. The "Terminal Way": `PYTHONPATH**`

If you don't want to put "path code" inside your Python files, you can tell your computer where your functions are before you run the script. This is great for keeping your code clean.

**On Windows (Command Prompt):**

```cmd
set PYTHONPATH=C:\path\to\your\folder_a
python folder_b\main.py

```

**On Mac/Linux:**

```bash
export PYTHONPATH="/path/to/your/folder_a"
python3 folder_b/main.py

```

*Now, `main.py` can simply call `import functions` as if it were in the same folder.*

---

### **3. The "Smart Way": Use `pathlib**`

Instead of the older `os` module, `pathlib` is more readable and handles "stepping up" out of folders more intuitively.

**In `main.py`:**

```python
import sys
from pathlib import Path

# Get the path of the current file, go up one level, then into 'folder_a'
folder_a_path = Path(__file__).resolve().parent.parent / "folder_a"

# Add to sys.path
sys.path.append(str(folder_a_path))

import functions

```

---

### **Which one should you use?**

| Method | Pros | Cons |
| --- | --- | --- |
| **`sys.path.append`** | Works immediately; very easy to understand. | Makes code messy with "hardcoded" paths. |
| **`PYTHONPATH`** | Keeps code clean; no extra lines of Python needed. | You have to remember to set it every time you open a new terminal. |
| **`pathlib`** | Best practice for modern Python; very reliable. | Slightly more complex syntax for beginners. |

---

### **Summary Table**

| Location of Functions | Code to add to `main.py` |
| --- | --- |
| **Child Folder** | `from child_folder.file import func` (No special code needed) |
| **Parent Folder** | `sys.path.append('..')` |
| **Sibling Folder** | `sys.path.append('../sibling_folder')` |

**Would you like me to show you how to set up a `.env` file so these paths are loaded automatically every time you start your project?**




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


