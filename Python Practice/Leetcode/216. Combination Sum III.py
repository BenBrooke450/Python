
"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

"""


def combinationSum3(k: int, n: int) -> list[list[int]]:

    numbers = list(range(1,n+1))
    nine = []
    result = []

    def sum_nums_back(index_num):

        if sum(nine) == n and len(nine) == k:
            result.append(nine)
            return

        num = numbers[index_num]
        nine.append(num)
        print("TEST",nine)

        if len(nine) == k:
            nine.pop()

        sum_nums_back(index_num + 1)
        nine.pop()





    sum_nums_back(0)


print(combinationSum3(3,9))



