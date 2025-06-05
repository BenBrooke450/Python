
"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

"""
from itertools import permutations
import numpy as np
def numTilePossibilities(tiles: str) -> int:
    list2 = ["".join(x) for x in permutations(tiles)]
    print(list2)
    list1 = []
    for i,x in enumerate(np.arange(len(list2))):
        tiles = list2[i]
        list1.extend(["".join(tiles[i:j]) for i in np.arange(len(tiles)) for j in np.arange(i+1, len(tiles)+2)])
    return len(set(list1))

print(numTilePossibilities("HT"))





