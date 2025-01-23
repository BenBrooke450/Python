

"""
There are n rings and each ring is either red, green, or blue.
    The rings are distributed across ten rods labeled from 0 to 9.

You are given a string rings of length 2n that describes the n
    rings that are placed onto the rods. Every two characters in
     rings forms a color-position pair that is used to describe each ring where:

The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red
    ring placed onto the rod labeled 3, a green ring placed onto
     the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return the number of rods that have all three colors of rings on them.



Example 1:
Input: rings = "B0B6G0R6R0R6G9"
Output: 1
Explanation:
- The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
- The rod labeled 6 holds 3 rings, but it only has red and blue.
- The rod labeled 9 holds only a green ring.
Thus, the number of rods with all three colors is 1.


Example 2:
Input: rings = "B0R0G0R9R0B0G0"
Output: 1
Explanation:
- The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
- The rod labeled 9 holds only a red ring.
Thus, the number of rods with all three colors is 1.


Example 3:
Input: rings = "G4"
Output: 0
Explanation:
Only one ring is given. Thus, no rods have all three colors.


"""

def loop(rings: str):

    list_rings = list([y,x] for x,y in zip(rings[::2],rings[1::2]))
    dict1 = dict()

    for x in list_rings:
        if x[0] not in dict1.keys():
            dict1[x[0]] = x[1]
        else:
            dict1[x[0]] = x[1] + dict1.get(x[0])

    return sum(1 for x,y in dict1.items() if "R" in y and "G" in y and "B" in y)

print(loop("B0B6G0R6R0R6G9"))



##################################################################



def loop(rings: str):

    list_rings = list([y,x] for x,y in zip(rings[::2],rings[1::2]))
    dict1 = dict()

    for x in list_rings:
        if x[0] not in dict1.keys():
            dict1[x[0]] = x[1]
        else:
            dict1[x[0]] = x[1] + dict1.get(x[0])
    return dict1



print(loop("B0B6G0R6R0R6G9"))
#{'0': 'RGB', '6': 'RRB', '9': 'G'}





