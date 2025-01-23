"""



Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

"""
from collections import Counter

from sympy import false

text = "[[(())]]"
text2 = "[[(("
text3 = "[[)(]]"
text4 = "()}{{}"
text10 = "[]]]"
text5 = "[[()()]{}]"
text6 = "[[()()]{{]"
text7 = "({)(})"


#############################################################


def bracket(texts: str):

    odd = [x for x in range(1, 10000) if x % 2 != 0]

    text = [x for x in texts]

    if len(text) in odd:
        return False


    else:

        i = 0
        while i < (len(text) - 1):
            if text[i] == "[" and (text[i + 1] == "}" or text[i + 1] == ")"):
                return False
            elif text[i] == "(" and (text[i + 1] == "}" or text[i + 1] == "]"):
                return False
            elif text[i] == "{" and (text[i + 1] == "]" or text[i + 1] == ")"):
                return False
            i = i + 1




        for index, bra in enumerate(text):

            if bra == "(":
                for index2, opp_bra in enumerate(text):
                    num1 = index
                    num2 = index2
                    if opp_bra == ")" and num1 < num2 and (((num2-1) - num1) not in odd):
                        text[index] = ""
                        text[index2] = ""
                        break


            elif bra == "[":
                for index3, opp_bra in enumerate(text):
                    num1 = index
                    num2 = index3
                    if opp_bra == "]" and num1 < num2 and (((num2-1) - num1) not in odd):
                        text[index] = ""
                        text[index3] = ""
                        break


            elif bra == "{":
                for index4, opp_bra in enumerate(text):
                    num1 = index
                    num2 = index4
                    if opp_bra == "}" and (num1 < num2) and (((num2-1) - num1) not in odd):
                        text[index] = ""
                        text[index4] = ""
                        break

        if len("".join(text)) == 0:
            return True

        else:
            return False


print(bracket(text))


