

"""

Given a string s, reverse the
order of characters in each word
 within a sentence while still
 preserving whitespace and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

"""


def func(string:str):
    split_string = string.split(" ")
    return " ".join(x[::-1] for x in split_string)


print(func("Let's take LeetCode contest"))
#s'teL ekat edoCteeL tsetnoc


