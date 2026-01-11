
"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).



Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].


Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
"""


def countOdds(low: int, high: int) -> int:

    if low % 2 == 0:
        numbers = range(low+1, high+1, 2)

    else:
        numbers = range(low, high+1, 2)

    return numbers

print(countOdds(low = 3, high = 7))
print(countOdds(low = 8, high = 10))