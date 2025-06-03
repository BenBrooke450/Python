

"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

"""

from typing import Optional
# Definition for singly-linked list.

import numpy as np

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

    def to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def pairSum(self, head: Optional[ListNode]) -> int:

        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        result = np.array(result)
        l = len(result)-1
        t = 0
        q = 0
        while t < l:
            s = result[t] + result[l]
            print(s,result[t],result[l])
            if s > q:
                q = s
            t = t+1
            l = l-1
        return q



sol = Solution()

x = [5,4,3,4,2,1]

y = sol.build_linked_list(x)

print(sol.pairSum(y))
"""
6 5 1
6 4 2
7 3 4
7
"""

















from typing import Optional
# Definition for singly-linked list.

import numpy as np

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

    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        list1 = []
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next

        array1 = np.array(list1)

        array_split = np.array_split(array1,k)

        y = [x.tolist() for x in array_split]

        return y


head = [1,2,3]
k = 5

sol = Solution()

x = sol.build_linked_list(head)

print(sol.splitListToParts(x,k))
#[[1], [2], [3], [], []]