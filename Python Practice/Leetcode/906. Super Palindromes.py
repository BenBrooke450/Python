
"""
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].



Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1

"""


def superpalindromesInRange(left: str, right: str) -> int:

    num_str = (x ** 0.5 for x in range(int(left), int(right) + 1) if str(x) == str(x)[::-1] and x ** 0.5 % 1 == 0)

    i = 0

    for x in num_str:
        x = str(x)
        if x == x[::-1]:
            i = i + 1

    return i

print(superpalindromesInRange(left = "4", right = "1000"))





