

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
        print("---- PASS THROUGH ----")
        if index == len(s):
            print("ADDED TO RESULT (NO CAP):  ",path)
            result.append("".join(path))
            return

        char = s[index]

        print("Path: ",path)

        path.append(char)
        backtrack(index + 1)
        path.pop()
        print("POP", char)
        print("AFTER POP:  ", path)

        if char.isalpha():
            print("IT'S A LETTER, it now passes the through:  ",char)
            path.append(char.swapcase())
            print("Added to the path:  ",char.swapcase())
            print("ADDED TO RESULT (CAP):  ", path)
            backtrack(index + 1)
            print("POP (CAP)", char.swapcase())
            path.pop()

    backtrack(0)
    return result


print(letterCasePermutation("a1b2"))















