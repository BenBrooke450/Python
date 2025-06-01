

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


x = [0,3,1,0,4,5,2,0]

sol = Solution()

sol