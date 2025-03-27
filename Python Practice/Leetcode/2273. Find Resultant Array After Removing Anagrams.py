

"""
You are given a 0-indexed string array words,
    where words[i] consists of lowercase English letters.

In one operation, select any index i such that
    0 < i < words.length and words[i - 1] and
    words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations.
    It can be shown that selecting the indices
     for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase using
     all the original letters exactly once.
      For example, "dacb" is an anagram of "abdc".



Example 1:
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.


Example 2:
Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are performed.


"""


def removeAnagrams(words: list[str]) -> list[str]:

    list1 = []
    i = 0
    t = 0
    while i + 1 != len(words):
        if sorted(words[i]) != sorted(words[i+1]):
            if t > 0:
                i = i + 1
                t = 0
                if i + 1 == len(words) and sorted(words[i-1]) != sorted(words[i]):
                    list1.append(words[i])
            else:
                list1.append(words[i])
                i = i + 1
                t = 0
                if i + 1 == len(words) and sorted(words[i-1]) != sorted(words[i]):
                    list1.append(words[i])
        elif sorted(words[i]) == sorted(words[i+1]) and t == 0:
            list1.append(words[i])
            i = i + 1
            t = t + 1
        else:
            i = i + 1
    if len(words)==1:
        return words
    else:
        return list1

print(removeAnagrams(["a","b","c","d","e"]))








#############################



def removeAnagrams(words: list[str]) -> list[str]:

    words_sorted =  ["".join(sorted(x)) for x in words]
    set1 = dict()
    for i,n in enumerate(words_sorted):
        if n not in set1.keys():
            set1[n] = words[i]
        else:
            pass

    return list(set1.values())

print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))








