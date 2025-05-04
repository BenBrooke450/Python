
"""
You are given two 0-indexed integer arrays player1 and player2, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

Assume a player hits xi pins in the ith turn. The value of the ith turn for the player is:

2xi if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
Otherwise, it is xi.
The score of the player is the sum of the values of their n turns.

Return

1 if the score of player 1 is more than the score of player 2,
2 if the score of player 2 is more than the score of player 1, and
0 in case of a draw.


Example 1:

Input: player1 = [5,10,3,2], player2 = [6,5,7,3]

Output: 1

Explanation:

The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25.

The score of player 2 is 6 + 5 + 7 + 3 = 21.

Example 2:

Input: player1 = [3,5,7,6], player2 = [8,10,10,2]

Output: 2

Explanation:

The score of player 1 is 3 + 5 + 7 + 6 = 21.

The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.

Example 3:

Input: player1 = [2,3], player2 = [4,1]

Output: 0

Explanation:

The score of player1 is 2 + 3 = 5.

The score of player2 is 4 + 1 = 5.

Example 4:

Input: player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]

Output: 2

Explanation:

The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73.

The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.

"""


def isWinner(player1: list[int], player2: list[int]) -> int:
    t = 0
    d1 = 0
    d2 = 0
    p1 = 0
    p2 = 0
    while t < len(player1):
        if player1[t] == 10:
            if d1 > 0 and d1 < 3:
                p1 = player1[t]*2 + p1
                d1 = 1
            else:
                p1 = player1[t] + p1
                d1 = 1
        elif d1 > 0 and d1 < 3:
            d1 = d1 + 1
            p1 = player1[t] * 2 + p1
        else:
            p1 = player1[t] + p1
            d1 = 0

        if player2[t] == 10:
            if d2 > 0 and d2 < 3:
                p2 = player2[t] * 2 + p2
                d2 = 1
            else:
                p2 = player2[t] + p2
                d2 = 1
        elif d2 > 0 and d2 < 3:
            d2 = d2 + 1
            p2 = player2[t] * 2 + p2
        else:
            p2 = player2[t] + p2
            d2 = 0
        t = t + 1
        print("p1:",p1,"p2:",p2)

print(isWinner(player1 = [9,7,10,7], player2 = [10,2,4,10]))










