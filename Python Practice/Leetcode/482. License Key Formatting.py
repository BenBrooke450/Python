"""

You are given a license key represented as
a string s that consists of only alphanumeric
characters and dashes. The string is separated
into n + 1 groups by n dashes. You are also
given an integer k.

We want to reformat the string s such that
each group contains exactly k characters,
except for the first group, which could be
shorter than k but still must contain at least
 one character. Furthermore, there must be a
 dash inserted between two groups, and you
 should convert all lowercase letters to uppercase.

Return the reformatted license key.



Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split
into two parts, each part has 4 characters.
Note that the two extra dashes are not
needed and can be removed.




Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.


"""


def reformant(string: str, k: int):
    upper_joined_string = list(string.upper().replace("-",""))
    ujr = upper_joined_string[::-1]
    for index,letters in enumerate(ujr):
        if (index +1 ) % k == 0 and len(ujr) != (index +1):
            ujr[index] = "-" + letters
    return "".join(ujr[::-1])






print(reformant("5F3ZT-2e-9-w", 4))
#5-F3ZT-2E9W


###################################################

def reformant(string :str, k : int):

    upper_string = string.upper()
    i = 0
    list1 = []
    for digits in upper_string:
        if digits != "-":
            i = i + 1
        elif digits == "-":
            list1.append(i)
            i = 0


    return list1


print(reformant("5F3Z-2e-9-w",4))
#[4, 2, 1]
