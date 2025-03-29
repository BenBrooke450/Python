

"""
You have a water dispenser that can dispense cold,
    warm, and hot water. Every second, you can either
     fill up 2 cups with different types of water,
      or 1 cup of any type of water.

You are given a 0-indexed integer array
    amount of length 3 where amount[0],
     amount[1], and amount[2] denote the number of cold,
      warm, and hot water cups you need to fill
       respectively. Return the minimum number of
       seconds needed to fill up all the cups.



Example 1:
Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.


Example 2:
Input: amount = [5,4,4]
Output: 7
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.


Example 3:
Input: amount = [5,0,0]
Output: 5
Explanation: Every second, we fill up a cold cup.

"""


def fillCups(amount: list[int]) -> int:
    t = 0
    while sum(amount) != 0:
        print(amount)
        if all(x > 0 for x in amount):
            y = amount.index(max(amount))
            x = amount.index(min(amount))
            if x == y:
                amount = [x - 1 if x > 0 else 0 for x in amount]
                x = amount.index(min(amount))
                amount[y] = amount[y] + 1
                t = t + 1
                continue
            amount[y] = amount[y] - 1
            amount[x] = amount[x] - 1
            t = t + 1
        elif amount.count(0) == 1:
            amount = [x - 1 if x > 0 else 0 for x in amount]
            t = t + 1
        elif amount.count(0) == 2:
            amount = [x - 1 if x > 0 else 0 for x in amount]
            t = t + 1
    return t

print(fillCups([1,1,1]))




