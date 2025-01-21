
"""
You are given an integer array cost where cost[i]
    is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


"""

def minCostClimbingStairs(cost: list[int]) -> int:

    cost.append(0)
    reverse_cost = cost[::-1]

    n = 0

    while n < len(reverse_cost) - 3:
        print(reverse_cost[::-1])
        reverse_cost[n+3] = min(reverse_cost[n + 1],reverse_cost[n + 2]) + reverse_cost[n+3]
        n = n + 1

    return min(reverse_cost[-1],reverse_cost[-2])



print(minCostClimbingStairs([20, 1, 2, 20, 1, 5, 1, 30]))
#5

print(minCostClimbingStairs([10, 15, 20]))
#15




##########################################################

def minCostClimbingStairs(cost: list[int]) -> int:

    c = 0
    g = 0

    while g + 1 < len(cost) - 1:
        c = cost[g] + c
        q = cost[g] + cost[g + 1]
        p = cost[g] + cost[g + 2]
        if q < p:
            g = g + 1
        elif q > p or q == p:
            g = g + 2

    n = 1
    c2 = 0

    while n + 1 < len(cost) - 1:
        c2 = cost[n] + c2
        q = cost[n] + cost[n + 1]
        p = cost[n] + cost[n + 2]
        if q < p:
            n = n + 1
        elif q > p or q == p:
            n = n + 2

    return min(c + cost[g],c2 + cost[n])

print(minCostClimbingStairs([20, 1, 2, 20, 1, 5, 1, 30]))

print(minCostClimbingStairs([10,15,20]))


