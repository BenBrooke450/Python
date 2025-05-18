

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between
    a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.

Each unique word in s maps to exactly one letter in pattern.

No two letters map to the same word, and no two words map to the same letter.


Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".


Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

"""

def wordPattern(pattern: str, s: str) -> bool:
    pattern = [x for x in pattern]
    s = s.split(" ")
    if len(s) != len(pattern):
        return False
    dict1 = dict()
    for x, y in zip(pattern, s):
        if x not in dict1.keys() and y not in dict1.values():
            dict1[x] = y
        elif x not in dict1.keys() and y in dict1.values():
            return False
        elif x in dict1.keys() and y not in dict1.values():
            return False
        elif x in dict1.keys() and y in dict1.values():
            if dict1.get(x) != y:
                return False
    return True



print(pattern,s)

print(wordPattern(pattern = "abba", s = "dog cat cat fish"))







