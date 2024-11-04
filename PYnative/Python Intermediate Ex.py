


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


####################################################################


"""Display all duplicate items from a list"""

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

x = 0
y = len(sample_list)

def count_dub(sample_list):
    for
