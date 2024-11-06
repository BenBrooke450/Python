
"""Use for, .split(), and if to create a Statement
that will print out words that start with 's':"""


st = 'Print only the words that start with s in this sentence'
splitstr = st.split(" ")

for words in splitstr:
    if words[0] == "s":
        print(words)

####################################################################

"""Use range() to print all the even numbers from 0 to 10."""

list = list(range(0,10,2))
print(list)

[0, 2, 4, 6, 8]

####################################################################

"""Use a List Comprehension to create a list of all 
numbers between 1 and 50 that are divisible by 3."""

list = [print(nums) for nums in range(1,50) if nums%3==0]

3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48

####################################################################

"""Go through the string below and if the length of a 
word is even print "even!"""

st = 'Print every word in this sentence that has an even number of letters'

splitstr = st.split(" ")
for word in splitstr:
    ev = len(word)
    if ev % 2 == 0:
        print(word)
#word
#in
#this
#sentence
#that
#an
#even
#number
#of

####################################################################

"""Use List Comprehension to create a list of the first 
letters of every word in the string below:"""

st = 'Create a list of the first letters of every word in this string'
sts = st.split()

list = [words[0] for words in sts]

print(list)

#['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']
