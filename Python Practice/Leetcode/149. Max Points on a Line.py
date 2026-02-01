





def maxPoints(points: list[list[int]]) -> int:

    m = 0
    nums = []
    grad = {}
    for i,x in enumerate(points):
        a = 0
        for y in points[i+1:]:

            if (y[0] - x[0]) == 0:
                g = 10000
            elif (y[1] - x[1]) == 0:
                g = 0
            else:
                g = (y[1] - x[1]) / (y[0] - x[0])

            print(g)

            if g not in grad.keys():
                grad[g] = 1
            else:
                grad[g] = grad[g] + 1

        if len(grad) != 0:
            m = max(grad.values())
        grad = {}
        nums.append(m+1)
        m = 0

    return nums

print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))




