


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val       # overwrite current node’s value
        node.next = node.next.next




##### INCORRECT
class Solution:

    def linked_list(self, values):

        if not values:
            return None

        head = ListNode(values[0])
        current = head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
            print(current.val)

        self.head = head
        return head


    def deleteNode(self, node):

        current = self.head
        prev = None

        while current:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            break
            prev = current
            current = current.next
        return current


sol = Solution()

list_sol = sol.linked_list([1,2,3,4,5])

print(list_sol)

sol.deleteNode(3)


##### incorrect



