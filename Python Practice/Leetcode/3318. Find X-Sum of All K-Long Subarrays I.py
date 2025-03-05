
"""
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements.
    If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.

Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].



Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

"""

from collections import Counter

def findXSum(nums: list[int], k: int, x: int) -> list[int]:

    substrings = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if len(nums[i:j]) == k]
    print(substrings)
    i = 0
    list1 = []
    while len(substrings) != i :
        freq = Counter(substrings[i])
        #sorted(arr, key=lambda x: (-freq[x], -x))
        most_feq = list(sorted([x for x in set(substrings[i]) if substrings[i].count(x) > 1],key=lambda x: (-freq[x], -x),reverse=True))[-x:]
        print(most_feq)
        if len(most_feq) < x:
            left = x - len(most_feq)
            numbers = sorted([x for x in set(substrings[i]) if substrings[i].count(x) == 1])[-left:]
            everything = most_feq + numbers
        else:
            everything = most_feq

        list1.append(sum([x for x in substrings[i] if x in everything]))
        i = i + 1

    return list1

print(findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))


print(findXSum([5,5,4,3,1,3,1,3,4,6,4,2],10,2))


print(findXSum([2,8,9,3,4,9,4],6,1))


