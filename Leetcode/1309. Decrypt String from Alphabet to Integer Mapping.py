

"""

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.



Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

"""

import re


def freqAlphabets(s: str):


    V = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f',
         '7': 'g', '8': 'h', '9': 'i','10': 'j', '11': 'k',
         '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p',
         '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u',
         '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}

    string = ''
    n = -1

    while abs(n+1) < len(s):
        if s[n] != "#":
            string = string + V.get(s[n])
            n = n - 1

        else:
            string = string + V.get(s[n-2:n])
            n = n - 3
    return string[::-1]

print(freqAlphabets("10#11#12"))
#jkab

print(freqAlphabets("1326#"))
#acz


t = ['1', '2', '3', '4', '5', '6', '7','8', '9','10#',
 '11#','12#', '13#', '14#', '15#', '16#', '17#',
  '18#', '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#']
  
q = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

V = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f',
     '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k',
     '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p',
     '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u',
     '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
