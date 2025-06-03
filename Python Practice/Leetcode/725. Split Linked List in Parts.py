

"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.



Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

"""

from typing import Optional
# Definition for singly-linked list.

import numpy as np

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list1 = []
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next

        array1 = np.array(list1)

        array_split = np.array_split(array1,k)

        def list_to_linked_list(lst):
            if not lst:
                return None

            head = ListNode(lst[0])
            current = head
            for val in lst[1:]:
                current.next = ListNode(val)
                current = current.next
            return head
        return [list_to_linked_list(x.tolist()) for x in array_split]

















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











