

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

    def double(self,input_list):
        if not isinstance(input_list, LinkedList):
            raise TypeError("Input must be a LinkedList")


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

ll.print_list()
#10 → 20 → 30 → None
























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







