

"""
Given an array of integers arr, and three integers a, b and c.
    You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.



Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].


Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.

"""
def func(arr: list[int], a: int, b: int, c: int):

    f = 0
    n = 0
    m = 0
    j = 0

    for x in arr:

        if f == len(arr) - 2:
            break

        else:
            f = f + 1
            n = 0

        for y in arr[f + n:]:
            n = n + 1
            m = 0

            for z in arr[f + n + m:]:
                m = m + 1

                print(x,y,z)

                if ((abs(x - y) <= a) and (abs(y - z) <= b) and (abs(x - z) <= c)):
                    print("PASSED: ",x,y,z)
                    j = j + 1
    return j

print(func(arr = [5,5,2,6,4], a = 5, b = 4, c = 5))
#10


############################################################


def func(arr: list[int], a: int, b: int, c: int):

    n = 0
    m = 0

    list2 = []

    for x in arr:
        list2.extend([arr[n:n+3]])
        n = n + 1
        if n == len(arr) - 2:
            for y in list2:
                print(y)
                if ((abs(y[0] - y[1]) <= a) and (abs(y[1] - y[2]) <= b) and (abs(y[0] - y[2]) <= c)):
                    m = m + 1
    return m



print(func([3,0,1,1,9,7], 7, 2, 3))









