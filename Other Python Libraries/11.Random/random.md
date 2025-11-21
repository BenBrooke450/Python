
# **1️⃣ Purpose of the `random` module**

* The `random` module provides **pseudo-random number generation** in Python.
* Useful for:

  * Generating random numbers
  * Random selections from sequences
  * Random shuffling
  * Probabilistic simulations
  * Games, testing, ML data sampling, etc.

> **Note:** Python’s `random` module is **deterministic** if you use a seed — it generates reproducible “pseudo-random” numbers.

```python
import random
random.seed(42)  # reproducible results
```

---

# **2️⃣ Random number generation**

### `random.random()`

* Returns a **float between 0.0 and 1.0** (uniform distribution)

```python
import random
print(random.random())  # e.g., 0.6394267984578837
```

---

### `random.uniform(a, b)`

* Returns a **float between a and b** (inclusive of both ends)

```python
print(random.uniform(10, 20))  # e.g., 15.2345
```

---

### `random.randint(a, b)`

* Returns an **integer N such that a ≤ N ≤ b**

```python
print(random.randint(1, 6))  # like a dice roll
```

---

### `random.randrange(start, stop[, step])`

* Returns an **integer from a range** like `range(start, stop, step)`

```python
print(random.randrange(0, 10, 2))  # 0, 2, 4, 6, or 8
```

---

### `random.getrandbits(k)`

* Returns a **k-bit integer**

```python
print(random.getrandbits(8))  # 0-255
```

---

# **3️⃣ Random choices from sequences**

### `random.choice(seq)`

* Returns a **single random element** from a non-empty sequence

```python
colors = ["red", "green", "blue"]
print(random.choice(colors))
```

---

### `random.choices(population, weights=None, k=1)`

* Returns **k random elements** from population **with replacement**
* Optional `weights` for probability distribution

```python
print(random.choices(colors, weights=[0.1,0.1,0.8], k=5))
```

---

### `random.sample(population, k)`

* Returns **k unique elements** from population (no replacement)

```python
print(random.sample(range(10), 3))  # e.g., [2, 7, 5]
```

---

# **4️⃣ Shuffling sequences**

### `random.shuffle(x[, random])`

* Shuffles a list **in-place**

```python
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)  # e.g., [4,1,3,5,2]
```

* Returns `None`; modifies the list directly

---

# **5️⃣ Random distributions**

The module also supports **sampling from common statistical distributions**.

| Function                             | Description                       |
| ------------------------------------ | --------------------------------- |
| `random.betavariate(alpha, beta)`    | Beta distribution                 |
| `random.expovariate(lambd)`          | Exponential distribution          |
| `random.gammavariate(alpha, beta)`   | Gamma distribution                |
| `random.gauss(mu, sigma)`            | Gaussian / normal distribution    |
| `random.lognormvariate(mu, sigma)`   | Log-normal distribution           |
| `random.normalvariate(mu, sigma)`    | Normal distribution (like gauss)  |
| `random.vonmisesvariate(mu, kappa)`  | Von Mises distribution (circular) |
| `random.paretovariate(alpha)`        | Pareto distribution               |
| `random.weibullvariate(alpha, beta)` | Weibull distribution              |

**Example:**

```python
print(random.gauss(mu=0, sigma=1))  # sample from N(0,1)
```

---

# **6️⃣ Seeding**

* Pseudo-random means sequences **can be repeated** using a seed:

```python
random.seed(123)
print(random.randint(1,10))  # always same output if seed is same
```

* If you do **not** set a seed, Python uses system time or OS randomness.

---

# **7️⃣ Advanced: Random state / Generator**

* Python 3.9+ supports `random.Random()` objects for **independent generators**:

```python
rng = random.Random(42)  # independent generator
print(rng.randint(1,100))
```

* Useful if you want **reproducible but separate random streams**.

---

# **8️⃣ Quick examples for ML / Deep Learning**

```python
import random

# Shuffle dataset indices
indices = list(range(100))
random.shuffle(indices)

# Sample mini-batch
batch_indices = random.sample(indices, k=16)

# Random float for augmentation
flip_prob = random.random()
if flip_prob > 0.5:
    image = horizontal_flip(image)
```

---

# **9️⃣ Summary / Key Takeaways**

* `random` = pseudo-random numbers, selections, shuffling, and distributions
* **Deterministic if seeded**; reproducible
* Core functions:

  * `random()`, `uniform()`, `randint()`, `randrange()`, `getrandbits()`
  * `choice()`, `choices()`, `sample()`, `shuffle()`
  * Statistical: `gauss()`, `normalvariate()`, `expovariate()`, etc.
* Use `Random()` object if you want **independent streams**
* Does **not produce cryptographically secure randomness** — for that, use `secrets` module

