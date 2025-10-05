
# Working with Linked Lists in Python

You can create a new linked list by copying or selectively adding elements from an existing linked list. This is a common pattern when you want to:

- Filter or transform the data
- Remove certain nodes
- Clone the list
- Build a new one with added logic

---

## Example: Create a new linked list from another

Let's assume you already have a basic `ListNode` class like this:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
````

---

### Using `ListNode` in a function

```python
# Example: mergeTwoLists function
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Implementation would merge two sorted linked lists
    # This is called like:
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))
    mergeTwoLists(list1, list2)
```

> Notes:
>
> * `list1: ListNode` → function expects a non-empty linked list (cannot pass `None`)
> * `list1: Optional[ListNode]` → function can handle an empty list (`None`) or a normal linked list (`ListNode`)

---

## Example 1: Copy elements to a new list

```python
def copy_linked_list(head):
    if not head:
        return None
    
    dummy = ListNode(0)  # Temporary start node
    tail = dummy
    current = head
    
    while current:
        tail.next = ListNode(current.val)  # Copy the node
        tail = tail.next
        current = current.next
    
    return dummy.next  # Returns the copied list, excluding the dummy
```

---

## Full Example: Building, merging, and converting linked lists

```python
from typing import Optional

# Definition for singly-linked list
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def build_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Temporary start node
        tail = dummy
        total = 0
        curr = head
        first = 1  # Skip the first zero
        
        while curr:
            if curr.val == 0 and first != 1:
                tail.next = ListNode(total)  # Add accumulated sum as new node
                tail = tail.next
                total = 0
            else:
                total += curr.val
            curr = curr.next
            first = 0

        return dummy.next

# Example usage
sol = Solution()
x = [0,3,1,0,4,5,2,0]
y = sol.build_linked_list(x)
z = sol.mergeNodes(y)
print(sol.to_list(z))
# Output: [4, 11]
```

---

### Explanation

1. **`build_linked_list`**: Converts a Python list into a linked list.
2. **`to_list`**: Converts a linked list back into a Python list for easy inspection.
3. **`mergeNodes`**: Traverses a linked list, sums values between zeros, and creates a **new linked list** with the sums.
4. **`dummy` node**: Helps simplify adding new nodes without special cases for the head.

