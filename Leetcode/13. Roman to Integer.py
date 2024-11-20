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








####################################################################



def converter(number : int):
    dic1 = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
    list = [1,5,10,50,100,500,1000,4,9,40,90,400,900]

    if 0 <= number < 10:
        if number in list:
            return dic1[number]

        elif max(dic1.keys()) < number:
            a = max(dic1.keys())
            print(a*number)

converter(3)


""""   number % 10

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