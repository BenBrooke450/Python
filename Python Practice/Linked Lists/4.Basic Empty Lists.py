
class Solution:
    def mergeNodes(self, head: Optional[listNode]) -> Optional[ListNode]:
        dummy = listNode(0)  # Temporary start node
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
