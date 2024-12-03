
"""

A self-dividing number is a number
that is divisible by every digit it contains.

For example, 128 is a self-dividing
number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed
to contain the digit zero.

Given two integers left and right, return
a list of all the self-dividing numbers in
 the range [left, right] (both inclusive).



Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]

"""






def self_divide(left: int, right: int):
    list2 = []
    number = [[str(x) for x in str(numbers)] for numbers in range(left, right+1) if numbers % 10 != 0 and "0" not in str(numbers)]
    a = list(filter(lambda nums: all(map(lambda y : int("".join(nums)) % int(y) == 0 ,(y for y in nums))) ,(nums for nums in number)))
    b = list(map(lambda x: int("".join(x)),a))
    return b

    #result = list(map(lambda a: list(map(lambda b: a + b, y)), x))

print(self_divide(123,2340))
"""
[124, 126, 128, 132, 135, 144, 155, 162, 168, 175, 184, 212, 216,
 222, 224, 244, 248, 264, 288, 312, 315, 324, 333, 336, 366, 384,
  396, 412, 424, 432, 444, 448, 488, 515, 555, 612, 624, 636, 648,
   666, 672, 728, 735, 777, 784, 816, 824, 848, 864, 888, 936, 999,
    1111, 1112, 1113, 1115, 1116, 1122, 1124, 1128, 1131, 1144, 1155,
     1164, 1176, 1184, 1197, 1212, 1222, 1224, 1236, 1244, 1248, 1266,
      1288, 1296, 1311, 1326, 1332, 1335, 1344, 1362, 1368, 1395, 1412,
       1416, 1424, 1444, 1448, 1464, 1488, 1515, 1555, 1575, 1626, 1632,
        1644, 1662, 1692, 1715, 1722, 1764, 1771, 1824, 1848, 1888, 1926,
         1935, 1944, 1962, 2112, 2122, 2124, 2128, 2136, 2144, 2166, 2184,
          2196, 2212, 2222, 2224, 2226, 2232, 2244, 2248, 2262, 2288, 2316, 2322, 2328]"""











def self_divide(left: int, right: int):
    number = [[str(x) for x in str(numbers)] for numbers in range(left, right+1) if numbers % 10 != 0]
    print(list(map(lambda nums: list(map(lambda y : int("".join(nums)) % int(y) == 0 ,(y for y in nums))) ,(nums for nums in number))))

    #result = list(map(lambda a: list(map(lambda b: a + b, y)), x))

self_divide(1,15)
[[True], [True], [True], [True], [True], [True], [True], [True], [True], [True, True], [True, True], [True, False], [True, False], [True, True]]


