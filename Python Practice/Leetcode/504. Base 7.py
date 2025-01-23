

"""
Given an integer num, return a string of its base 7 representation.



Example 1:

Input: num = 100
Output: "202"


Example 2:

Input: num = -7
Output: "-10"

"""


def base(number : int):
    list1 = []

    if number == 0:
        return "0"

    elif number > 0:
        for nums in range(0, abs(number)):
            remainder = number % 7
            number = number // 7
            list1.insert(0,remainder)
            if number == 0:
                break

    elif number < 0:
        for nums in range(0, abs(number)):
            remainder = abs(number) % 7
            number = abs(number) // 7
            list1.insert(0,remainder)
            if number == 0:
                list1.insert(0,"-")
                break

    return ''.join(str(x) for x in list1)


print(base(-11))



