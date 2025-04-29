
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
    by deleting some (can be none) of the characters without disturbing the relative
     positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
      while "aec" is not).



Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


"""

import numpy as np
def isSubsequence(s: str, t: str) -> bool:
    q = 0
    for i,x in enumerate(s):
        print(t)
        if x in t:
            if i >= q:
                t = t[t.index(x)+1:]
                q = i
                pass
            else:
                return False
        else:
            return False
    return True

print(isSubsequence(s = "abc", t = "ahcdfbgdc"))

















