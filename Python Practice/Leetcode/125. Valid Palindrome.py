"""

A phrase is a palindrome if, after converting all
 uppercase letters into lowercase letters and removing
  all non-alphanumeric characters, it reads the same
  forward and backward. Alphanumeric characters include
  letters and numbers.

Given a string s, return true if it is a palindrome,
or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""


def letters(string):

     alpha =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"0",
               "1","2","3","4","5","6","7","8","9"]
     list1 = []

     string_split = [x.lower() for x in string if x.lower() in alpha]
     if "".join(string_split) == "".join(string_split[::-1]):
         return True
     else:
         return False



#print(letters("A man, a plan, a canal: Panama"))
print(letters("0P"))