


"""Given two lists, l1 and l2, write a program to create
a third list l3 by picking an odd element from
the list l1 and even elements from the list l2."""

l1 = [3, 6, 9, 12, 16, 17, 22]
l2 = [4, 7, 13, 16, 23, 24, 28]

l3 = []

def oddeven(l1,l2):
    for nums in l2:
        if nums % 2 == 0:
            l3.append(nums)
    for nums2 in l1:
        if nums2 % 2 == 0:
            pass
        else:
            l3.append(nums2)

oddeven(l1,l2)
print(l3)


####################################################################


"""Given two lists, l1 and l2, write a program to create
a third list l3 by picking an odd-index element from
the list l1 and even index elements from the list l2."""


l1 = [3, 6, 9, 12, 15, 18, 22]
l2 = [4, 7, 12, 16, 20, 24, 28]

l3 = []

def oddevenindex(l1,l2):
    x = l1[::2]
    z = list(set(l1)  - set(x))
    y = l2[::2]
    l3.append(z)
    l3.append(y)

oddevenindex(l1,l2)
print(l3)




list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)



####################################################################


"""Write a program to remove the item present at index 4 
and add it to the 2nd position and at the end of the list."""

list1 = [54, 44, 27, 79, 91, 41]

def remove(list1,a):
    del list1[4]
    list1.insert(-1,a)
    print(list1)

remove(list1,5)




sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)



####################################################################
