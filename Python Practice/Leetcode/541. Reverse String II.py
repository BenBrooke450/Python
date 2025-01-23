


"""


Given a string s and an integer k, reverse the
first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left,
reverse all of them. If there are less than
2k but greater than or equal to k characters,
then reverse the first k characters and leave the other as original.



Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"


"""


def reverse_two(string: str, k: int):
    n = 0

    list1 = []

    for index, letters in enumerate(string):

        if index % 2 == 0:
            double = string[n: n + k]
            list1.append(double[::-1])
            n = n + k

        else:
            double = string[n: n + k]
            list1.append(double)
            n = n + k

    return "".join(list1)


print(reverse_two("abcdefg", 2))
#bacdfeg








######################################################################



def reverse_two(string:str, k:int):

    n = 0

    list1 = []

    for letters in string:

        double = string[n : n + k]

        list1.append(double)

        n = n + k

    return "".join(x[::-1] for x in list1)



print(reverse_two("abcdefg",  2))
#badcfeg

