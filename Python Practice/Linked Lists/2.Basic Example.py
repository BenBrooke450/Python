

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
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def double(self):
        # First, check that there are at least two nodes
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        if count < 2:
            raise ValueError("Not enough nodes to process")

        # Now loop through and double every even-positioned node
        index = 0
        current = self.head
        while current:
            if index % 2 == 0:
                current.data *= 2
            current = current.next
            index += 1

    # Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)

ll.print_list()
#10 → 20 → 30 → 10 → 20 → 30 → 40 → 50 → 60 → None

ll.double()
ll.print_list()
#20 → 20 → 60 → 10 → 40 → 30 → 80 → 50 → 120 → None
























# Define a Linked List
class LinkedList2:
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

    # Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")







