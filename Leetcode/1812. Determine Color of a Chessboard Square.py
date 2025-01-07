

"""
You are given coordinates, a string that represents the
        coordinates of a square of the chessboard. Below is a chessboard for your reference.



Return true if the square is white, and false if the square is black.


The coordinate will always represent a valid chessboard square.
        The coordinate will always have the letter first, and the number second.



Example 1:
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:
Input: coordinates = "c7"
Output: false

"""







def squareIsWhite(coordinates: str) -> bool:

    n = [1,2,3,4,5,6,7,8]
    l = ["a","b","c","d","e","f","g","h"]
    i = [True,False,True,False,True,False,True,False]

    dict1 = dict()
    g = 0
    for t in l:
        if g % 2 == 0:
            g = g + 1
            for p,y in zip(i[::-1],n):
                dict1[t + str(y)] = p

        else:
            g = g + 1
            for p,y in zip(i,n):
                dict1[t + str(y)] = p

    return dict1.get(coordinates)



print(squareIsWhite("a1"))
#False

"""{'a1': False, 'a2': True, 'a3': False, 'a4': True, 'a5': 
    False, 'a6': True, 'a7': False, 'a8': True, 'b1': True, 
    'b2': False, 'b3': True, 'b4': False, 'b5': True, 'b6': False, 
    'b7': True, 'b8': False, 'c1': False, 'c2': True, 'c3': False, 
    'c4': True, 'c5': False, 'c6': True, 'c7': False, 'c8': True, 
    'd1': True, 'd2': False, 'd3': True, 'd4': False, 'd5': True, 
    'd6': False, 'd7': True, 'd8': False, 'e1': False, 'e2': True, 
    'e3': False, 'e4': True, 'e5': False, 'e6': True, 'e7': False, 
    'e8': True, 'f1': True, 'f2': False, 'f3': True, 'f4': False, 
    'f5': True, 'f6': False, 'f7': True, 'f8': False, 'g1': False, 
    'g2': True, 'g3': False, 'g4': True, 'g5': False, 'g6': True, 
    'g7': False, 'g8': True, 'h1': True, 'h2': False, 'h3': True, 
    'h4': False, 'h5': True, 'h6': False, 'h7': True, 'h8': False}"""



