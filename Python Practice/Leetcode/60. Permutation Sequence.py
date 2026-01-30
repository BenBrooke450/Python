







from itertools import permutations

def getPermutation(n: int, k: int) -> str:

    num = range(1,n+1)

    perm_num = permutations(num,n)

    return "".join([str(x) for x in list(perm_num)[k-1]])


print(getPermutation(4,9))


