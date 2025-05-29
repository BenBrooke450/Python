"""
2807. Insert Greatest Common Divisors in Linked List
Medium
Topics
premium lock icon
Companies
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""
import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

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
            gcd = math.gcd(curr.val, prev.val)
            new_node = ListNode(gcd)
            new_node.next = curr.next
            prev = new_node.next
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

    def print_list_external(self, my_list):
        current = head
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("None")





sol = Solution()

input_list = [18, 6, 10, 3]

head = sol.build_linked_list(input_list)

second_head = sol.insertGreatestCommonDivisors(head)

sol.print_list_external(second_head)


