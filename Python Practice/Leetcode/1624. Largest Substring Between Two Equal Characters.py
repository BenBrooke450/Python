

"""
Given a string s, return the length of the longest substring
    between two equal characters, excluding the two characters
     If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.



Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

"""


def maxLengthBetweenEqualCharacters(s: str) -> int:
    m = 0
    reverse_s = s[::-1]

    for i, l in enumerate(s):
        x = reverse_s.find(l)
        position = (len(s) - 1) - x
        if i == position:
            pass
        else:
            if position - i > m:
                m = position - i
    if m == 0:
        return -1
    return m - 1

print(maxLengthBetweenEqualCharacters("abca"))






