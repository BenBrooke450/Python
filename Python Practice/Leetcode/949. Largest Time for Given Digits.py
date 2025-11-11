
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

    index = [0,1,2,3]

    for i,x in enumerate(arr):
        for j,y in enumerate(arr):
            if i != j:
                x, y = str(x), str(y)
                hour = int(x + y)
                hours_left = [str(arr[q]) for q in index if q != i and q != j]
                hours_left_one = int("".join(hours_left))
                hours_left_two = int("".join(hours_left[::-1]))
                if hour < 24 and (hours_left_one < 60 or hours_left_two < 60):
                    max_list.append([hour,x + y])


    if len(max_list) != 0:
        hour = max(max_list,key=lambda x: x[0])
    else:
        return ""


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

    if one[0] < 60 and two[0] < 60:
         if one[0] > two[0]:
             max_minute = one[1]
         else:
             max_minute = two[1]
    elif one[0] < 60:
        max_minute = one[1]
    elif two[0] < 60:
        max_minute = two[1]
    else:
        return ""

    return str(hour) + ":" + str(max_minute)

print(largestTimeFromDigits(arr = [1,9,6,0]))






######################### chat gpt


from itertools import permutations

def largestTimeFromDigits(arr: list[int]) -> str:
    max_time = -1

    # Try every permutation of 4 digits
    for h1, h2, m1, m2 in permutations(arr):
        hour = h1 * 10 + h2
        minute = m1 * 10 + m2

        if hour < 24 and minute < 60:
            total_minutes = hour * 60 + minute
            max_time = max(max_time, total_minutes)

    if max_time == -1:
        return ""

    # Convert back to HH:MM format
    return f"{max_time // 60:02d}:{max_time % 60:02d}"



