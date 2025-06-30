

"""

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]




Example 2:


Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30

"""


def generate(numRows: int) -> list[list[int]]:

    list1 = []

    def pas(first,incre,numRows):

        list1.append(first[:])
        first.append(incre)
        first = [1] + [sum(first[x:x+2]) for x in range(len(first)-1)]
        if len(list1) >= numRows:
            return list1
        else:
            pas(first,incre,numRows)

    pas(first = [1],incre = 0,numRows = numRows)

    return list1


print(generate(5))






















"""

def pas(num : int):

    list1 = [1,2,3]
    list2 = []
    i = 1

    for index,x in enumerate(list1):

        a = list1[0:i]
        list2.append(a)
        i = i + 1

        if len(list2) == num:
            break

    return list2


print(pas(3))


####################################################################

def pas(num : int):

    list1 = [1,2,3]
    list2 = []
    x = 0

    for x in list1:
        list2.append(list1)

        if len(list2) == num:
            break

    return list2


print(pas(3))
#[[1, 2, 3], [1, 2, 3], [1, 2, 3]]


####################################################################



def pas(num : int):

    list1 = [1]
    list2 = []
    list3 = []


    x = 0

    for x in list1:

        x =  x + 1

        list1.append(x)

        if len(list1) == num:
            break

    return list1


print(pas(3))
#[1, 2, 3]


####################################################################


list1 = [0,0,1,0,0]
list2 = []
i = 1
for index, x in enumerate(list1):

    if (index + 1) == len(list1):
        break

    else:
        y =  x + list1[index+i]
        list2.append(y)

print(list2)

####################################################################


print([[x, x + 1] for x in range(10)])
#[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]

"""