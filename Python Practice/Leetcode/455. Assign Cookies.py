"""
Assume you are an awesome parent and want to give your
 children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum
 size of a cookie that the child will be content with; and
  each cookie j has a size s[j]. If s[j] >= g[i], we can
   assign the cookie j to the child i, and the child i will be content.
    Your goal is to maximize the number of your content children and output the maximum number.



Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.


Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.
"""





def cookies(g:list[int],s:list[int]):
    i = 0
    sorted_s = sorted(s)
    sorted_g = sorted(g)
    for index1, x in enumerate(sorted_s):
        for index2, y in enumerate(sorted_g):
            if x >= y and y > 0:
                sorted_g[index2] = 0
                i = i + 1
                print(sorted_g, sorted_s, )
                break

    return i

print(cookies([1,2,2,3,4,5,7,7,7,7,4,3,5,4,321],[1,2,3,7,7,7,7,4,4,412,31,4,1,241,5,1,2,3,123,13,1,5,5,5,5,53,33,3,3,22,1,1,1]))


