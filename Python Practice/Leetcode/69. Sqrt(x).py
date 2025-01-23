


"""

Given a non-negative integer x, return the
square root of x rounded down to the nearest integer.
 The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and
since we round it down to the nearest integer, 2 is returned.

"""

def mySqrt(num: int) -> int:

    low = 0
    high = num

    while low <= high:

        mid = (high + low) // 2

        if mid*mid > num:
            high = mid - 1

        elif mid*mid < num:
            low = mid + 1

        else:
            return mid

    return high



print(mySqrt(103))



####################################################################


def mySqrt(num: int) -> int:

    list1 = list(range(1, num + 1))

    high  = len(list1) - 1
    low = 0
    mid = 0

    max_val = 0

    while low <= high:
        mid = (high + low) // 2

        if (list1[mid]*list1[mid]) < num:
            low = mid + 1
            a = list1[mid] * list1[mid]
            if (list1[mid] * list1[mid]) > max_val:
                a = list1[mid]

        elif (list1[mid]*list1[mid]) > num:
            high = mid - 1

        elif (list1[mid]*list1[mid]) == num:
            return list1[mid]

    return a


print(mySqrt(103))





####################################################################




def mySqrt(self, num: int) -> int:

    import numpy as np

    start = 0
    stop = num
    step = 0.5

    if num == 0:
        return 0
    elif num == 1:
        return 1

    for x in np.arange(start, stop, step)[::-1]:
        if (x * x) <= num:
            return round(x // 1)



####################################################################




def square_root(num: int):
    numbs = ((num)**(1/2))
    return int(numbs//1)

print(square_root(8))
#2.0




####################################################################






"""So basically we are halfing the list everytime by 
  changing the low and high points from which we divide by 2
  
  If we have a list of say list = [1,2,3...,10]
    
    we first find the length which is = 10 - 1 = 9 (as python starts at 0)
    
    we find the mid point which is mid = (high + low) // 2  =>  
        (0+9)//2 which is 4 (is the index position, it would be 4.5 but we used //)
    
    so let's say we are looking for target of 3
    
    1. is 0 <= 9, yes that is correct so we start 
    
    2. list[mid] list[4] which is equal to 5 and the target is 3
    
    3. 5 is bigger then 3, so we (high = mid - 1) 4 - 1 = 3, 
         so now our high point is 3
    
    4. now we have index positions of low is 0 and high is 3,
         is low smaller or equal to 3, lower so we continue.
    
    5. mid = (high + low) // 2 
         mid = (3 + 0) // 2   =>    mid = 1
       
    6. so now our mid = 1, so list1[1] = 2
          is 2 less or bigger then 3 our target, less, so
          low = mid + 1   =>   low = 1 + 1
          so low = 2
    
    7. now we have low on 2 and high on 3,
        is low <= high, yea so we continue
    
    8. mid = (high + low) // 2
         mid = (3 + 2) // 2     =>    mid = 2
    
    9. list[mid]   =>   list[2] = 3
        which is list[mid] == target 
        sooo there we have it 
        index of 2 get´s you your target
          
  
  """

def binary_search(list1, target):
    low = 0
    high = len(list1) - 1
    print(high)
    mid = 0  # Place holder
    while low <= high:


        mid = (high + low) // 2
        print(mid)
        # Check if x is present at mid


        if list1[mid] < target:
            low = mid + 1

        # If x is greater, ignore left half
        elif list1[mid] > target:
            high = mid - 1


        # If x is smaller, ignore right half
        else:
            return [mid]

    # If we reach here, the element was not present
    return None













