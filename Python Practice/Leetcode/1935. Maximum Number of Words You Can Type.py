
"""
There is a malfunctioning keyboard where some letter keys
    do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space
    (no leading or trailing spaces) and a string brokenLetters
     of all distinct letter keys that are broken, return the number
      of words in text you can fully type using this keyboard.



Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
Example 3:

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.

"""


def canBeTypedWords(text: str, brokenLetters: str) -> int:
    text = text.split(" ")
    brokenLetters = [x for x in brokenLetters]
    c = 0
    for word in text:
        n = 0
        for x in brokenLetters:
            if x in word:
                break
            elif (len(brokenLetters) - 1) == n:
                c = c + 1
            n = n + 1

    if len(brokenLetters) == 0:
        return len(text)

    return c


print(canBeTypedWords(text = "hello world", brokenLetters = "ad"))



