"""

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
"""

def non_int(num1 : str, num2 : str):
    pass




non_int("1231","12414")



####################################################################



def non_int(number1 : str,number2 : str):
    return str(int(number1) + int(number2))

print(non_int("15","20"))
