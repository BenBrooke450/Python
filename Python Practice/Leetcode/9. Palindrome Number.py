
"""Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""


def pan(x: int) -> bool:
    reverse = [item for item in str(abs(x))]
    if int("".join(reverse[::-1])) == abs(x) and x >= 0:
        return True
    else:
        return False

print(pan(101))
#True
print(pan(134))
#False

print(pan(5))
#True

print(pan(-121))
