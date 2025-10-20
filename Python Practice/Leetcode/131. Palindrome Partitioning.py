

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


    path_word = []
    all_words = []

    def word_back(letter_index:int(), path:list()):
        for i in range(letter_index, len(s)):

            path_word.append(s[i])
            print(path_word)

            word_back(i + 1, path_word)

            path_word.pop()

    word_back(0,[])

    return path_word


print(partition(s = "aabacba"))
















