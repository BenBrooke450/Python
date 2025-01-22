

"""
Given a string paragraph and a string array of the banned words banned,
    return the most frequent word that is not banned. It is guaranteed
     there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.



Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

"""


import re

def mostCommonWord(paragraph: str, banned: list[str]) -> str:

    paragraph = re.split(r'[^\w]+', paragraph.lower())
    #paragraph = ("".join(x.lower() for x in paragraph if x.isalpha() or x == " ")).split(" ")

    dict1 = dict()
    for x in set(paragraph):
        if (len(banned) > 0 and x in banned) or len(x) == 0:
            continue
        else:
            dict1[x] = paragraph.count(x)

    return max(dict1, key = dict1.get)


print(mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))

print(mostCommonWord("  I'm     i'''''m !?',;.  ''M  im",""))