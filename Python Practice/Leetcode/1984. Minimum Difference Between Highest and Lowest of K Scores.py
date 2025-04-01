
"""
You are given a 0-indexed integer array nums,
    where nums[i] represents the score of the
     ith student. You are also given an integer k.

Pick the scores of any k students from the array
    so that the difference between the highest
     and the lowest of the k scores is minimized.

Return the minimum possible difference.



Example 1:
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.

"""

def minimumDifference(nums: list[int], k: int) -> int:
    if k == 1:
        return 0
    else:
        nums.sort()
        n = 1
        m = 0
        t = 1000000
        nums = nums + nums
        print(nums)
        while m + k <= len(nums):
            list_k = nums[m:k + m]
            print(list_k)
            m = m + 1
            x = max(list_k) - min(list_k)
            if x < t:
                t = x
    return t


print(minimumDifference([87063,61094,44530,21297,95857,93551,9918],k=6))






#########################################


from itertools import combinations

def minimumDifference(nums: list[int], k: int) -> int:
    if k == 1:
        return 0
    else:
        t = 10000000
        combinations_of_k = list(combinations(nums, k))
        for n in combinations_of_k:
            x = max(n) - min(n)
            if x < t:
                t = x
    return t

#print(minimumDifference(nums=[41900,69441,94407,37498,20299,10856,36221,2231,54526,79072,84309,76765,92282,13401,44698,17586,98455,47895,98889,65298,32271,23801,83153,12186,7453,79460,67209,54576,87785,47738,40750,31265,77990,93502,50364,75098,11712,80013,24193,35209,56300,85735,3590,24858,6780,50086,87549,7413,90444,12284,44970,39274,81201,43353,75808,14508,17389,10313,90055,43102,18659,20802,70315,48843,12273,78876,36638,17051,20478], k=5))







#########################################

def minimumDifference(nums: list[int], k: int) -> int:
    if k == 1:
        return 0
    else:
        substrings = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if len(nums[i:j]) == k]
        y = [nums[i:i + 2] for i in range(len(nums) - 1)]
    return substrings, y

#print(minimumDifference(nums = [9,4,1,7], k = 2))







