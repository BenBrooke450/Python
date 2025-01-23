


"""

Given an integer num, repeatedly add all its
digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
"""

def number_split(number : int):
    split_int = [int(x) for x in str(number)]

    if len(split_int) > 1:
        for nums in split_int:
            numbers = sum(split_int)
            if numbers < 10:
                return numbers
            else:
                split_int = [int(x) for x in str(numbers)]
    else:
        return number

print(number_split(2147483647))






