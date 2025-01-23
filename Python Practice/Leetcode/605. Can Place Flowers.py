

"""


You have a long flowerbed in which some of the plots
are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
 return true if n new flowers can be planted in the flowerbed
  without violating the no-adjacent-flowers rule and false otherwise.



Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true


Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


"""


def canPlaceFlowers(flowerbed: list[int], k: int):

    n = 0

    if len(flowerbed) == 1 and flowerbed[0] == 0:
        return True

    for index, nums in enumerate(flowerbed[:-1]):
        if nums == 0 and index < 1:
            if flowerbed[index + 1] == 0 and index < 1:
                flowerbed[index] = 1
                n = n + 1

        elif nums == 0 and index != len(flowerbed) - 2:
            if flowerbed[index + 1] == 0 and flowerbed[index - 1] == 0:
                flowerbed[index] = 1
                n = n + 1

        elif flowerbed[len(flowerbed) - 2] == 0:
            if flowerbed[len(flowerbed) - 1] == 0:
                flowerbed[(len(flowerbed) - 1)] = 1
                n = n + 1

    if k <= n:
        return True
    else:
        return False


print(canPlaceFlowers([0,0,0,0,0],3))
#True


print(canPlaceFlowers([0,0,0],2))
#True
