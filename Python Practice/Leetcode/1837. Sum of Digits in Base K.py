

"""
Given an integer n (in base 10) and a base k,
    return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be
    interpreted as a base 10 number, and the sum should be returned in base 10.



Example 1:

Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
Example 2:

Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.


"""
def sumBase(n: int, k: int) -> int:

    list1 = []

    i = int

    while n != 0:
        i = n % k
        list1.append(i)
        n = n // k

    return sum(list1)

print(sumBase(n = 34, k = 6))



#################################

def sumBase(n: int, k: int) -> int:

    list1 = []

    while n > 10:
        i = n % k
        list1.append(i)
        n = n // k
        if n < 10:
            i = n % k
            list1.append(i)

    return sum(list1)




