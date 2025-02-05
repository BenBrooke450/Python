
"""
Given an array arr, replace every element in that array
    with the greatest element among the elements to its right,
     and replace the last element with -1.

After doing so, return the array.



Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.


"""

def replaceElements(self, arr: List[int]) -> List[int]:

    n = 1
    l = len(arr)
    reverse_arr = arr[::-1]

    while l >= n + 1:
        if n + 1 >= l:
            reverse_arr = reverse_arr[::-1]
            reverse_arr.append(-1)
            arr = reverse_arr[1:]
            break
        elif reverse_arr[n] < reverse_arr[n - 1]:
            reverse_arr[n] = reverse_arr[n - 1]
            n = n + 1
        else:
            n = n + 1
    if len(arr) == 1:
        return [-1]
    return arr
print(replaceElements([17,18,5,4,6,1]))
print(replaceElements([17]))


###############################################################


def replaceElements(arr: list[int]) -> list[int]:
    n = 0
    l = len(arr)

    while l >= n + 1:
        if n + 1 >= l:
            arr[n] = -1
            break
        else:
            t = max(arr[n + 1:])
            arr[n] = t
            n = n + 1
    return arr

print(replaceElements([17,18,5,4,6,1]))


