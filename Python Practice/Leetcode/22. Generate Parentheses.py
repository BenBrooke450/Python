
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
    list1 = []
    for y in com_strings:
        t = 0
        for i in range(len(y)):
            print(i,t)
            if y[i] == ")":
                t = t - 1
                if t < 0:
                    break

                elif i + 1 == len(y) and t == 0:
                    list1.append(y)

            elif y[i] == "(":
                t = t + 1
                if i + 1 == len(y) and t == 0:
                    list1.append(y)
    return list1









    return com_strings

print(generateParenthesis(3))




