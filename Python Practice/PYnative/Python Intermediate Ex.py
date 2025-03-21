


"""Reverse each word of a string"""

str = 'My Name is Jessa'
str1 = str.split()

print(str1)
#['My', 'Name', 'is', 'Jessa']

list1 = []

for words in str1:
    a = words[::-1]
    list1.append(a)
    print(list1)
#['yM']
#['yM', 'emaN']
#['yM', 'emaN', 'si']
#['yM', 'emaN', 'si', 'asseJ']

print(" ".join(list1))
#yM emaN si asseJ




# Exercise to reverse each word  of a string
def reverse_words(Sentence):
    # Split string on whitespace
    words = Sentence.split(" ")

    # iterate list and reverse each word using ::-1
    new_word_list = [word[::-1] for word in words]

    # Joining the new list of words
    res_str = " ".join(new_word_list)
    return res_str


# Given String
str1 = "My Name is Jessa"
print(reverse_words(str1))

####################################################################

"""Assume you have a following text file (sample.txt)."""



####################################################################

"""In this question, You need to remove items from a list 
while iterating but without creating a different copy of a list.

Remove numbers greater than 50"""

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
len_number_list = len(number_list)

for index, nums in enumerate(number_list):
    if nums > 50:
        del number_list[index]
        print(index,nums)
#5 60
#6 80
#7 100

print(number_list)
#[10, 20, 30, 40, 50, 70, 90]

"""The problem is you removed a value from a list during iteration
 and then your list index will collapse."""

"""Reduce the list size!!! to break down the index while you delete"""

number_list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = len(number_list2)
i = 0
while x > i:
    x = x - 1
    if number_list2[x] > 50:
         del number_list2[x]

print(number_list2)





number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
# get list's size
n = len(number_list)
# iterate list till i is smaller than n
while i < n:
    # check if number is greater than 50
    if number_list[i] > 50:
        # delete current index from list
        del number_list[i]
        # reduce the list size
        n = n - 1
    else:
        # move to next item
        i = i + 1
print(number_list)


####################################################################

"""Reverse Dictionary mapping"""

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
y = list()
x = list()

for keys,values in ascii_dict.items():
    y.append(keys)
    x.append(values)
    z = zip(x,y)
    print(dict(z))
#{65: 'A'}
#{65: 'A', 66: 'B'}
#{65: 'A', 66: 'B', 67: 'C'}
#{65: 'A', 66: 'B', 67: 'C', 68: 'D'}

####################################################################


"""Display all duplicate items from a list"""

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

x = 0
y = len(sample_list)

count_dict = dict()

for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
        if item > 1:
            print(item)
    else:
        count_dict[item] = 1

#20
#30
#60

####################################################################

"""Filter dictionary to contain keys present in the given list
"""

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']

d2 = dict()

for keys,values in d1.items():
    if keys in l1:
        d2.update({keys:values})

print(d2)

####################################################################

"""Print the following number pattern
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 """

for nums in range(1,2):
    print(nums,nums,nums,nums,nums)
    for nums2 in range(2,3):
        print(nums2,nums2,nums2,nums2)
        for nums3 in range(3,4):
            print(nums3,nums3,nums3)

####################################################################

"""Modify the element of a nested list inside the following list"""

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]

#[5, [10, 15, [20, 25, [30, 3500], 40], 45], 50]

list1[1][2][2][1]=3500
print(list1)
#[5, [10, 15, [20, 25, [30, 3500], 40], 45], 50]

####################################################################

emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}
print(emp_dict['company']['employee']['payable']['increment'])
