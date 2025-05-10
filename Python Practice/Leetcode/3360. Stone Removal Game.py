
"""
Alice and Bob are playing a game where they take turns removing stones from a pile,
    with Alice going first.

Alice starts by removing exactly 10 stones on her first turn.

For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.

The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.



Example 1:
Input: n = 12
Output: true
Explanation:
Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
Bob cannot remove 9 stones, so Alice wins.

Example 2:
Input: n = 1
Output: false
Explanation:
Alice cannot remove 10 stones, so Alice loses.


"""

def canAliceWin(n: int) -> bool:
    if (n - 10) < 0:
        return False
    elif n == 10:
        return True
    n = n - 10
    who = 0
    for x in range(9, -1, -1):
        print(n,x)
        n = n - x
        if n < 0 and who % 2 == 0:
            return True
        elif n < 0:
            return False
        who = who + 1



print(canAliceWin(34))



















