

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
























import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

    def print_list_external(self, head):
        current = head
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("None")

    def build_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

sol = Solution()

input_list = [18, 6, 10, 3]
head = sol.build_linked_list(input_list)
sol.print_list_external(head)
#18 → 6 → 10 → 3 → None











from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_2:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head
        print(curr.val, prev.val)
        while curr:
            print("At node:", curr.val)
            # Example logic:
            prev = curr
            curr = curr.next


    def build_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def print_list_external(self, head):
        current = head
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("None")




sol_2 = Solution_2()

input_list = [18, 6, 10, 3]
head = sol_2.build_linked_list(input_list)
sol_2.insertGreatestCommonDivisors(head)
"""
6 18
At node: 6
At node: 10
At node: 3
"""



















import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_3:
    def print_linked_list(self,head):
        current = head
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("None")

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head
        while curr:
            print(curr.val, prev.val)
            prev = curr
            curr = prev.next
            self.print_linked_list(head)
        return head

    def build_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


input_list = [18,6,10,3,20,30,21,34]
sol_3 = Solution_3()
head = sol_3.build_linked_list(input_list)
sol_3.insertGreatestCommonDivisors(head)
"""
6 18
18 → 6 → 10 → 3 → 20 → 30 → 21 → 34 → None
10 6
18 → 6 → 10 → 3 → 20 → 30 → 21 → 34 → None
3 10
18 → 6 → 10 → 3 → 20 → 30 → 21 → 34 → None
20 3
18 → 6 → 10 → 3 → 20 → 30 → 21 → 34 → None
30 20
18 → 6 → 10 → 3 → 20 → 30 → 21 → 34 → None
21 30
18 → 6 → 10 → 3 → 20 → 30 → 21 → 34 → None
34 21
18 → 6 → 10 → 3 → 20 → 30 → 21 → 34 → None
"""





