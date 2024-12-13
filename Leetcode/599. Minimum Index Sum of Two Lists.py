"""


Given two arrays of strings list1 and list2,
 find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum
is a common string such that if it
appeared at list1[i] and list2[j]
then i + j should be the minimum
value among all the other common strings.

Return all the common strings
with the least index sum. Return the answer in any order.



Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

Output: ["Shogun"]
Explanation: The only common string is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".

"""



def name(nums1:list[str],nums2:list[str]):

    dic1 = {}

    for index, words in enumerate(nums1):

        if words in nums2:

            index_two = nums2.index(words)

            if (index + index_two) in dic1:

                dic1[index + index_two] = dic1.get(index + index_two) + ',' + words

            else:
                dic1[index + index_two] = words

    return (dic1.get(min(dic1.keys()))).split(",")


print(name(["happy","sad","good"], ["sad","happy","good"]))
#['happy', 'sad']



###################################################


import numpy as np


def name(nums1:list[str],nums2:list[str]):

    array1 = np.array(nums1)

    array2 = np.array(nums2)

    list3 = np.intersect1d(array1,array2).tolist()

    list4 = []

    for strings in list3:
        index_array1  = nums1.index(strings)
        index_array2 =  nums2.index(strings)
        number = index_array1 + index_array2
        list4.append(number)

    return list4




print(name(["happy","sad","good"], ["sad","happy","good"]))












