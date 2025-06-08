
"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

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

    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode):

        array1 = np.array([])
        array2 = np.array([])

        curr_1 = list1
        curr_2 = list2

        # Process list1
        while curr_1:
            array1 = np.append(array1, curr_1.val)
            curr_1 = curr_1.next

        # Process list2
        while curr_2:
            array2 = np.append(array2, curr_2.val)
            curr_2 = curr_2.next

        return array1, array2

sol = Solution()

x = sol.build_linked_list([10,1,13,6,9,5])
y = sol.build_linked_list([1000000,1000001,1000002])

print(Solution.mergeInBetween(list1 = x, a = 3, b = 4, list2 = y))
#(array([10.,  1., 13.,  6.,  9.,  5.]), array([1000000., 1000001., 1000002.]))













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

    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode):

        array1 = []
        array2 = []

        curr_1 = list1
        curr_2 = list2

        # Process list1
        while curr_1:
            array1.append(curr_1.val)
            curr_1 = curr_1.next

        # Process list2
        while curr_2:
            array2.append(curr_2.val)
            curr_2 = curr_2.next

        new_list = array1[:a] + array2 + array1[b+1:]

        if not new_list:
            return None
        head = ListNode(new_list[0])
        current = head
        for val in new_list[1:]:
            current.next = ListNode(val)
            current = current.next

        return head


sol = Solution()

x = sol.build_linked_list([10,1,13,6,9,5])
y = sol.build_linked_list([1000000,1000001,1000002])

print(Solution.mergeInBetween(list1 = x, a = 3, b = 4, list2 = y))
#<__main__.ListNode object at 0x1048d4c80>







