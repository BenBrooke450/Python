
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
