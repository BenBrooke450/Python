

"""

Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:
Input: s = "aba"
Output: true


Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.


Example 3:
Input: s = "abc"
Output: false


"""


def validPalindrome(string: str) -> bool:
    for index in range(len(string)):
        modified_string = string[:index] + string[index + 1:]
        if modified_string == modified_string[::-1]:
            return True

    return False

print(validPalindrome("aababaa"))
#True



#################################################



def pan(string:str):

    x = list(string)

    for index, letters in enumerate(x):
        x[index] = ""
        x = "".join(x)
        if x[::-1] == x:
            return True
        else:
            x = list(string)
    return False



print(pan("aababaa"))
#True








