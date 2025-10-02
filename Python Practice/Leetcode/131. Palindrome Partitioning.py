

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
    list1.append([x for x in s])


    def loop(s: list[str]):

        for i in range(len(s)):
            for j in range(1, len(s)):

                t = s[i:j]

                print(i, j, t, "    ", t[::-1])

                if t == t[::-1]:

                    list1.append(s[i:j])

                    loop(s[j:])



    loop(s)

    return list1

print(partition(s = "aab"))













