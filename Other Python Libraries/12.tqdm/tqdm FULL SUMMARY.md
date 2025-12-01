

# ⭐ What is `tqdm`?

`tqdm` is a Python library that wraps any iterable (list, dataloader, generator, etc.) and displays a **live progress bar** showing how fast it is iterating.

It stands for:

> **“taqaddum” (Arabic for progress), or “taqaddum” (Persian for progress)”**
> and
> **“progress meter” in general.**

---

# ⭐ Minimal example

```python
from tqdm import tqdm

for i in tqdm(range(100)):
    pass
```

This prints something like:

```
100%|██████████| 100/100 [00:01<00:00, 92.21it/s]
```

---

# ⭐ What each part of the bar means

Take this typical tqdm output:

```
Epoch 1:  45%|███████▏      | 43/96 [00:10<00:12, loss=0.98]
```

Breakdown:

### ✔ 1. **Epoch 1:**

This is the **`desc="..."` text** you passed.

### ✔ 2. **45%**

Percent of total iterations completed.

### ✔ 3. **|███████▏      |**

The block-shaped progress bar.

### ✔ 4. **43/96**

* `43` → iterations completed
* `96` → total iterations

### ✔ 5. **[00:10<00:12, ...]**

The metadata section (time).

Inside the brackets:

| Part        | Meaning                              |
| ----------- | ------------------------------------ |
| `00:10`     | Time spent so far (elapsed)          |
| `<00:12`    | Estimated time remaining (ETA)       |
| `loss=0.98` | Postfix values (your custom metrics) |

---

# ⭐ `set_postfix()` — adding live metrics

You update the displayed values like this:

```python
loop.set_postfix(loss=loss.item(), acc=accuracy)
```

Output:

```
Epoch 3:  12%|███▌        | 12/96 [00:05<00:40, loss=0.83, acc=92.1]
```

**`set_postfix()` is the standard way to show loss and accuracy while training.**

---

# ⭐ tqdm in different environments

### ✔ Terminal

Uses ANSI escape codes → modifies the line in-place.

### ✔ Jupyter Notebook (including PyCharm’s notebook mode)

`tqdm` cannot update the terminal line, so you must use:

```python
from tqdm.notebook import tqdm
```

This uses **HTML widgets**, which update in-place inside a notebook.

### ✔ Auto version

Works in both environments:

```python
from tqdm.auto import tqdm
```

---

# ⭐ Full API — important arguments

```python
tqdm(iterable=None, 
     total=None,
     desc=None,
     position=0,
     leave=True,
     dynamic_ncols=True,
     smoothing=0.3)
```

### ✔ `iterable`

What you are looping over.

Example: `train_loader`.

### ✔ `total`

Total # of iterations (optional, inferred automatically if iterable has length).

### ✔ `desc`

Text at the front ("Epoch 1").

### ✔ `position`

Used for **multiple bars**.
`position=0`, `position=1` keeps bars stacked.

### ✔ `leave=True`

When finished:

* `True`: leave bar printed
* `False`: remove bar after completion (cleaner logs)

### ✔ `dynamic_ncols=True`

Automatically resize bar length → prevents weird wrapping.

### ✔ `smoothing`

Controls smoothing of the ETA:

* `0.0` → jittery ETA
* `1.0` → smooth but inaccurate
* default = `0.3` (best)

---

# ⭐ tqdm in ML training — best practice pattern

### ✔ Most used structure in deep learning:

```python
from tqdm.notebook import tqdm

for epoch in range(num_epochs):
    print(f"\nEpoch {epoch+1}/{num_epochs}")

    batch_bar = tqdm(train_loader, desc=f"Epoch {epoch+1}", leave=True)

    for images, labels in batch_bar:
        loss = ...

        batch_bar.set_postfix(loss=loss.item())
```

Why this structure?

* Ensures **one clean bar per epoch**
* Avoids duplicated output
* Jupyter-compatible
* Easy postfix updates

---

# ⭐ Nested progress bars (epoch + batch)

```python
from tqdm.notebook import tqdm

epoch_bar = tqdm(range(num_epochs), desc="Epochs")

for epoch in epoch_bar:
    iteration_bar = tqdm(train_loader, desc=f"Epoch {epoch+1}", leave=False)

    for images, labels in batch_bar:
        loss = ...
        iteration_bar.set_postfix(loss=loss.item())
```

This produces:

```
Epochs:  10%|██▍         | 1/10
Epoch 2:  █████▊         | 54/96 [loss=0.84]
```

---

# ⭐ How tqdm displays ETA

ETA is computed by:

```
eta = (elapsed / completed) * (total - completed)
```

Smoothed using an exponential moving average.

---

# ⭐ Performance impact

`tqdm` is extremely lightweight.
Overhead per iteration: **~1 µs** (one microsecond).

Even in deep learning, the computation dominates; tqdm is negligible.

---

# ⭐ Summary (the clean master summary)

`tqdm` is a fast, flexible progress bar that:

* wraps any iterable
* shows % completion, iteration count, ETA
* supports Jupyter with `tqdm.notebook`
* supports nested bars
* allows live metrics via `set_postfix()`
* is the standard for ML training progress
* is nearly zero overhead
* auto-computes times and updates the bar efficiently

It is the **go-to tool** for tracking training in PyTorch.




# Example 1

## Put the train_loader into the tqdm function

```python
from torch.utils.tensorboard import SummaryWriter
from tqdm.notebook import tqdm

writer = SummaryWriter()

epochs = 1

step = 0

for epoch in tqdm(range(epochs),desc="Epochs"):

    model_one.train()

    running_loss = 0
    train_loader = tqdm(train_loader, desc=f"Epoch [{epoch+1}/{epochs}]", leave=True)

    for X_train, y_train in train_loader:

        optimizer.zero_grad()

        y_pred = model_one(X_train)

        loss = loss_fn(y_pred, y_train)

        loss.backward()

        optimizer.step()


        preds = y_pred.argmax(dim=1)
        acc = (preds == y_train).float().mean().item()

        writer.add_scalar("Loss/train", loss.item(), step)
        writer.add_scalar("Accuracy/train", acc, step)

        step = step + 1


        train_loader.set_postfix(loss=loss.item(), acc=acc)

```