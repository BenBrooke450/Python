

"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]


Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]


Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.

"""


def letterCasePermutation(s: str) -> list[str]:
    result = []
    path = []

    def backtrack(index: int):
        # Base case: we’ve built one full string
        if index == len(s):
            print("First Full (RETURN):  ",path)
            result.append("".join(path))
            return

        char = s[index]

        print("Path: ",path)

        # Case 1: use the character as is
        path.append(char)
        backtrack(index + 1)
        path.pop()
        print("AFTER POP:  ", path, "CHAR", char)

        # Case 2: if it’s a letter, toggle its case
        if char.isalpha():
            print("letter: ",char)
            path.append(char.swapcase())
            print("Second Full (RETURN):  ", path)
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return result


print(letterCasePermutation("a1b2"))















