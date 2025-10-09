

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.



Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


"""


from itertools import combinations, permutations

def partition(s: str) -> list[list[str]]:

    list1 = []

    for x in range(len(s)):
        for y in range(x+1,len(s)):
            if s[x:y] == s[x:y][::-1] and len(s[x:y])>1:
                if len(s[:x]) == 0:
                    list1.append([s[x:y].split(",")[0]] + [x for x in s[y:]])
                else:
                    list1.append([x for x in s[:x]] + [s[x:y].split(",")[0]] + [x for x in s[y:]])

    for q in list1:
        for x in range(len(q)):
            for y in range(x + 1, len(q)):

                if len(q[x]) > 1:
                    break

                if q[x:y] == q[x:y][::-1] and len(q[x:y]) > 1:
                    if len(q[:x]) == 0:
                        list1.append([q[x:y].split(",")[0]] + [x for x in q[y:]])
                    else:
                        list1.append([x for x in q[:x]] + [q[x:y].split(",")[0]] + [x for x in q[y:]])


    return list1


print(partition(s = "aabaabba"))













