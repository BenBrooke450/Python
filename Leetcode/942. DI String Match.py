

"""
A permutation perm of n + 1 integers of
    all the integers in the range [0, n]
     can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the
    permutation perm and return it.
    If there are multiple valid permutations
     perm, return any of them.



Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]

"""
from IPython.utils.text import list_strings

from itertools import zip_longest

def diStringMatch(s: str):

    list1 = []
    length = len(s)
    m = 0

    for n in s:
        print(n)
        if n == "I":
            list1.append(m)
            m = m + 1
            pass
        elif n == "D":
            list1.append(length)
            length = length - 1

    list1.append(m)
    return list1


print(diStringMatch("IDID"))
#[0, 4, 1, 3, 2]















