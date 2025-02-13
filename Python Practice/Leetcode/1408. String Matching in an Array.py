
"""
Given an array of string words, return all strings
    in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string



Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
"""


def stringMatching(words: list[str]) -> list[str]:

    words.sort(key = lambda x: len(x))
    print(words)
    list1 = []

    for i in range(len(words) - 1):
        if any(word for word in words if words[i] in word and words[i] != word):
            list1.append(words[i])
    return list1

print(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))










