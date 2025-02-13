
"""
You are given two strings, coordinate1 and coordinate2,
    representing the coordinates of a square on an 8 x 8 chessboard.

Below is the chessboard for reference.



Return true if these two squares have the same color and false otherwise.

The coordinate will always represent a valid chessboard square.
    The coordinate will always have the letter first
    (indicating its column), and the number second (indicating its row).



Example 1:
Input: coordinate1 = "a1", coordinate2 = "c3"
Output: true
Explanation:
Both squares are black.

Example 2:
Input: coordinate1 = "a1", coordinate2 = "h3"
Output: false
Explanation:
Square "a1" is black and "h3" is white.


"""


def checkTwoChessboards(coordinate1: str, coordinate2: str) -> bool:

    letters = ["a","b","c","d","e","f","g","h"]
    numbers = [1,2,3,4,5,6,7,8]
    chess = dict()

    for i,a in enumerate(letters):
        if i%2==0:
            n = 0
        else:
            n = 1
        for m in numbers:
            if n%2 == 0:
                chess[a + str(m)] = "Black"
                n = n + 1
            else:
                chess[a + str(m)] = "White"
                n = n + 1

    if chess.get(coordinate1) == chess.get(coordinate2):
        return True
    else:
        return False

print(checkTwoChessboards("a1","a3"))










