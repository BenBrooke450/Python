

from typing import Optional

# Definition for singly-linked list.
class listNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[listNode]) -> Optional[listNode]:
        dummy = listNode(0)  # Temporary start node
        tail = dummy
        total = 0
        curr = head
        first = 1
        while curr:
            if curr.val == 0 and first != 1:
                tail.next = listNode(total)  # Copy the node
                tail = tail.next
                total = 0
            else:
                total = total + curr.val
            curr = curr.next
            first = 0

        return dummy.next
