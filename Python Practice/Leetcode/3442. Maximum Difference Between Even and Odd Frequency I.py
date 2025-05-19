

"""
You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:

One of the characters has an even frequency in the string.

The other character has an odd frequency in the string.

Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency.



Example 1:
Input: s = "aaaaabbc"

Output: 3
Explanation:
The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.

Example 2:
Input: s = "abcabcab"
Output: 1
Explanation:
The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.

"""


def maxDifference(s: str) -> int:
    counts = [s.count(x) for x in set(s)]
    odd_max = max((x for x in counts if x % 2 != 0), key=lambda x: x)
    even_min = min((x for x in counts if x % 2 == 0), key=lambda x: x)
    return odd_max-even_min

print(maxDifference("aaaaabbccc"))






