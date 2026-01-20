

"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

"""


def maximumSwap(num: int) -> int:

    if "".join(sorted(str(num),reverse=True)) == str(num) or len(str(num)) == 1:
        return num

    text_num = [y for y in str(num)]

    for i,x in enumerate(text_num):
        if int(x) == max([int(x) for x in text_num[i:]]):
            pass

        else:
            largest_num = max([int(x) for x in text_num[i:]])
            if text_num[i:].count(str(largest_num))>1:
                text_num_reverse = text_num[::-1]
                n_r = len(text_num) - 1
                position_largest = n_r + text_num_reverse.index(str(largest_num))
                text_num[i], text_num[position_largest] = text_num[position_largest], text_num[i]
                return int("".join(text_num))

            position_largest = i + text_num[i:].index(str(largest_num))
            text_num[i], text_num[position_largest] = text_num[position_largest], text_num[i]
            return int("".join(text_num))


print(maximumSwap(1993))









