
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]


"""

from itertools  import combinations,permutations
def generateParenthesis(n: int) -> list[str]:
    string = "("*n + n*")"
    com_strings = list(set("".join(x) for x in list(permutations(string))))
    for y in com_strings:
        for j in y:
            if j == ")":

    return com_strings

print(generateParenthesis(3))




