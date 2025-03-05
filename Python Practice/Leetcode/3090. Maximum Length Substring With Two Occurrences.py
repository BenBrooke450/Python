

"""
Given a string s, return the maximum length of a
    substring such that it contains at most two occurrences of each character.


Example 1:
Input: s = "bcbbbcba"
Output: 4
Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".


Example 2:
Input: s = "aaaa"
Output: 2
Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
"""


def maximumLengthSubstring(s: str) -> int:
    substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) > 1]
    print(substrings)
    t = 0
    for string in substrings:
        q = 1
        for n in set(s):
            if string.count(n) > 3:
                break
            elif len(string) > t and q == len(set(s)):
                t = len(string)
            else:
                q = q + 1
    return t

print(maximumLengthSubstring("bcbbbcba"))

print(maximumLengthSubstring("aaaa"))




















