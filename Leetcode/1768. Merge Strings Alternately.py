

"""
You are given two strings word1 and word2. Merge the strings by
    adding letters in alternating order, starting with word1. If
     a string is longer than the other, append the additional
      letters onto the end of the merged string.

Return the merged string.



Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

"""

from itertools import zip_longest


def alter(word1: str, word2: str):

    list2 = []
    z = [z for z in word1]
    q = [q for q in word2]

    for x,y in zip_longest(z,q):
        if x is None:
            list2.append(y)
        elif y is None:
            list2.append(x)
        else:
            list2.append(x)
            list2.append(y)

    return "".join(list2)


print(alter(word1 = "abc", word2 = "pqr"))
#apbqcr


print(alter(word1 = "abrs", word2 = "pq"))







