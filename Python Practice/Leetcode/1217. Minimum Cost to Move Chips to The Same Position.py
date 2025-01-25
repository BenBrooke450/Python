

"""
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step,
    we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.



Example 1:
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.


Example 2:
Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2.
    Each move has cost = 1. The total cost = 2.

Example 3:
Input: position = [1,1000000000]
Output: 1
"""

def minCostToMoveChips(position: list[int]) -> int:
    n = 0
    list1 = []
    a = sum(position.count(x) for i, x in enumerate(set(position)) if x % 2 != 0)

    b = sum(position.count(x) for i, x in enumerate(set(position)) if x % 2 == 0)

    return min(a, b)

print(minCostToMoveChips([2,2,2,3,3,4,4,4,4,4,2,2,12]))

#####################################################

def minCostToMoveChips(position: list[int]) -> int:
    n = 0
    list1 = []

    count_positions = [position.count(x) for x in set(position)]

    print(count_positions)

    max_position = count_positions.index(max(count_positions))

    if max_position % 2 == 0:
        return sum(x for i,x in enumerate(count_positions) if i % 2 != 0)
    else:
        return sum(x for i,x in enumerate(count_positions) if i % 2 == 0)


print(minCostToMoveChips([2,2,2,3,3,4,4,4,4,4,2,2]))


###############################################


def minCostToMoveChips(position: list[int]) -> int:
    n = 0
    list1 = []
    for i,x in enumerate(position):
        if (i != len(position) - 1) and x == position[i+1]:
            n = n + 1
        else:
            list1.append(n + 1)
            n = 0

    max_position = list1.index(max(list1))

    if max_position % 2 == 0:
        return sum(x for x in list1 if max_position % 2 == 0)
    else:
        return sum(x for x in list1 if max_position % 2 != 0)




print(minCostToMoveChips([2,2,2,3,3,4,4,4,4,4,2,2]))






