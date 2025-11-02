

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

P   A   H    N
A P L S I  I G
Y   I   R

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

"""



def convert(s: str, numRows: int) -> str:









def convert(s: str, numRows: int) -> str:
    n = numRows * 2 - 2
    m = 0
    string_new = []

    def swirling_wind(n,m):
        z,i = 0
        if m >= numRows/2:
            z = 1

        if len(string_new) >= len(s):
            return string_new

        print("NEW-----------")

        while i + m < len(s):

            if m > 0 and m + 1 < numRows:
                if z%2 == 0:
                    string_new.append(s[i+m])
                    print("MID JUMP:",s[i+m], "BASE NUMBER:",n, f"  sum of {i} & {m}:",i+m, "  even or odd:",z)
                    z = z + 1
                    i = i + 4
                    print(i)
                    continue

                    #"PINALSIGYAHRPI"
                else:
                    string_new.append(s[i+m])
                    print("Normal:", s[i + m], f"  sum of {i} & {m}:", i + m, "  even or odd:",z)
                    z = z + 1
                    if z % 2 == 0:
                        i = i + 2
                    else:
                        i = i + n
                    print(i)
                    continue

            string_new.append(s[i + m])
            i = i + numRows * 2 - 2

        n = n - 2

        swirling_wind(n ,m + 1)

    swirling_wind(n,m)

    return string_new


print(convert(s = "PAYPALISHIRING", numRows = 6))







