
"""
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.



Example 1:
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array.
Notice that there are no odd integers or integers with leading zeros.

Example 2:
Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits.
In this example, the digit 8 is used twice each time in 288, 828, and 882.

Example 3:
Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.

"""


def findEvenNumbers(digits: list[int]) -> list[int]:
    digits = "".join([str(x) for x in digits])
    list1 = [int(n + m + q) for n in set(digits) for m in set(digits) for q in set(digits) if
             int(n + m + q) % 2 == 0 and (n + m + q).count(n) <= digits.count(n) and (n + m + q).count(
                 m) <= digits.count(m) and (n + m + q).count(q) <= digits.count(q)]

    return sorted(list1)

print(findEvenNumbers([2,2,8,8,2]))

#########################################################



def findEvenNumbers(digits: list[int]) -> list[int]:
    digits = "".join([str(x) for x in digits])
    list1 = []
    for n in digits:
        for m in digits:
            for q in digits:
                r = n+m+q
                if int(r) % 2 == 0 and r.count(n) <= digits.count(n) and r.count(m) <= digits.count(m) and r.count(q) <= digits.count(q) and r not in list1:
                    list1.append(n+m+q)

    return list1


print(findEvenNumbers([2,2,8,8,2]))












