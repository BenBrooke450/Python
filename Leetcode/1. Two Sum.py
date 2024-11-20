"""Given an array of integers nums and an
integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have
exactly one solution, and you may not use
the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]"""

nums = [2,7,11,15]
target = 9

nums2 = [2,3,4,5]
target2 = 8

nums3 = [3,2,4]
target3 = 6

nums4 = [3,3]
target4 = 6

nums5 = [1]
target5 = 4


nums6 = list(range(0,10000))
target6 = 19999
[9998,9999]



def twosums(nums: list[int],target: int):
    if (-10)**9 <= target <= (10)**9:
        j = 0
        for index1,num in enumerate(nums):
            back = nums[j]
            j = j + 1
            for index2,num2 in enumerate(nums):
                if num2 + back == target and index1 != index2:
                    list_index = [index1, index2]
                    return print(list_index)


twosums(nums,target)


####################################################################
#                           HASHMAP
####################################################################



def twosum(nums : list[int] , target: int):

    prevMap = {} #val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            #first 8 - 2 = 6 so is 6 [prevMap[6] in the dictionary ?
            #Second 8 - 3 = 5,so is 5 [prevMap[5] in the dictionary ?
            #....
            return [prevMap[diff], i]
        # if it´s not in the dic then we add it
        prevMap[n] = i
        print(prevMap)


"""

SO BASICALLY WE START BY RUNNING THROUGH EACH NUMBER
FINDING THE DIFFERENCE, EACH TIME THE DIFFERENCE IS
FOUND WE THEN LOOK (WITHIN THE NEXT LINE) IF THAT 
NUMBER EXISTS WITHIN THE LIST GIVEN THEN THERE HAS TO BE A SOLUTION.

AS THE 
   diff = target - n  =>  diff + n = target
SO IF n AND diff EXISTS THEN THERE IS A SOLUTION 

"""

nums2 = [2,3,4,5]
target2 = 8

twosum(nums2,target2)
#[1, 3]



















