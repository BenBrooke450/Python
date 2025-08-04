

"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].ç

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

"""


def totalFruit(self, fruits: List[int]) -> int:
# Dictionary to keep track of the fruits in the current window
    fruit_counts = {}
    left = 0
    max_picked = 0

    # Iterate over the fruits with the right pointer
    for right, fruit in enumerate(fruits):
        # Add the current fruit to the dictionary
        if fruit in fruit_counts:
            fruit_counts[fruit] += 1
        else:
            fruit_counts[fruit] = 1

        # If there are more than two types of fruits, shrink the window from the left
        while len(fruit_counts) > 2:
            left_fruit = fruits[left]
            fruit_counts[left_fruit] -= 1
            if fruit_counts[left_fruit] == 0:
                del fruit_counts[left_fruit]
            left += 1

        # Update the maximum number of fruits picked
        max_picked = max(max_picked, right - left + 1)

    return max_picked


def totalFruit(fruits: list[int]) -> int:

    q = 2
    for i,x in enumerate(range(len(fruits))):
        y = tuple(fruits[i:i+2])
        print(y)
        t = 0
        for j in fruits[i+1:]:
            print("frontwards:",fruits[i+2:])
            if j in y:
                print(j,y)
                t = t + 1
                if t > q:
                    q = t
            else:
                break

        fruit_backwards = fruits[:i+1][::-1]
        print("backwards:",fruit_backwards)

        for j in fruit_backwards:
            if j in y:
                print(j,y)
                t = t + 1
                if t > q:
                    q = t
            else:
                break


    return q


print(totalFruit(fruits = [3,0,0,1,1,4,5,6]))

