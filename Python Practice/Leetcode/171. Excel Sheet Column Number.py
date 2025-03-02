

"""
Given a string columnTitle that represents the column title
    as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

"""



def titleToNumber(columnTitle: str) -> int:
    x = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
         'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
         'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
         'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
         'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    q = 0

    for i, n in enumerate(columnTitle):
        if i + 1 == len(columnTitle):
            q = x.get(n) + q
        else:
            q = x.get(n) * (26 ** (len(columnTitle) - i - 1)) + q
    return q

print(titleToNumber("FXSHRXW"))



















