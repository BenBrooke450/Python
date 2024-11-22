

"""

Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""


Explanation: There is no common prefix among the input strings."""
from numpy.core.defchararray import startswith









def prefix(string: list[str]):

    n = 1

    first_word = min(string, key=len)

    for word in string:
        if word.startswith(first_word,0,len(first_word)):
            pass

        else:
            for letters in first_word:
                first_word = first_word[:-n]
                length = len(first_word)
                if first_word == word[0:length]:
                    break
                else:
                    n = + 1
    return first_word


print(prefix(["flower","flow","flight"]))
print(prefix(["reflower","flow","flight"]))

print(prefix(["flower","flow","flight"]))

print(prefix(["s","s","s"]))

print(prefix(["swapppppp","s","s"]))

print(prefix(["swap","hap","clap"]))




####################################################################





alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

strs = ["flower", "flow", "flight"]


def prefix(string: list[str]):

    dic1 = {}

    i = 0

    for letters in string:
        smallest_sofar = len(letters)
        next_string = len(string[i+1])
        if smallest_sofar < next_string:
            smaller = smallest_sofar
        else:
            smaller = next_string



    print(smaller)



print(prefix(strs))



####################################################################




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z']

strs = ["flower","flow","flight"]

def prefix(string : list[str]):

    dic1 = {}

    i = 0

    for letters in string:
        print(letters)


        for letter in letters:

            if letter in dic1:
                dic1[letter] = i + 1


            elif letter not in dic1:
                dic1[letter] = 1

        i = i + 1

    return dic1

print(prefix(strs))




####################################################################


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z']

strs = ["flower","flow","flight"]

def prefix(string : list[str]):

    dic1 = {}

    for letters in string:
        print(letters)

        for letter in letters:

            if letter in dic1:
                dic1[letter] += 1

            elif letter not in dic1:
                dic1[letter] = 1

    return dic1

print(prefix(strs))







