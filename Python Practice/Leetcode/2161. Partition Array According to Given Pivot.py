
def pivotArray(nums: list[int], pivot: int) -> list[int]:
    list1 = []
    list2 = []
    list3 = []
    for x in nums:
        if x < pivot:
            list1.append(x)
        elif x > pivot:
            list2.append(x)
        elif x == pivot:
            list3.append(x)
    return list1 + list3 + list2