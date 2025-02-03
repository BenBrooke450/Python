

"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.



Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".

"""

def countWords(words1: list[str], words2: list[str]) -> int:

    m = 0

    for n in words1:
        if n in words2 and words1.count(n) == 1 and words2.count(n) == 1:
            m = m + 1
    return m

print(countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]))






