
"""
You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.



Example 1:
Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation:
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
The odd array out is [1, 1], so we return the corresponding string, "abc".


Example 2:
Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].


"""


### OPTIMIZED

from collections import Counter
import numpy as np


def oddString(words: list[str]) -> str:
    # Compute difference patterns for each word
    diffs = []
    for word in words:
        values = [ord(c) - ord('a') for c in word]
        diffs.append(tuple(np.diff(values)))

    # Count patterns and find the unique one
    freq = Counter(diffs)
    odd_pattern = next(pattern for pattern, count in freq.items() if count == 1)

    # Return the word with that unique pattern
    return words[diffs.index(odd_pattern)]

### OPTIMIZED





import numpy as np
def oddString(words: list[str]) -> str:

    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    dic_alphabet = {x: i for i,x in enumerate(alphabet)}

    list2 = []
    list1 = []
    for i,x in enumerate(words):
        for y in x:
            list2.append(dic_alphabet[y])
            if len(list2) == len(words[0]):
                q = tuple(np.diff(list2))
                list1.append(q)
                if set(list1) == 2 and i > 2:
                    break
                list2 = []


    return words[next(i for i, tup in enumerate(list1) if list1.count(tup) == 1)]


print(oddString(["adc","wzy","abc"]))









