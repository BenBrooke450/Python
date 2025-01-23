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


