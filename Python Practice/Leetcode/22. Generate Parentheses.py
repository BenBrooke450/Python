
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

"""

def generateParenthesis(n: int) -> list[str]:
    result = []

    def backtrack(current, open_count, close_count):
        # Base case: valid combination
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add an open parenthesis if we still can
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        # Add a close parenthesis if it won’t break validity
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    # Start the recursion
    backtrack("", 0, 0)
    return result

print(generateParenthesis(2))









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


print(generateParenthesis(2))




