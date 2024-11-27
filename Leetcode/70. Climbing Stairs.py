"""

You are climbing a staircase. It
takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


5 = [1,1,1,1,1]
5 = [2,1,1,1] * 4
5 = [1,2,2] * 3

6 = [1,1,1,1,1,1]
6 = [1,1,1,1,2] * 5   [1,1,1,2,1] [1,1,2,1,1] [1,2,1,1,1] [2,1,1,1,1] [1,1,1,1,2]
6 = [1,1,2,2] * 4
6 = [2,2,2] * 1

7 = [1,1,1,1,1,1,1]
7 = [1,1,1,1,1,2] * 6
7 = [1,1,1,2,2] * 7    [1,1,2,1,2] [1,2,1,1,2] [2,1,1,1,2] [2,1,1,2,1] [2,1,2,1,1] [2,2,1,1,1] [1,1,1,2,2]
7 = [1,2,2,2] * 4


8 = [1,1,1,1,1,1,1,1]
8 = [1,1,1,1,1,1,2] * 7   [1,1,1,2,1] [1,1,2,1,1] [1,2,1,1,1] [2,1,1,1,1] [1,1,1,1,2]
8 = [1,1,1,1,2,2] * 9
8 = [1,1,2,2,2] * 6
8 = [2,2,2,2] * 1

9 = [1,1,1,1,1,1,1,1,1]


EVEN = length 4 = [1] * 1 [2,2] *1  [1,1,2] * 3
       length 6 = [1] * 1 [2,2,2] *1  [1,1,2,2] * 4 [1,1,1,1,2] * 5
       length 8 = [1] * 1 [2,2,2,2] * 1 [1,1,2,2,2] * 6 [1,1,1,1,2,2] * 9 [1,1,1,1,1,1,2] * 7


odd = times + 2
even  =
"""

step1 = 1
step3 = 3
step5 = 8
step7 = 21
step9 = 55
step11 = 144

step2 = 2
step4 = 5
step6 = 13
step8 = 34
step10 = 89
step12 = 233
step14 = 610
step16 = 1597
step18 = 4181
step20 = 10946

step33 = 5702887
step34 = 9227465
step35 = 14930352

step43 = 701408733
step44 = 1134903170






def climbStairs( string: int) -> int:
    dic = {1: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13, 7: 21, 8: 34, 9: 55, 10: 89, 11: 144, 12: 233}

    if string in dic.keys():
        return dic.get(string)
    else:
        i = 1
        j = 12
        while True:

            dic[12 + i] = round((1.618033988749895 * dic.get(j)), 0)

            if string in dic.keys():
                return int(max(dic.values()))

            i = i + 1
            j = j + 1

####################################################################




def stars(string: int):

    dic1odd = {1:1,3:3,5:8,7:21,9:55,11:144}
    dic2even = {2:2,4:5,6:13,8:34,10:89,12:233}

    if string % 2 == 0:
        if string in dic2even.keys():
            return dic2even.get(string)
        else:
            i = 2
            j = 12
            while True:

                dic2even[12 + i] = (2.6180339887498949*dic2even.get(j))

                if string in dic2even.keys():
                    return int(round(max(dic2even.values())))

                i = i + 2
                j = j + 2

    elif string % 2 != 0:
        if string in dic1odd.keys():
            return dic1odd.get(string)
        else:
            i = 2
            j = 11
            while True:

                dic1odd[11 + i] = (2.6180339887498949*dic1odd.get(j))

                if string in dic1odd.keys():
                    return int(round(max(dic1odd.values())))

                i = i + 2
                j = j + 2



























