

"""
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.



Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

"""

def clearDigits(s: str) -> str:
    list1 = []
    for n in s:
        if n.isalpha():
            list1.append(n)
        else:
            list1.pop()
    return "".join(list1)



print(clearDigits("cb34"))











