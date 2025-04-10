"""



You are given an array prices where prices[i]
 is the price of a given stock on the ith day.

You want to maximize your profit by choosing
 a single day to buy one stock and choosing
 a different day in the future to sell that stock.


Return the maximum profit you can achieve from
 this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""




####################################################################


import numpy as np
def maxProfit(prices: list[int]) -> int:
    i = 0
    l = len(prices) - 1
    q = 0
    while i < len(prices):
        t = prices[l] - prices[i]
        if t < 0:
            prices = prices[1:]
            i = i + 1
            if t > q:
                q = t
        elif t >= 0:
            prices = prices[:-1]
            l = l - 1
            if t > q:
                q = t
    return q


print(maxProfit([1,2,11,4,7]))

#print(maxProfit([2,1,2,1,0,1,2]))


####################################################################


import numpy as np
def maxProfit(prices: list[int]) -> int:
    diff = np.array(np.diff(prices))
    m = sum(diff)
    for n in diff:
        x = np.sum(diff[1:])
        y = np.sum(diff[:-1])
        print(diff,m)
        if x >= y:
            diff = diff[1:]
            if np.sum(diff) > m:
                m = np.sum(diff)
        elif y >= x:
            diff = diff[:-1]
            if np.sum(diff) > m:
                m = np.sum(diff)
    return int(m)


print(maxProfit([1,2,11,4,7]))

print(maxProfit([2,1,2,1,0,1,2]))




####################################################################



import numpy as np
def maxProfit(prices: list[int]) -> int:
    diff = np.array(np.diff(prices))
    substrings = [(diff[i:j]) for i in range(len(diff)) if diff[i] > 0 for j in range(i + 1, len(diff) + 1)]
    return  substrings

print(maxProfit([7,1,5,3,6,4]))







####################################################################




import numpy as np
def maxProfit(prices: list[int]) -> int:
    diff = np.array(np.diff(prices))
    m = 0
    q = 0
    for i, n in enumerate(diff):
        m = 0
        if n <= 0:
            continue
        elif i + 1 == len(diff):
            if n > q:
                q = n
        elif n > q:
            q = n
        for t in diff[i + 1:]:
            m = n + t + m
            n = 0
            if m > q:
                q = m
    return int(q)

print(maxProfit([7,1,5,3,6,4]))







####################################################################







def max_num(prices : list[int]):

    max_diff = 0
    max_num = 0
    min_num = 0
    position_of_max = 0
    position_of_min = 0
    i = 0
    j = 0

    while j < len(prices):
        max_prices = max(prices)
        if prices.index(max_prices) == 0:
            prices.pop(0)
        else:
            break

    for index, nums in enumerate(prices):

        try:

            index_start = position_of_max + i
            max_num = max(prices[position_of_max + i:])
            position_of_max = prices.index(max_num,index_start)
            min_num = min(prices[position_of_min:position_of_max])
            position_of_min = prices.index(min_num,position_of_min)

            i = 1

            diff = max_num - min_num
            if diff > max_diff:
                max_diff = diff


        except ValueError as e:
            print(e)
            break
        else:
            pass

    return max_diff








#print(max_num([1,2,3,4,2,4,6,7,4,2,2,32,1,2,3,4,0]))

#print(max_num([3,1,2,0,0,0,1]))

print(max_num([7,4,1,2]))

#print(max_num([2,1,2,1,0,1,2]))

#print(max_num([31,31,31,31,31,31,31,32,1,2,3,4,0,1]))

#print(max_num([31,31,31,31,31,31,31,32,6,7,8,9,10,0,1,9]))



####################################################################




def max_num(prices : list[int]):

    max_diff = 0
    max_num = 0
    min_num = 0
    position_of_max = 0
    position_of_min = 0
    i = 0

    j = 0
    while j < len(prices):
        max_prices = max(prices)
        if prices.index(max_prices) == 0:
            prices.pop(0)
        else:
            break


    print(prices)

    for index, nums in enumerate(prices):

        try:

            index_start = position_of_max + i
            max_num = max(prices[position_of_max + i:])
            position_of_max = prices.index(max_num,index_start)
            min_num = min(prices[position_of_min:position_of_max])
            position_of_min = prices.index(min_num,position_of_min)

            i = 1

            diff = max_num - min_num
            if diff > max_diff:
                max_diff = diff


        except ValueError as e:
            print(e)
            break
        else:
            pass

    return max_diff








#print(max_num([1,2,3,4,2,4,6,7,4,2,2,32,1,2,3,4,0]))

#print(max_num([3,1,2,0,0,0,1]))

print(max_num([7,4,1,2]))

#print(max_num([2,1,2,1,0,1,2]))

#print(max_num([31,31,31,31,31,31,31,32,1,2,3,4,0,1]))

#print(max_num([31,31,31,31,31,31,31,32,6,7,8,9,10,0,1,9]))


word = "Helloobbpp"
print("lindex:",word.index("l",2,5))




####################################################################

def max_num(prices : list[int]):

    max_diff = 0


    for index, nums in enumerate(prices):
        for index2, nums2 in enumerate(prices):
            if index2 >= index:
                diff = nums2 - nums
                if diff > max_diff:
                    max_diff = diff

    return max_diff


print(max_num([1,2,3,4,2,4,6,7,4,2,2,32,1,2,3,4,0]))


####################################################################


def max_num(prices : list[int]):

    min_num = min(prices)
    position_of_min = prices.index(min_num)

    max_diff = 0

    for index, nums in enumerate(prices):
        if index >= position_of_min:
            diff = nums - min_num
            if diff > max_diff:
                max_diff = diff
    return max_diff



print(max_num([7,1,5,3,6,4]))


