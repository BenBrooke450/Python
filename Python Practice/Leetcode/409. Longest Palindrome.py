

"""
Given a string s which consists of lowercase
    or uppercase letters, return the length
    of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example,
 "Aa" is not considered a palindrome.



Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""


def longestPalindrome(s: str) -> int:

    counts_letters = [s.count(x) for x in set(s)]
    even = sum([x for x in counts_letters if x % 2 == 0])
    odd = [x-1 for x in counts_letters if x % 2 != 0]
    print(even,odd)
    if 1 in counts_letters:
        return even + sum(odd) + 1
    else:
        if any(x % 2 == 0 and x > 1 for x in odd):
            return even + sum(odd) + 1
        else:
            return even + sum(odd)


print(longestPalindrome("DaDaD"))















