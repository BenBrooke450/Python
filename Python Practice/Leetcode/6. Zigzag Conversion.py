

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
    n = numRows * 2 - 2
    m = 0
    string_new = []
    visited = set()


    def swirling_wind(n,m):
        z = 1
        i = 0
        if len(string_new) >= len(s):
            return

        print("NEW")

        while i + m <= len(s):
            print(s[i+m],n,i,z)
            if m > 0 and m < len(s):
                if z%2 == 0 and (s[i+m],i) not in visited:
                    string_new.append(s[i+m+2])
                    print("NEW:",s[i+m+2], n, i+2, z)
                    i = i + 4
                    z = z + 1
                    continue
                else:
                    string_new.append(s[i+m])

            elif (s[i+m],i) not in visited:
                    string_new.append(s[i+m])

            visited.add((s[i],i))
            z = z + 1
            i = i + n

        n = n - 2
        m = m + 1


        swirling_wind(n,m)

    swirling_wind(n,m)

    return string_new, visited


print(convert(s = "PAYPALISHIRING", numRows = 4))







