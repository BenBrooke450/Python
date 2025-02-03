
"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.



Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

"""


def makeFancyString(s: str) -> str:

    list1 = []
    n = 0
    p = 0

    while n < len(s):
        if  n + 1 != len(s) and s[n] == s[n+1]:
            p = p + 1
            if p >= 2:
                n = n + 1
            else:
                list1.append(s[n])
                n = n + 1
        else:
            list1.append(s[n])
            n = n + 1
            p = 0

    return "".join(list1)

print(makeFancyString("leeetcode"))






