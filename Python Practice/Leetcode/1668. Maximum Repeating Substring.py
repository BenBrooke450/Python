

"""
For a string sequence, a string word is k-repeating if
    word concatenated k times is a substring of sequence.
     The word's maximum k-repeating value is the highest
      value k where word is k-repeating in sequence.
       If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.



Example 1:
Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".

Example 2:
Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

Example 3:
Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".

"""


def maxRepeating(sequence: str, word: str) -> int:
    x = "_".join(sequence[::-1].split(word[::-1]))
    y = "_".join(sequence.split(word))
    m = 0
    f = 0
    for t in x:
        if t == "_":
            m = m + 1
            if m > f:
                f = m
        else:
            m = 0

    d = 0
    a = 0
    for t in y:
        if t == "_":
            d = d + 1
            if d > a:
                a = d
        else:
            d = 0

    return max(f,a)

print(maxRepeating(sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba", word = "aaaba"))
#(5, '_____baaa_', '__aaba____')


print(maxRepeating(sequence = "ababc", word = "ba"))
#(1, 'cb_a', 'a_bc')


print(maxRepeating(sequence = "ababc", word = "ab"))
#(2, 'c__', '__c')


