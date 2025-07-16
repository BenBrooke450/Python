



A linked list in Python is a linear data structure where elements (called nodes) are stored in separate objects, and each node points to the next node in the list.

Unlike Python’s built-in list, a linked list does not use contiguous memory. This makes inserting and deleting elements more efficient (especially in the middle), but slower to access elements by index.

[ data | next ] → [ data | next ] → [ data | None ]

 

 

 
```python
# Define a Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a Linked List

class LinkedList:
    def __init__(self):
        self.head = None

    # Add node to end
    def append(self, data):
        new_node = Node(data)
        if new_node not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

 

    # Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next

        print("None")

 ```


Variants:

Singly Linked List – each node points to next only

Doubly Linked List – each node has next and prev

Circular Linked List – last node points back to head
 

 

 

 

 

 

 
```python
# Define a Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# What is self.next = None?

"""
Because when we create a new node, it’s not yet connected to anything.
    It’s alone. By default, it doesn’t point to another node — so we set:
"""

node1 = Node(10)
print(node1.data)  # 10
print(node1.next)  # None → means there's no next node *yet*


# Can you set self.next to something else?

# Yes — once you're ready to connect it to another node.

node1 = Node(10)

node2 = Node(20)

node1.next = node2  # Now node1 points to node2

#Now the structure looks like:

"""
node1 → node2
 10       20
"""


#So when does self.next change from None?

#When you connect the node to the next one using something like:

node1.next = node2
```


<br><br><br> 

 

 
```python
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # points to next Node (if any)

That gives you a single "train carriage" — a node that can point to another node.

But a linked list is a whole train, not just a single carriage.

 That’s where the LinkedList class comes in.

"""

#The Node is just one piece of data + a pointer. It doesn't know about the whole list.

#The LinkedList class:

#Keeps track of the starting point (called the head).

#Knows how to add nodes, remove nodes, traverse the list, etc.

 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to next node (initially nothing)

class LinkedList:
    def __init__(self):
        self.head = None   # start of the list (nothing yet)

 

ll = LinkedList()         # create an empty linked list

ll.head = Node(10)        # add first node manually

ll.head.next = Node(20)   # link second node

#What does this line do?

ll.head.next = Node(20)

#Does it make 20 the new head?
#No! It just adds a new node after the current head.

"""head → [10] → [20] → None"""

"""
Head still points to 10.
10’s next points to 20.
20’s next is None.
"""

#ll.head = Node(10) Sets the head of the list to 10

#ll.head.next = Node(20)    Adds a node with 20 after the head

#ll.head = Node(99) Replaces the head entirely with a new node

 

#Part 1: append(self, data)
#This method adds a new node to the end of the linked list.
# Define a Linked List

class LinkedList:
    def __init__(self):
        self.head = None
    # Add node to end
    
    def append(self, data):
        
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        
        while last.next:
            last = last.next
        last.next = new_node

 

#This method adds a new node to the end of the linked list.

def append(self, data):
    new_node = Node(data)

#We create a new Node with the given data.

#It starts with next = None.

"""

if not self.head:
    self.head = new_node
    return

"""

#If the list is empty (self.head is None), then we make this new node the head.

#And we return right away — we're done!

 

 

"""last = self.head"""

#If the list isn’t empty, we start at the head and traverse the list.

 

while last.next:
    last = last.next

"""

This loop walks through the list until it finds the last node.

How? It checks if the current node has a next node.

If it does, we move last to the next node.

⛳ When last.next is None, we’ve found the last node.

"""

"""last.next = new_node"""

#We set the last node’s next to point to the new node.

#Now the new node is added to the end of the list.

 

 

 

 

 

 

 

 

 

# Part 2: print_list(self)

def print_list(self):
    current = self.head

#Start at the head node.

while current:
    print(current.data, end=" → ")
    current = current.next

"""

While we haven’t reached the end:

Print the current node's data.

Move to the next node.

"""

 

 

 

 

 

 

 

 

 

 

 

#Why do some methods have an extra parameter like data, while others just use self?

#def append(self, data):

#This method needs extra information — specifically, a new value (data) to add to the linked list.

#So you call it like:

ll.append(10)  # you're passing 10 to the 'data' parameter

#self refers to the linked list

#data is the value you're adding

 

 

 

 

#2 def print_list(self):

#This method does not need any extra information. It simply loops through the list and prints what's already there.

ll.print_list()

 
```


