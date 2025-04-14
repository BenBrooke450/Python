
"""
Initially, you have a bank account balance of 100 dollars.

You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars, in other words, its price.

When making the purchase, first the purchaseAmount is rounded to the nearest multiple of 10. Let us call this value roundedAmount. Then, roundedAmount dollars are removed from your bank account.

Return an integer denoting your final bank account balance after this purchase.

Notes:

0 is considered to be a multiple of 10 in this problem.
When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so on).


Example 1:

Input: purchaseAmount = 9

Output: 90

Explanation:

The nearest multiple of 10 to 9 is 10. So your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15

Output: 80

Explanation:

The nearest multiple of 10 to 15 is 20. So your account balance becomes 100 - 20 = 80.

Example 3:

Input: purchaseAmount = 10

Output: 90

Explanation:

10 is a multiple of 10 itself. So your account balance becomes 100 - 10 = 90.

"""



def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
    n = str(purchaseAmount)

    if int(n) < 10:
        if int(n) > 4:
            return 90
        else:
            return 100
    elif int(n) == 100:
        return 0
    else:
        if int(n[1]) > 4:
            return 100 - (int(n[0]) + 1) * 10
        else:
            return 100 - (int(n[0])) * 10











