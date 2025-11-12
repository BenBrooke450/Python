
"""
You are given two integers, n and k.

An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.

Return the minimum possible sum of a k-avoiding array of length n.



Example 1:
Input: n = 5, k = 4
Output: 18
Explanation: Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.

Example 2:
Input: n = 2, k = 6
Output: 3
Explanation: We can construct the array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.


"""








def minimumSum(n: int, k: int) -> int:
    n_list = set()

    first_numbers = range(n + 10000)

    cant_be = set()

    for i in range(1,n+1000):
        if len(n_list) >= n:
            break
        elif first_numbers[i] in cant_be:
            continue

        for j in range(i + 1,n+1000):
            if first_numbers[i] + first_numbers[j] == k:
                cant_be.add(j)

            if len(n_list) >= n:
                break

        if first_numbers[i] not in cant_be:
            n_list.add(first_numbers[i])

    return sum(n_list) + sum(set(x for x in range(n + 1, 2 * n - len(n_list) + 1)))

print(minimumSum(n = 3, k = 5))













