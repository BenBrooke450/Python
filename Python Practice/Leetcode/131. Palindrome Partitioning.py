

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

    all_words = []

    def word_back(start_index: int, path: list):

        if start_index == len(s):
            all_words.append(path.copy())
            return


        for end_index in range(start_index, len(s)):
            print(start_index,end_index+1)

            substring = s[start_index:end_index + 1]
            print("NONPASS: ", substring)

            if substring == substring[::-1]:
                print("PASS: ",substring)
                path.append(substring)
                print(path)
                word_back(end_index + 1, path)
                path.pop()
                print("DROP BACK -- PATH:", path)

        print("DROP BACK")

    word_back(0, [])
    return all_words



print(partition(s = "aabacba"))
















