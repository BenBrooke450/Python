




import numpy as np
def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    list1 = []
    groupSizes = np.array(groupSizes)
    for x in set(groupSizes):
        list1.append([x,((np.nonzero(groupSizes == x))[0]).tolist()])

    list2 = []
    for x in list1:
        y = len(x[1])/x[0]
        list2.append(np.split(np.array(x[1]),y))

    flat = [item.tolist() for sublist in list2 for item in sublist]
    return flat

print(groupThePeople([3,3,3,3,3,1,3]))