You can create a new linked list by copying or selectively
    adding elements from an existing linked list. 
        This is a common pattern when you want to:

Filter or transform the data, Remove certain nodes, Clone the list, or Build a new one with added logic.
 


Example: Create a new linked list from another

Let’s assume you already have a basic ListNode and LinkedList class like this:

 
<br><br>

# Example 1

### list1: ListNode → function expects a non-empty linked list (head node). Cannot pass None.

### list1: Optional[ListNode] → function can handle an empty list (None) or a regular linked list (ListNode).

 

 
```python

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Soltuion:        
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:

        #Then your function will be called by the test system with arguments like this:

        list1 = ListNode(1, ListNode(3, ListNode(5)))
        list2 = ListNode(2, ListNode(4, ListNode(6)))

        
mergeTwoLists(list1, list2)


#########################################################

# Example 1: Copy elements to a new list



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
    
        return dummy.next # this takes every node but the first missing the 0 you put

 

 

 

#########################################################

 

 

from typing import Optional

# Definition for singly-linked list.

 

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

 

    def to_list(self,head):
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

        first = 1

        while curr:

            if curr.val == 0 and first != 1:

                tail.next = ListNode(total)  # Copy the node

                tail = tail.next

                total = 0

            else:

                total = total + curr.val

            curr = curr.next

            first = 0

 

        return dummy.next

 

sol = Solution()

 

x = [0,3,1,0,4,5,2,0]

 

y = sol.build_linked_list(x)

 

z = sol.mergeNodes(y)

 

print(sol.to_list(z))

#[4, 11]

```

<br><br><br><br>

## def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

## What is head: Optional[ListNode]?

 - head: This is usually the head node of a singly linked list.

 - Optional[ListNode]: This means head can either be a ListNode or None. (Optional is a type hint from Python’s typing module.)


<br><br><br><br>


# Example 2

## Definition for singly-linked list.

```python
from typing import Optional

import numpy as np

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

 

    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode):

        array1 = np.array([])

        array2 = np.array([])

        curr_1 = list1

        curr_2 = list2


        # Process list1

        while curr_1:
            array1 = np.append(array1, curr_1.val)
            curr_1 = curr_1.next

        # Process list2

        while curr_2:
            array2 = np.append(array2, curr_2.val)
            curr_2 = curr_2.next
        return array1, array2

 

 

sol = Solution()

x = sol.build_linked_list([10,1,13,6,9,5])

y = sol.build_linked_list([1000000,1000001,1000002])

 

print(Solution.mergeInBetween(list1 = x, a = 3, b = 4, list2 = y))

#(array([10.,  1., 13.,  6.,  9.,  5.]), array([1000000., 1000001., 1000002.]))

```


<br><br><br><br>


# Example 3

## Definition for singly-linked list.


```python

from typing import Optional

import numpy as np

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = []
        current = head
        while current:
            result.append(str(current.val))
            current = current.next
        result = "".join(result)
        return int(result, 2)


node3 = ListNode(1)
node2 = ListNode(0, node3)
node1 = ListNode(1, node2)

sol = Solution()

print(sol.getDecimalValue(node1))
['1', '0', '1']
5










from typing import Optional

import numpy as np


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


node3 = ListNode(1)
node2 = ListNode(0, node3)
node1 = ListNode(1, node2)

sol = Solution()

print(sol.getDecimalValue(node1))
#[1, 0, 1]

```



