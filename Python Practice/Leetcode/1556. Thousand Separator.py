

"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"
"""



def thousandSeparator(n: int) -> str:
    n = [x for x in str(n)]
    l = len(n)
    if len(n) > 3:
        n = n[::-1]
        t = l // 3

        if l % 3 == 0:
            for m in range(3, 3 * t, 4):
                print(m)
                n.insert(m, ".")

        elif l % 3 != 0:
            for m in range(3, 3*t+3, 4):
                print(m)
                n.insert(m, ".")

        return "".join(n[::-1])
    else:
        return "".join(n)

print(thousandSeparator(1234123))







