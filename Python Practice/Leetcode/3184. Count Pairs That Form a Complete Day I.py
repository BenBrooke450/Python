

"""
Given an integer array hours representing times in hours,
    return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.



Example 1:
Input: hours = [12,12,30,24,24]
Output: 2
Explanation:
The pairs of indices that form a complete day are (0, 1) and (3, 4).

Example 2:
Input: hours = [72,48,24,3]
Output: 3
Explanation:
The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).
"""
import numpy as np


def countCompleteDayPairs(hours: list[int]) -> int:

    hours_array = np.array(hours)

    i = 0
    n = 0

    for h in hours_array:
        i = i + 1
        for h2 in hours_array[i:]:
            if (h + h2) % 24 == 0:
                n = n + 1
    return n

print(countCompleteDayPairs([72,48,24,3]))






