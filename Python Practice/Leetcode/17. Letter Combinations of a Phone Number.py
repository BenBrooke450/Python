
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

"""

from itertools import combinations,permutations



def letterCombinations(digits: str) -> list[str]:

    tele = {"2":['a', 'b', 'c'], "3":['d', 'e', 'f'], "4":['g', 'h', 'i'], "5":['j', 'k', 'l'], "6":['m', 'n', 'o'], "7":['p', 'q', 'r','s'], "8": ['t', 'u', 'v'], "9": ['w','x','y','z']}

    list1 = []

    for x in digits:
        list1.append(tele[x])

    print(list1)

    list2 = []
    start = list1[0]
    i = 0

    def loop(numbers : list[list[str]],list2,start:list[str],i):

        for x in start:
            for y in list1[1 + i]:
                if i == 0 :
                    list2.append([x,y])
                else:
                    list3 = []
                    list3.extend(x)
                    list3.extend(y)
                    list2.append(list3)

        if i + 2 < len(list1):
            start = list2
            list2 = []
            last = loop(list1,list2,start, i+1)
            return last

        return list2

    return ["".join(x) for x in loop(list1,list2,start,i)]


print(letterCombinations("232"))

