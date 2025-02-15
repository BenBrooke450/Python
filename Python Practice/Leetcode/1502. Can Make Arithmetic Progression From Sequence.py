
"""
A sequence of numbers is called an arithmetic progression
    if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array
    can be rearranged to form an arithmetic progression. Otherwise, return false.



Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or
    [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.


Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

"""


def canMakeArithmeticProgression(arr: list[int]) -> bool:

    arr.sort()
    diff = arr[1] - arr[0]
    n = 0

    while n < len(arr)-1:
        if arr[n] + diff == arr[n+1]:
            n = n + 1
        else:
            return False

    return True

print(canMakeArithmeticProgression([3,5,1]))









