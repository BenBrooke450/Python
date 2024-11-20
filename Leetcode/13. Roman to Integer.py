"""

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two
ones added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
 However, the numeral for four is not IIII. Instead, the number four is
 written as IV. Because the one is before the five we subtract it making
 four. The same principle applies to the number nine, which is written
 as IX. There are six instances where subtraction is used:


I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.


Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.


Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


2020 = MMXX

"""

from collections import Counter


def converter(roman_number : str):
    dic1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500
        ,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,
            "CM":900}

    dictt = Counter(roman_number)
    dictt2 = dict(dictt.items())

    dic2 = {}
    i = 0
    for key, value in dic1.items():
        if key not in str(roman_number):
            dic2[key] = i

        elif key in str(roman_number):
                dic2[key] = i + 1

    dic2.update(dictt2)

    i = 0

    for key, value in dic2.items():
        if len(key) > 2
            value = value +


    print(dic2)


converter("MVIX")




####################################################################


"""

import re


def converter(roman_number : str):
    dic1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500
        ,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,
            "CM":900}
    dic2 = {}
    i = 0
    for  key, value in dic1.items():
        if key not in str(roman_number):
            dic2[key] = i


        elif key in str(roman_number) or key == str(roman_number):
            for letter in str(roman_number):
                    dic2[key] = i + 1

    return (dic2)




print(converter("MXLVIIIV"))






converter(3)


     number % 10

    ((number % 100) - (number % 10))

    ((number % 1000) - (number % 100))"""








"""
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""



####################################################################



def comp(num :int):
    print(num % 10)

    print((num % 100) - (num % 10))
    print(num % 100)

    print((num % 1000) - (num % 100))
    print(num % 1000)

comp(768)
8
60
68
700
768

comp(1152)
2
50
52
100
152


####################################################################

def compont(numbers : int):
    int_list = [int(num) for num in str(numbers)]
    number = str(numbers).split()
    if numbers < 10:
        print(number)
    elif 10 <= numbers < 100:
        tenth = int_list[0]
        digit = int_list[1]
        print(tenth*10,digit)
    elif 100 <= numbers < 1000:
        hund = int_list[0]
        tenth = int_list[1]
        digit = int_list[2]
        print(hund*100,tenth*10,digit)
    elif 1000 <= numbers < 10000:
        thous = int_list[0]
        hund = int_list[1]
        tenth = int_list[2]
        digit = int_list[3]
        print(thous*1000,hund*100,tenth*10,digit)

compont(1063)
#1000 0 60 3


####################################################################


def comp(num :int):

    list1 = []

    zero = num % 10
    if  zero > 0:
        list1.append(zero)

    first = (num % 100) - (num % 10)
    if  first > 0:
        list1.append(first)

    second = (num % 1000) - (num % 100)
    if  second > 0:
        list1.append(second)

    third = (num % 10000) - (num % 1000)
    if  third > 0:
        list1.append(third)

    return list1

print(comp(768))
[8, 60, 700]


print(comp(1152))
[2, 50, 100, 1000]



comp(1152)