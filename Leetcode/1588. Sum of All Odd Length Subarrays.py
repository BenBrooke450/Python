

"""
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58


Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.


Example 3:

Input: arr = [10,11,12]
Output: 66



"""


def func(list1:list[int]):

    list2 = [x for x in range(0,len(list1)+1) if x % 2 != 0]

    list3 = []
    list4 = []

    for nums in list2[::-1]:

        n = 0

        for nums2 in list1:

            if len(list1[n:n + nums]) == nums:

                x = sum(list1[n:n + nums])

                list3.append(x)

                n = n + 1

        list4.append(sum(x for x in list3))

        list3 = []


    return sum(list4)




print(func([1,4,2,5,3]))





