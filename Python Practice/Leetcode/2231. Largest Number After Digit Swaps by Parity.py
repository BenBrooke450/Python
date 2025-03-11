

"""
You are given a positive integer num. You may swap any two digits
    of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.



Example 1:
Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.


Example 2:
Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

"""


def largestInteger(num: int) -> int:
    nums = str(num)
    num = [int(x) for x in str(num)]
    num_even_odd = ["even" if int(x) % 2 ==0 else "odd" for x in nums]
    even = sorted([x for x in nums if int(x) % 2 == 0 ],reverse=True)
    odd = sorted([x for x in nums if int(x) % 2 != 0],reverse=True)
    for i,n in enumerate(num_even_odd):
        if n == "even":
            num[i] = even[0]
            even = even[1:]
        elif n == "odd":
            num[i] = odd[0]
            odd = odd[1:]
    return int("".join(num))

print(largestInteger(65875))









