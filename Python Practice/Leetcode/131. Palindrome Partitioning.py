

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
            print("MAX OUTED - RETURN")
            return

        print(f"\n","---------NEW PASS-------",start_index,f"\n")
        for end_index in range(start_index, len(s)):
            print(start_index,end_index+1,len(s),s[start_index:end_index + 1])

            substring = s[start_index:end_index + 1]

            if substring == substring[::-1]:
                print("PASS: ",substring)
                path.append(substring)
                print(path, "LOOP +1")
                word_back(end_index + 1, path)
                path.pop()
                print("DROP BACK -- PATH:", path)

        print("DROP BACK OUT OF THE FUNCTION - remove another letter")

    word_back(0, [])
    return all_words

print(partition(s = "aabacba"))
"""
/opt/anaconda3/bin/python /Users/benjaminbrooke/PycharmProjects/Python/Python Practice/Leetcode/131. Palindrome Partitioning.py 

 ---------NEW PASS------- 0 

0 1 7 a
PASS:  a
['a'] LOOP +1

 ---------NEW PASS------- 1 

1 2 7 a
PASS:  a
['a', 'a'] LOOP +1

 ---------NEW PASS------- 2 

2 3 7 b
PASS:  b
['a', 'a', 'b'] LOOP +1

 ---------NEW PASS------- 3 

3 4 7 a
PASS:  a
['a', 'a', 'b', 'a'] LOOP +1

 ---------NEW PASS------- 4 

4 5 7 c
PASS:  c
['a', 'a', 'b', 'a', 'c'] LOOP +1

 ---------NEW PASS------- 5 

5 6 7 b
PASS:  b
['a', 'a', 'b', 'a', 'c', 'b'] LOOP +1

 ---------NEW PASS------- 6 

6 7 7 a
PASS:  a
['a', 'a', 'b', 'a', 'c', 'b', 'a'] LOOP +1
MAX OUTED - RETURN
DROP BACK -- PATH: ['a', 'a', 'b', 'a', 'c', 'b']
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a', 'a', 'b', 'a', 'c']
5 7 7 ba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a', 'a', 'b', 'a']
4 6 7 cb
4 7 7 cba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a', 'a', 'b']
3 5 7 ac
3 6 7 acb
3 7 7 acba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a', 'a']
2 4 7 ba
2 5 7 bac
2 6 7 bacb
2 7 7 bacba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a']
1 3 7 ab
1 4 7 aba
PASS:  aba
['a', 'aba'] LOOP +1

 ---------NEW PASS------- 4 

4 5 7 c
PASS:  c
['a', 'aba', 'c'] LOOP +1

 ---------NEW PASS------- 5 

5 6 7 b
PASS:  b
['a', 'aba', 'c', 'b'] LOOP +1

 ---------NEW PASS------- 6 

6 7 7 a
PASS:  a
['a', 'aba', 'c', 'b', 'a'] LOOP +1
MAX OUTED - RETURN
DROP BACK -- PATH: ['a', 'aba', 'c', 'b']
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a', 'aba', 'c']
5 7 7 ba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a', 'aba']
4 6 7 cb
4 7 7 cba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['a']
1 5 7 abac
1 6 7 abacb
1 7 7 abacba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: []
0 2 7 aa
PASS:  aa
['aa'] LOOP +1

 ---------NEW PASS------- 2 

2 3 7 b
PASS:  b
['aa', 'b'] LOOP +1

 ---------NEW PASS------- 3 

3 4 7 a
PASS:  a
['aa', 'b', 'a'] LOOP +1

 ---------NEW PASS------- 4 

4 5 7 c
PASS:  c
['aa', 'b', 'a', 'c'] LOOP +1

 ---------NEW PASS------- 5 

5 6 7 b
PASS:  b
['aa', 'b', 'a', 'c', 'b'] LOOP +1

 ---------NEW PASS------- 6 

6 7 7 a
PASS:  a
['aa', 'b', 'a', 'c', 'b', 'a'] LOOP +1
MAX OUTED - RETURN
DROP BACK -- PATH: ['aa', 'b', 'a', 'c', 'b']
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['aa', 'b', 'a', 'c']
5 7 7 ba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['aa', 'b', 'a']
4 6 7 cb
4 7 7 cba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['aa', 'b']
3 5 7 ac
3 6 7 acb
3 7 7 acba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: ['aa']
2 4 7 ba
2 5 7 bac
2 6 7 bacb
2 7 7 bacba
DROP BACK OUT OF THE FUNCTION - remove another letter
DROP BACK -- PATH: []
0 3 7 aab
0 4 7 aaba
0 5 7 aabac
0 6 7 aabacb
0 7 7 aabacba
DROP BACK OUT OF THE FUNCTION - remove another letter
[['a', 'a', 'b', 'a', 'c', 'b', 'a'], ['a', 'aba', 'c', 'b', 'a'], ['aa', 'b', 'a', 'c', 'b', 'a']]

Process finished with exit code 0
"""














