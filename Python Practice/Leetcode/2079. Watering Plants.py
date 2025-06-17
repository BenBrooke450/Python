





def wateringPlants(plants: list[int], capacity: int) -> int:
    steps = 0
    i = 0
    z = capacity
    while i != len(plants):

        if capacity >= plants[i]:
            capacity = capacity - plants[i]
            steps = steps + 1

        elif capacity < plants[i]:
            steps = steps + (i) * 2
            capacity = z
            steps = steps + 1
            capacity = capacity - plants[i]

        i = i + 1

    return steps


print(wateringPlants(plants = [1,1,1,4,2,3], capacity = 4))







