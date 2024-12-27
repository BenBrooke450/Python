

"""

You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

You must perform an operation shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with the result of the shift(s[i-1], s[i]) operation.

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

Note that shift(c, x) is not a preloaded function, but an operation to be implemented as part of the solution.



Example 1:

Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
Example 2:

Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'

"""
from matplotlib.style.core import library

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

y = range(1,len(x))

dict1 = dict()

for x,y in zip(x,y):
    dict1[y] = x





def lib(s:str):

    library = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'
    , 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o'
    , 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v'
    , 23: 'w', 24: 'x', 25: 'y',26:'z'}

    f = [x for x in s]
    s = [x for x in s]


    n = 2
    for x in s:
        for key,value in library.items():
            if value == x and n != len(s) + 1:
                q = int(s[n-1]) + key
                f[n-1] = library.get(q)
                n = n + 2

    print(f)

    return "".join(f)


print(lib("c4k9v1q9r0g"))
#cgktvwqzrrg

#####################################################









def lib(s:str):

    library = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
               'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
               'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
               'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
               'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25}

    list2 = []

    s = [x for x in s]
    n = 2

    for x in s:
        z = library.get(x)
        if z == None:
            continue
        else:
            q = int(s[n-1]) + z
            s[n-1] = q
        n = n + 2

    return s



