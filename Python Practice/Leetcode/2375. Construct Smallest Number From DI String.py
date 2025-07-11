
"""
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.



Example 1:
Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.


Example 2:
Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

"""

def smallestNumber(pattern: str) -> str:
    pattern =[x for x in pattern]
    k = 1
    n = list(range(1,len(pattern) + 2))
    list1,list2 = [],[]
    while k + 1 < len(n):
        if pattern[k] == "I":
            list1.append(n[k])

        k = k + 1

    return n


print(smallestNumber("IIIDIDDD"))




"""def smallestNumber(pattern: str) -> str:
    pattern =[x for x in pattern]
    i = 0
    j = 0
    list1 = [1]
    while i + 1 < len(pattern):
        if pattern[i] == "D" and pattern[i+1] == "I":
            j = j + 2
            list1.append(j)
        elif pattern[i] == "D" and pattern[i+1] == "D":
            x = "I".split(pattern[i:])
            x = len([0])
            j = j + """
