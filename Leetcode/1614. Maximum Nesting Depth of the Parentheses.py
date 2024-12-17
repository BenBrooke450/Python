

"""
Given a valid parentheses string s,
return the nesting depth of s.
The nesting depth is the maximum number of nested parentheses.



Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3


"""

def func(string:str):

    n = 0
    m = 0
    list1 = []

    for items in string:

        if items == "(":
            n = n + 1
            if n > m:
                m = n

        elif items == ")":
            n = n - 1

    return m


print(func("()(())((()()))"))



















