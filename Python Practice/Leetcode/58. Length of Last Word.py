"""
Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.


Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.


Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.


Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

word = "   fly me   to   the moon  "

def last_word(word):
    word = word.split(" ")
    list1 = []
    for space in word:
        if len(space) > 0:
            list1.append(space)

    return len(list1[-1])



print(last_word(word))


#############################################################

word = "   fly me   to   the moon  "

def last_word(word):
    word = word.split(" ")
    i = 0
    while i < len(word):
        if word[i] == "":
            del word[i]
        i = i + 1
    print(word)


last_word(word)
#['', 'fly', 'me', '', 'to', '', 'the', 'moon', '']


#############################################################


word = "   fly me   to   the moon  "

def last_word(word):
    word = word.strip()
    print(word)


last_word(word)
#fly me   to   the moon

