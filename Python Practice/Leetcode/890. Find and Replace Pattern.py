
"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.



Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

Example 2:
Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
"""


def findAndReplacePattern(words: list[str], pattern: str) -> list[str]:
    set_pattern = [x for x in pattern]




    print(set_pattern)
    for i,x in enumerate(words):
        print("      ")
        print(x)
        list1 = []
        for y,j in zip(set_pattern,x):
            print("old: ",j, "new: ",y.upper(),x)
            if y.upper() in list1:
                continue
            else:
                y = y.upper()
                x = x.replace(j, y)
                print(x)
                list1.append(y.upper())
        print("now:",x.lower() , "  Pattern:",set_pattern)

        if x.lower()  != pattern:
            words[i] = ""

    return [x for x in words if x != ""]


print(findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))

#print(findAndReplacePattern(["abc","cba","xyx","yxx","yyx"],"abc"))


#print(findAndReplacePattern(["yzmyr","fhufq","lghlq","oahot","ueiuq"],"iusiq"))
