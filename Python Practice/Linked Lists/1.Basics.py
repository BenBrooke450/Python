
# Define a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ✅What is self.next = None?

"""
Because when we create a new node, it’s not yet connected to anything.
    It’s alone. By default, it doesn’t point to another node — so we set:
"""

node1 = Node(10)
print(node1.data)  # 10
print(node1.next)  # None → means there's no next node *yet*







# ✅Can you set self.next to something else?

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









"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # points to next Node (if any)
        
That gives you a single "train carriage" — a node that can point
 to another node.

But a linked list is a whole train, not just a single carriage.
 That’s where the LinkedList class comes in.
"""

#✅The Node is just one piece of data + a pointer. It doesn't know about the whole list.

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











#✅What does this line do?

ll.head.next = Node(20)

#Does it make 20 the new head?

#No! It just adds a new node after the current head.

"""head → [10] → [20] → None"""

"""
Head still points to 10.

10’s next points to 20.

20’s next is None.
"""

#ll.head = Node(10)	Sets the head of the list to 10

#ll.head.next = Node(20)	Adds a node with 20 after the head

#ll.head = Node(99)	Replaces the head entirely with a new node








#✅ Part 1: append(self, data)

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










#✅ Part 2: print_list(self)

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












#🎯Why do some methods have an extra parameter like data, while others just use self?

#1️⃣ def append(self, data):
#This method needs extra information — specifically, a new value (data) to add to the linked list.

#So you call it like:
ll.append(10)  # you're passing 10 to the 'data' parameter

#self refers to the linked list

#data is the value you're adding





#2️⃣ def print_list(self):
#This method does not need any extra information. It simply loops through the list and prints what's already there.
ll.print_list()




