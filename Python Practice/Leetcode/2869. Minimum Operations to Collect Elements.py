
"""
You are given an array nums of positive integers and an integer k.

In one operation, you can remove the last element of the array and add it to your collection.

Return the minimum number of operations needed to collect elements 1, 2, ..., k.



Example 1:
Input: nums = [3,1,5,4,2], k = 2
Output: 4
Explanation: After 4 operations, we collect elements 2, 4, 5, and 1, in this order.
    Our collection contains elements 1 and 2. Hence, the answer is 4.

Example 2:
Input: nums = [3,1,5,4,2], k = 5
Output: 5
Explanation: After 5 operations, we collect elements 2, 4, 5, 1, and 3, in this order.
 Our collection contains elements 1 through 5. Hence, the answer is 5.

"""


def minOperations(nums: list[int], k: int) -> int:
    nums = nums[::-1]
    numbers_needed = list(range(1, k + 1))
    list1 = set()
    for i, n in enumerate(nums):
        list1.add(n)
        if all(x in list1 for x in numbers_needed):
            return i + 1







