

"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of
    vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:
Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:
Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:
Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

"""

#        if all(z in y for z in vowels):
#           t = max(y.count(z) for z in vowels) + t

import re

def countVowelSubstrings(word: str) -> int:

    vowels = ("a","e","o","u","i")
    list1 = [x if x in vowels else " " for x in word]
    list1 = (("".join(list1)).strip()).split(" ")
    p = 0
    for y in list1:
        q = [y[i:j] for i in range(len(y)) for j in range(i + 1, len(y) + 1)]
        for w in q:
            if all(z in w for z in vowels):
                p = p + 1

    return p

print(countVowelSubstrings("cuaieuoutac"))











