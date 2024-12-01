
"""

Given a positive integer num,
return true if num is a perfect square or false otherwise.

A perfect square is an integer that
is the square of an integer. In other words,
it is the product of some integer with itself.

You must not use any built-in library
function, such as sqrt.


Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.


Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

"""


def isPerfectSquare(num: int) -> bool:
    print((list(map(lambda y: y * y == num, range(1, int((num / 2) + 1))))))
    if any(map(lambda y: y * y == num, range(1, int((num / 2) + 1)))):
        return True
    else:
        return False


print(isPerfectSquare(100))
[False, False, False, False, False, False, False, False, False, True, False, False, False,
 False, False, False, False, False, False, False, False, False, False, False, False, False,
 False, False, False, False, False, False, False, False, False, False, False, False, False,
 False, False, False, False, False, False, False, False, False, False, False]

True

####################################################################




def func_square(number: int):

    for y in range(1,number):
        z = (number / y)
        if z*z == number:
            return True
    return False


print(func_square(225))








