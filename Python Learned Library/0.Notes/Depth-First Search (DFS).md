



<br><br><br><br>

# Example 1

```python

def numIslands(grid):

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return

        visited.add((r, c))

        # Explore in all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:

                dfs(r, c)
                count += 1

    return count



print(numIslands(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))

```

<br>


<br>

### Step 1.0

Here we set up the dimensions of the matrix for use to loop through.

```python
rows, cols = len(grid), len(grid[0])

visited = set()
```




<br>


### Step 2.0

We move past this part for now as we haven't called the function.

```python
def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return

        visited.add((r, c))

        # Explore in all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
```


<br>


### Step 3.0

We begin to loop through the rows and columns of the matrix, when the first 1 appears we then enter the dfs(r, c) which begins the recursion

```python

count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:

                dfs(r, c)
                count += 1
```

<br>

### Step 3.1

We now enter the function.

```python

if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
    return
```

This top statement tells us if any of these conditions are met we **return** to the function below, BUT as we have just entered this statement it will never happen the first time.

```python
if grid[r][c] == 1 and (r, c) not in visited:
    dfs(r, c)
    count += 1
```


<br>

### Step 3.2

Now we check each space above and below, left and right as we are go further into the recursion.

Let's say that **dfs(r+1, c)** has found a 1, so then you renter the function.

```python

visited.add((r, c))

# Explore in all 4 directions
dfs(r+1, c)
dfs(r-1, c)
dfs(r, c+1)
dfs(r, c-1)
```

We then move back to this statement. This again check if we have met any of the conditions. If we do meet one of these conditions we return back to the previous space/area. 
 - BUT you have to remember if we then find a 0 below that 1, we return to the one and then move into the next **dfs(r-1, c)** and we work our way down the list of dfs

```python

if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
    return
```

<br>

### Step 3.3

Let's say we hit a 0 at (1,3) and we were on (1,2) we then **return** to (1,2), we move through the matrix.

dfs(r+1, c) we can´t go any further as there's a 0 at (1,3).

We move back a space to (1,2) BUT we move onto the next dfs which would be dfs(r-1, c).

dfs(r-1, c) we try to go back to (1,1) BUT **(r, c) in visited** so we move to the next one.

dfs(r, c+1)....

**IT CAN ONLY RETRACE ITS STEPS BY THE RETURN FUNCTION NOT BY THE FUNCTIONS BELOW, THE RETURN FUNCTION WILL PULL IT BACK TO WITHIN ITS SELF AND CAN ONLY BE DONE WHEN THERE´S NO WHERE ELSE LEFT TO GO**

```python
# Explore in all 4 directions
dfs(r+1, c)
dfs(r-1, c)
dfs(r, c+1)
dfs(r, c-1)
```

**Left, right, up and down, searching every part AND THEN IT PULLS/RETURNS IT-SELF TO THE BEGINNING AFTER IT CAN´T FIND ANYWHERE ELSE TO GO**

<br>

### Step 4

After every part of the island has been searched, it returns to dfs(r, c) the original function and counts +1 counting an island.

```python
if grid[r][c] == 1 and (r, c) not in visited:
    dfs(r, c)
    count += 1
```

And then after the count +1 the loop moves to the next **cols**, counting all the islands

```python

count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:

                dfs(r, c)
                count += 1
```




<br><br><br><br>

# Example 2


```python
def numIslands(grid):

    rows, cols = len(grid), len(grid[0])
    visited = set()
    q = 0
    list1 = []

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return 0

        visited.add((r, c))

        count = 1

        # Explore in all 4 directions
        count = count + dfs(r+1, c)  # down
        count = count + dfs(r-1, c)  # up
        count = count + dfs(r, c+1)  # right
        count = count + dfs(r, c-1)  # left

        return count

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                size = dfs(r, c)
                list1.append(size)

                if size > q:
                    q = size
                size = 0

    return list1, q
```


print(numIslands(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))












