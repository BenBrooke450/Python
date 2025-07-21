

"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.



Example 1:
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

"""


def partitionString(s: str) -> int:

    list_temp = ""
    letters = []

    for x in s:
        if x in list_temp:
            letters.append(list_temp)
            list_temp = ""
            list_temp = list_temp + x
        else:
            list_temp = list_temp + x
    letters.append(list_temp)

    return letters


print(partitionString("abacaba"))

print(partitionString("ssssss"))







