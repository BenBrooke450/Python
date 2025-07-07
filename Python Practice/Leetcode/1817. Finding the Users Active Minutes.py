
"""
You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

Return the array answer as described above.

"""


def findingUsersActiveMinutes(logs: list[list[int]], k: int) -> list[int]:

    dict1 = dict()
    for x in logs:
        if x[0] not in dict1.keys():
            dict1[x[0]] = [x[1]]
        else:
            dict1[x[0]].append(x[1])

    list1 = [x*0 for x in range(k)]

    for x in dict1.values():
        t = len(set(x))
        list1[t - 1] = list1[t - 1] + 1

    return list1

print(findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))












