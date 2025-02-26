
"""

Given two strings s and t, return true if t is an
anagram
 of s, and false otherwise.



Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s: str, t: str) -> bool:
    t = ([x for x in t])
    s = ([x for x in s])
    t.sort()
    s.sort()
    "".join(s)
    "".join(t)
    if t == s:
        return True
    return False

print(isAnagram(s = "anagram", t = "nagaram"))

print(isAnagram(s = "rat", t = "cat"))






