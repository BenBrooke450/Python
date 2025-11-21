# **1️⃣ Basic syntax**

```python
from PIL import Image

img = Image.open(fp, mode='r', formats=None)
```

* `fp` → File path (string), file object, or byte stream
* `mode` → Optional, mostly `'r'` for read
* `formats` → Optional, list/tuple of format strings (e.g., `["PNG", "JPEG"]`) to restrict formats

Returns an **`Image.Image` object** representing the image.

---

# **2️⃣ Parameters explained**

| Parameter | Type               | Default | Purpose                                                                  |
| --------- | ------------------ | ------- | ------------------------------------------------------------------------ |
| `fp`      | str or file object | —       | Path to the image file, or a file-like object (supports `.read()`)       |
| `mode`    | str                | `'r'`   | Open mode; `'r'` = read. Other modes (rare) are for plugins like `'r+b'` |
| `formats` | list/tuple of str  | None    | Optional: limit the formats Pillow will accept                           |

**Example restricting formats:**

```python
img = Image.open("example.png", formats=["PNG"])
```

* If the file is not PNG, it will raise an `OSError`.

---

# **3️⃣ Lazy loading**

* `Image.open()` **does not read the image into memory immediately**.

* It only **reads the file header** to determine:

  * image size
  * color mode
  * format

* The actual pixel data is loaded **on demand** (e.g., when you call `.load()`, `.show()`, or convert to NumPy array).

```python
img = Image.open("example.png")
print(img.size)   # Works immediately
pixels = img.load()  # Loads pixel data now
```

* This makes `Image.open()` **memory-efficient**, especially for large images.

---

# **4️⃣ Important attributes of the returned Image object**

Once you call `Image.open()`, you get an `Image.Image` object. Key attributes include:

| Attribute                | Description                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `img.size`               | Tuple `(width, height)` of the image                                    |
| `img.mode`               | Color mode (`'1'`, `'L'`, `'RGB'`, `'RGBA'`, `'CMYK'`, etc.)            |
| `img.format`             | String of original file format (`'PNG'`, `'JPEG'`, etc.)                |
| `img.format_description` | Human-readable format name, e.g., `'Portable network graphics'`         |
| `img.info`               | Dictionary of image metadata (e.g., PNG compression, DPI, transparency) |
| `img.getbands()`         | Tuple of channel names, e.g., `('R','G','B')`                           |
| `img.palette`            | Color palette info if the image is paletted (like `'P'` mode)           |
| `img.n_frames`           | Number of frames (for multi-frame formats like GIF or TIFF)             |
| `img.is_animated`        | True/False for animated images (GIF, WebP)                              |
| `img.fp`                 | Internal file pointer (useful for debugging)                            |

---

# **5️⃣ Common methods often used after `open()`**

| Method              | Purpose                                |
| ------------------- | -------------------------------------- |
| `img.load()`        | Force loading pixel data into memory   |
| `img.show()`        | Opens the image in default viewer      |
| `img.convert(mode)` | Convert to another mode (RGB, L, etc.) |
| `img.resize((w,h))` | Resize image                           |
| `np.array(img)`     | Convert image to NumPy array           |

---

# **6️⃣ Modes explained**

* `'1'` → 1-bit pixels, black and white
* `'L'` → 8-bit grayscale
* `'P'` → 8-bit paletted
* `'RGB'` → True color, 3 channels
* `'RGBA'` → RGB + alpha
* `'CMYK'` → For printing

Use `img.mode` to check and `img.convert("RGB")` if needed.

---

# **7️⃣ Format and metadata**

```python
img.format        # 'PNG'
img.format_description  # 'Portable Network Graphics'
img.info          # {'dpi': (72, 72), 'gamma': 0.45455}
```

* Metadata varies by format (PNG, JPEG, TIFF, etc.)
* Useful for DPI, transparency, color profiles.

---

# **8️⃣ Multi-frame / animated images**

Some formats support multiple frames:

```python
img = Image.open("animation.gif")
print(img.n_frames)      # number of frames
print(img.is_animated)   # True
```

* You can iterate through frames:

```python
for frame in range(img.n_frames):
    img.seek(frame)
    frame_img = img.copy()
```

---

# **9️⃣ Common pitfalls**

1. **Forgetting to close the file**

```python
img = Image.open("example.png")
img.close()  # optional if using context manager
```

Better:

```python
with Image.open("example.png") as img:
    img.load()
```

2. **Image not fully loaded**

* If you try `np.array(img)` without `.load()`, it will force loading anyway.

3. **Mode mismatch for ML**

* Ensure image is `RGB` or `L` before feeding into models:

```python
img = img.convert("RGB")
```

4. **Large images**

* Pillow is lazy-loading, so big PNGs are efficient until you process them.

---

# **🔟 Example Usage**

```python
from PIL import Image
import numpy as np

# Open image
img = Image.open("example.png")

# Inspect
print(img.size, img.mode, img.format)

# Convert to RGB
img = img.convert("RGB")

# Convert to NumPy
arr = np.array(img)
print(arr.shape)  # (height, width, 3)

# Show
img.show()
```

---

# ✅ **Summary of `.open()`**

* **Purpose:** Open an image file and return a `PIL.Image.Image` object.
* **Lazy loading:** Only reads header info; pixels loaded when needed.
* **Attributes to know:**

  * `.size`, `.mode`, `.format`, `.format_description`, `.info`, `.n_frames`, `.is_animated`
* **Common follow-ups:** `.convert()`, `.resize()`, `.thumbnail()`, `np.array()`, `.show()`

