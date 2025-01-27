
"""
You are given an integer array nums containing positive integers.
    We define a function encrypt such that encrypt(x) replaces
     every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

Return the sum of encrypted elements.



Example 1:
Input: nums = [1,2,3]
Output: 6
Explanation: The encrypted elements are [1,2,3].
    The sum of encrypted elements is 1 + 2 + 3 == 6.

Example 2:
Input: nums = [10,21,31]
Output: 66
Explanation: The encrypted elements are [11,22,33].
    The sum of encrypted elements is 11 + 22 + 33 == 66.
"""


def sumOfEncryptedInt(nums: list[int]) -> int:
    m = 0
    for n in nums:
        if len(str(n)) > 1:
            h = max(int(x) for x in str(n))
            m = int(str(h)*len(str(n))) + m
        else:
            m = n + m
    return m

print(sumOfEncryptedInt([1,2,3,10]))
#17













