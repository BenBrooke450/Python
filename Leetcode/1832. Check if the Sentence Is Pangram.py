


"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


"""




def alpa(string:str):

    list3 = ['a', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'i',
             'j', 'k', 'l', 'm', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r',
             'r', 's', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z']

    for letters in list3:
        if letters in string:
            pass
        else:
            return False
    return True


print(alpa("thequickbrownfoxjumpsoverthelazydog"))
#True

