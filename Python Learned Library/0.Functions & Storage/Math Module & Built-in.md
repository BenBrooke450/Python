

##  **1. Basic Arithmetic Operators**

These are the **core built-in operators** (no import needed).

| Operator | Description         | Example  | Output |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `3 + 2`  | `5`    |
| `-`      | Subtraction         | `5 - 2`  | `3`    |
| `*`      | Multiplication      | `3 * 4`  | `12`   |
| `/`      | Division (float)    | `7 / 2`  | `3.5`  |
| `//`     | Floor Division      | `7 // 2` | `3`    |
| `%`      | Modulus (remainder) | `7 % 2`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |

---

##  **2. Built-in Numeric Functions**

(No import required — work directly in Python.)

| Function        | Description                           | Example             | Output   |
| --------------- | ------------------------------------- | ------------------- | -------- |
| `abs(x)`        | Absolute value                        | `abs(-5)`           | `5`      |
| `pow(x, y)`     | Power of `x` to `y`                   | `pow(2, 3)`         | `8`      |
| `round(x, n)`   | Rounds `x` to `n` decimal places      | `round(3.14159, 2)` | `3.14`   |
| `divmod(x, y)`  | Returns tuple `(quotient, remainder)` | `divmod(7, 3)`      | `(2, 1)` |
| `sum(iterable)` | Sum of iterable elements              | `sum([1,2,3])`      | `6`      |
| `min(iterable)` | Smallest value                        | `min([5,1,7])`      | `1`      |
| `max(iterable)` | Largest value                         | `max([5,1,7])`      | `7`      |

---

##  **3. `math` Module Functions**

(Need to `import math`)

```python
import math
```

| Function              | Description                 | Example                    | Output  |
| --------------------- | --------------------------- | -------------------------- | ------- |
| `math.sqrt(x)`        | Square root                 | `math.sqrt(16)`            | `4.0`   |
| `math.factorial(x)`   | Factorial                   | `math.factorial(5)`        | `120`   |
| `math.exp(x)`         | eˣ (exponential)            | `math.exp(2)`              | `7.389` |
| `math.log(x)`         | Natural log (base e)        | `math.log(10)`             | `2.302` |
| `math.log10(x)`       | Log base 10                 | `math.log10(100)`          | `2`     |
| `math.log2(x)`        | Log base 2                  | `math.log2(8)`             | `3`     |
| `math.ceil(x)`        | Rounds up                   | `math.ceil(4.1)`           | `5`     |
| `math.floor(x)`       | Rounds down                 | `math.floor(4.9)`          | `4`     |
| `math.trunc(x)`       | Truncates decimal part      | `math.trunc(3.9)`          | `3`     |
| `math.fabs(x)`        | Absolute (float)            | `math.fabs(-7.2)`          | `7.2`   |
| `math.copysign(x, y)` | Copies sign from `y` to `x` | `math.copysign(5, -2)`     | `-5.0`  |
| `math.isfinite(x)`    | Checks if finite            | `math.isfinite(5)`         | `True`  |
| `math.isinf(x)`       | Checks if infinite          | `math.isinf(float('inf'))` | `True`  |
| `math.isnan(x)`       | Checks for NaN              | `math.isnan(float('nan'))` | `True`  |

---

##  **4. Trigonometric Functions**

(Also from `math` module)

| Function           | Description               | Example                 | Output    |
| ------------------ | ------------------------- | ----------------------- | --------- |
| `math.sin(x)`      | Sine                      | `math.sin(math.pi/2)`   | `1.0`     |
| `math.cos(x)`      | Cosine                    | `math.cos(0)`           | `1.0`     |
| `math.tan(x)`      | Tangent                   | `math.tan(math.pi/4)`   | `1.0`     |
| `math.asin(x)`     | Inverse sine              | `math.asin(1)`          | `1.5708`  |
| `math.acos(x)`     | Inverse cosine            | `math.acos(0)`          | `1.5708`  |
| `math.atan(x)`     | Inverse tangent           | `math.atan(1)`          | `0.785`   |
| `math.degrees(x)`  | Convert radians → degrees | `math.degrees(math.pi)` | `180.0`   |
| `math.radians(x)`  | Convert degrees → radians | `math.radians(180)`     | `3.14159` |
| `math.hypot(x, y)` | √(x² + y²)                | `math.hypot(3,4)`       | `5.0`     |

---

##  **5. Constants**

| Constant   | Description           | Example    |
| ---------- | --------------------- | ---------- |
| `math.pi`  | π = 3.141592653589793 | `math.pi`  |
| `math.e`   | e = 2.718281828459045 | `math.e`   |
| `math.tau` | τ = 2π                | `math.tau` |
| `math.inf` | Infinity              | `math.inf` |
| `math.nan` | Not a Number          | `math.nan` |

