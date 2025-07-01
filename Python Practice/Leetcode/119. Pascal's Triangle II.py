

def getRow(numRows: int) -> list[list[int]]:

    list1 = []

    def pas(first,incre,numRows):

        list1.append(first[:])
        first.append(incre)
        first = [1] + [sum(first[x:x+2]) for x in range(len(first)-1)]
        if len(list1) - 1 >= numRows:
            return list1
        else:
            pas(first,incre,numRows)

    pas(first = [1],incre = 0,numRows = numRows)

    return list1[-1]


print(getRow(5))