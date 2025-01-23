"""
You're given strings jewels representing
the types of stones that are jewels,
and stones representing the stones you
have. Each character in stones is a type
of stone you have. You want to know how
many of the stones you have are also jewels.

Letters are case sensitive, so "a" is
considered a different type of stone from "A".



Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0


"""


def stones(jewels: str , stones: str):

    dictionary = {}
    n = 0
    jewelry = [x for x in stones if x in jewels]
    for letters in jewelry:
        if letters not in dictionary:
            dictionary[letters] = 1
        else:
            dictionary[letters] = dictionary.get(letters) + 1

    return sum(dictionary.values())


print(stones("aA","aAAbbbb"))
#3