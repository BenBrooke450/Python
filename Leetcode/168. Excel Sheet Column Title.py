


"""

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"


"""
from string import ascii_lowercase, ascii_uppercase

num = 2147483647

print(2147483647/26)

def excel(number : int):



    zip(range(1,2147483647),)

    alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
                8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
                14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
                20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',26:'Z'}

    #lets create a new diction for big numbers



    if number < 27:
        return alphabet.get(number)

    elif number >= 27:

        interation_below = number // 26

        if number % 26 == 0:
            interation_over = 26

        else:
            interation_over = number % 26
            print(interation_over)

    print(alphabet.get(interation_below),alphabet.get(interation_over))


print(excel(27))





al = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]



print(ascii_uppercase)

print(ascii_lowercase)
print(ascii_uppercase)


uppercase_alphabet = ''.join(chr(i) for i in range(ord('A'), ord("Z") + 1))

print(ord("B"))

print(chr(66))

print(uppercase_alphabet)








