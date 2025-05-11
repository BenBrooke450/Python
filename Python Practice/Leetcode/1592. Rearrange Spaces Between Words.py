
"""
You are given a string text of words that are placed among some
    number of spaces. Each word consists of one or more lowercase
     English letters and are separated by at least one space.
      It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces
    between every pair of adjacent words and that number is maximized.
     If you cannot redistribute all the spaces equally, place the extra
      spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.



Example 1:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words.
    We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.

Example 2:
Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words.
    7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.

"""


def reorderSpaces(text: str) -> str:
    spaces = sum(1 for x in text if x == " ")
    words = sum(1 for x in text.split(" ") if x != "")

    if spaces == 0 or words == 1:
        return text.strip() + spaces * " "

    text =  [x for x in text.strip()]


    if spaces % (words-1) == 0:
        number  = spaces / (words-1)
        remain = 0
    elif spaces % (words-1) != 0:
        remain =  spaces % (words-1)
        number = (spaces - remain) / (words-1)

    print(text,number)

    f = 0
    t = 0
    while t < len(text):
        print(text)
        if text[t] ==  " ":
            f = f + 1
            if f > number:
                text.pop(t)
            else:
                t = t + 1
        elif text[t] !=  " ":
            if f > 0 and f < number:
                text.insert(t," ")
                f = f + 1
            elif f >= number:
                f = 0
            else:
                t = t + 1

    return "".join(text) + " "*remain


print(reorderSpaces("a b   c d"))







