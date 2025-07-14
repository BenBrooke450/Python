

"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.



Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

"""

from typing import Optional

import numpy as np


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = []
        current = head
        while current:
            result.append(str(current.val))
            current = current.next
        result = "".join(result)
        return int(result, 2)


node3 = ListNode(1)
node2 = ListNode(0, node3)
node1 = ListNode(1, node2)

sol = Solution()

print(sol.getDecimalValue(node1))







class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


node3 = ListNode(1)
node2 = ListNode(0, node3)
node1 = ListNode(1, node2)

sol = Solution()

print(sol.getDecimalValue(node1))
#[1, 0, 1]






x = 10
binary = bin(x)                   # '0b101'
stripped_binary = binary.lstrip('-0b')  # '101'
print(stripped_binary)           # '101'

stripped_binary = "1011101"
binary_str = str(stripped_binary)
x = int(binary_str, 2)
print(x)  # Output: 5
