

"""
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM",
    where HH is between 00 and 23, and MM
    is between 00 and 59. The earliest 24-hour time
     is 00:00, and the latest is 23:59.

In one operation you can increase the time
    current by 1, 5, 15, or 60 minutes.
     You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.



Example 1:
Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.

Example 2:
Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.

"""


def convertTime(current: str, correct: str) -> int:
    correct = correct.split(":")
    current = current.split(":")

    hours = abs(int(correct[0]) - int(current[0]))

    if int(correct[0]) == int(current[0]):
        n = 0
        mins =  abs(int(correct[1]) - int(current[1]))

        t = mins // 15
        mins = mins - t * 15

        n = n + t

        q = mins // 5
        mins = mins - q * 5

        n = n + q + mins

        return n

    else:
        current_mins = abs(int(current[1]) - 60)

        current_hour = int(current[0]) + 1

        hour_diff = int(correct[0]) - current_hour

        total_mins = int(correct[1]) + current_mins

        n = hour_diff + total_mins//60

        mins = total_mins % 60

        t = mins // 15
        mins = mins - t * 15

        n = n + t

        q = mins // 5
        mins = mins - q * 5

        n = n + q + mins

        return n




print(convertTime(current = "02:30", correct = "04:35"))

print(convertTime(current = "09:41", correct = "10:34"))




