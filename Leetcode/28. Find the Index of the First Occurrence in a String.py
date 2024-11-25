

"""

Given two strings needle and haystack, return the index
of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.



Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""


def finy(text,word):
     if word in text:
         a = text.find(word)
         return a
     else:
         return -1





text = "iamsosadbutsad"
word = "sad"

print(finy(text,word))
5


text2 = "caallll"
word2 = "all"

print(finy(text2,word2))
2






####################################################################


if "sad" in "mysadlife":
    print(True)


def finy(text,word):


    if word in text:
        text = text.split(word,1)
        print(text)



text = "sadbutsad"
word = "sad"


finy(text,word)
#['', 'butsad']








