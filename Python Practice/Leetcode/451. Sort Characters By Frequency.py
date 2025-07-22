

"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""


def frequencySort(s: str) -> str:


    dict2 = {x: s.count(x) for x in s}

    items = dict2.items()

    # Sort the list of tuples based on the second element (the count)
    s = sorted(items, key=lambda x: x[1], reverse=True)

    s = "".join(x[0]*x[1]  for x in s)

    return s

print(frequencySort("tree"))
#eetr

print(frequencySort("trrreerrrroooooiifg"))
#rrrrrrroooooeeiitfg

print(frequencySort("trrreeEErrRRrroooooiifg"))

print(frequencySort("treeEtrrR"))














def frequencySort(s: str) -> str:

    s = [x for x in s]

    s = sorted(s, key= lambda x: s.count(x),reverse=True)

    return "".join(s)











