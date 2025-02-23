

"""
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.



Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.

Example 2:
Input: word = "abc"
Output: 0
Explanation:
No character in word appears in uppercase.

Example 3:
Input: word = "abBCab"
Output: 1
Explanation:
The only special character in word is 'b'.


"""


def numberOfSpecialChars(word: str) -> int:
    list1 = []
    for n in word:
        if n.islower():
            if n.upper() in word:
                list1.append(n.lower())
        elif n.isupper():
            if n.lower() in word:
                list1.append(n.lower())
    return len(set(list1))

print(numberOfSpecialChars(word = "aaAbcBC"))




