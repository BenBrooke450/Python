


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def linked_list(self, values):

        if not values:
            return None

        head = ListNode(values[0])
        current = head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


    def deleteNode(self, node):

        dummy = ListNode(0)

        while dummy:
            if dummy == node:
                print(current.data, end=" → ")

            current = current.next


sol = Solution()

list_sol = sol.linked_list([1,2,3,4,5])

print(list_sol)

sol.deleteNode(3)



