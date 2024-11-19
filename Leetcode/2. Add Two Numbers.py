"""You are given two non-empty linked lists representing
 two non-negative integers. The digits are stored in
 reverse order, and each of their nodes contains a
 single digit. Add the two numbers and return the
 sum as a linked list.

You may assume the two numbers do not contain any
leading zero, except the number 0 itself."""


list1 = [3,0,4]
list2 = [2,5,3]

list3 = [0]
list4 = [0]

list5 = [9,9,9,9,9,9,9]
list6 = [9,9,9,9]

def reverse_add(list1: list[int], list2: list[int]):
    list3 = []
    for item1, item2 in zip(list1[::-1], list2[::-1]):
        list3.append(item1 + item2)
    return list3

print(reverse_add(list1,list2))
#[7, 5, 5]

print(reverse_add(list3,list4))
#[0]

print(reverse_add(list5,list6))
#[18, 18, 18, 18]

#WRONG




def reverse_add_2(list1: list[int], list2: list[int]):
    list1_string = int("".join(str(item) for item in list1))
    list2_string = int("".join(str(item) for item in list2))
    sum_list = str(list1_string + list2_string)
    reverse_list = [int(item) for item in sum_list[::-1]]
    return reverse_list

print(reverse_add_2(list1,list2))
#[7, 5, 5]

print(reverse_add_2(list3,list4))
#[0]


print(reverse_add_2(list5,list6))








class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverse_add_2(list1: list[int], list2: list[int]):
        list1_string = int("".join(str(item) for item in list1))
        list2_string = int("".join(str(item) for item in list2))
        sum_list = str(list1_string + list2_string)
        reverse_list = [int(item) for item in sum_list[::-1]]
        return reverse_list