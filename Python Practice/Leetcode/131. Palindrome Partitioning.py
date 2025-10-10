

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.



Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


"""



















def partition(s: str) -> list[list[str]]:
    list1 = []

    for x in range(len(s)):
        for y in range(x+1, len(s)+1):  # include last character
            if s[x:y] == s[x:y][::-1] and len(s[x:y]) > 0:
                if x == 0:
                    list1.append([s[x:y]] + [ch for ch in s[y:]])
                else:
                    list1.append([ch for ch in s[:x]] + [s[x:y]] + [ch for ch in s[y:]])


    for q in list1.copy():
        for x in range(len(q)):
            for y in range(x + 1, len(q)+1):
                substring = ''.join(q[x:y])
                if len(substring) > 1 and substring == substring[::-1]:
                    if x == 0:
                        list1.append([substring] + q[y:])
                    else:
                        list1.append(q[:x] + [substring] + q[y:])

    list2 = []

    for x in list1:
        if x not in list2:
            list2.append(x)

    return list2





print(partition(s = "aabaabba"))













