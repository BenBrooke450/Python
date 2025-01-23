"""

Given an integer n, return true if it
is a power of two. Otherwise, return false.

An integer n is a power of two,
if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false


"""




def power_two_se(number: int):

    if number <= 0:
        return False

    while number % 2 == 0:
        number //= 2

    return number == 1


print(power_two_se(17))


####################################################################




def power_two(number :int):
    if any(x for x in range(0, number//2) if (2**(x)) == number ):
        return True
    else:
        return False

print(power_two(32))