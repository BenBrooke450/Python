
"""
You are given a string s of lowercase English letters and
    an array widths denoting how many pixels wide each
    lowercase English letter is. Specifically, widths[0]
     is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where
    each line is no longer than 100 pixels. Starting
     at the beginning of s, write as many letters on
      the first line such that the total width does
       not exceed 100 pixels. Then, from where you
        stopped in s, continue writing as many letters
         as you can on the second line. Continue this
          process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.


Example 1:

Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,
                    10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.



Example 2:
Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,
                    10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
Output: [2,4]
Explanation: You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.


Constraints:

widths.length == 26
2 <= widths[i] <= 10
1 <= s.length <= 1000
s contains only lowercase English letters.
"""


def numberOfLines(widths: list[int], s: str) -> list[int]:

    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
        'x', 'y', 'z')

    n = 0
    c = 0

    dict1 = dict()

    for x,y in zip(alphabet,widths):
        dict1[x] = y

    for i,letter in enumerate(s):
        n = dict1.get(letter) + n
        if n > 100:
            n = 0
            n = dict1.get(letter) + n
            c = c + 1

        elif n == 100  and len(s) - 1 != i:
            n = 0
            c = c + 1
    if n > 0:
        c = c + 1

    return c



print(numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,
                    10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))
#2


print(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,
                     10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"))
#3

