

"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear
    in both lower and upper cases, more than once.



Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

"""

import numpy as np


def reverseVowels(s: str) -> str:
    vowels = ["o", "u", "i", "e", "a","O", "U", "I", "E", "A"]
    loc_vowels = np.array([i for i,x in enumerate(s) if x in vowels])
    s = np.array([x for x in s])
    for x,y in zip(loc_vowels,loc_vowels[::-1]):
        if x < y:
            s[x],s[y] = s[y],s[x]
        else:
            break
    return "".join(s.tolist())


print(reverseVowels("leetcode"))









#####################################


import numpy as np


def reverseVowels(s: str) -> str:
    vowels = ["o", "u", "i", "e", "a","O", "U", "I", "E", "A"]
    vowel_list = np.array([x for x in s if x in vowels])[::-1]
    loc_vowels = np.array([i for i,x in enumerate(s) if x in vowels])
    s = np.array([x for x in s])
    for i,n in np.ndenumerate(s):
        if np.isin(i,loc_vowels):
            s[i] = vowel_list[0]
            vowel_list = vowel_list[1:]
    return "".join(s.tolist())

print(reverseVowels("leetcode"))




#####################################





def reverseVowels(s: str) -> str:

    vowels = ["o","u","i","e","a"]
    vowels_list = [x for x in s if x in vowels]
    rev_vowel_list = vowels_list[::-1]
    not_vowels = [" " if x in vowels else x for x in s]
    for i,n in enumerate(not_vowels):
        if n == " ":
            not_vowels[i] = vowels_list[0]
            vowels_list = vowels_list[1:]


