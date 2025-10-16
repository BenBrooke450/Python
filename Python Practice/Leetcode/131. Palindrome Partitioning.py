

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


    p_word = []
    all_words = []

    def word(word:str(), letter_index:int()):


        l = s[letter_index]























