"""

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.



Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

"""


def findRelativeRanks(list1: list[int]):
    list2 = [0 for _ in range(len(list1))]

    i = 1
    for numbers in list1:

        max_value = max(list1)

        index_max = list1.index(max_value)

        list2[index_max] = str(i)

        list1[index_max] = -1

        i = i + 1

        if list2[index_max] == "1":
            list2[index_max] = "Gold Medal"
        elif list2[index_max] == "2":
            list2[index_max] = "Silver Medal"
        elif list2[index_max] == "3":
            list2[index_max] = "Bronze Medal"
    return list2


print(findRelativeRanks([5,4,3,2,1]))

print(findRelativeRanks([10,3,8,9,4]))








#################################################



def func(list1:list[int]):

    for index, numbers in enumerate(sorted(list1,reverse=True)):
        if index == 0:
            list1[index] = "Gold Medal"
        elif index == 1:
            list1[index] = "Bronze Medal"
        elif index == 2:
            list1[index] = "Silver Medal"
        else:
            list1[index] = index + 1

    return list1

print(func([5,4,3,2,1]))
#['Gold Medal', 'Bronze Medal', 'Silver Medal', 4, 5]

print(func([10,3,8,9,4]))




print(list(range(9999)))





