
"""
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.



Example 1:
Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

Example 2:
Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.

"""


def largestTimeFromDigits(arr: list[int]) -> str:

    max_list = list()

    for i,x in enumerate(arr):
        for j,y in enumerate(arr):
            if i != j:
                print(x,y)
                x, y = str(x), str(y)
                hour = int(x + y)
                if hour < 24:
                    max_list.append([hour,x + y])

    print(max_list)

    if len(max_list) != 0:
        hour = max(max_list,key=lambda x: x[0])
    else:
        return ""

    print(hour)

    hour = hour[1]
    print("pass")

    for x in str(hour[0]):
        i = arr.index(int(x))
        arr.pop(i)

    for x in str(hour[1]):
        i = arr.index(int(x))
        arr.pop(i)

    print(arr)

    max_minute = 0

    one = [str(x) for x in arr]
    two = [str(x) for x in arr][::-1]

    one = [int("".join(one)),str("".join(one))]
    two = [int("".join(two)),str("".join(two))]

    print(one,two)

    if one[0] < 59 and two[0] < 59:
         if one[0] > two[0]:
             max_minute = one[1]
         else:
             max_minute = two[1]
    elif one[0] < 59:
        max_minute = one[1]
    elif one[0] < 59:
        max_minute = two[1]
    else:
        return ""

    return str(hour) + ":" + str(max_minute)

print(largestTimeFromDigits(arr = [2,0,6,6]))




