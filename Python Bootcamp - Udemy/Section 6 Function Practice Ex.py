

"""

WARMUP SECTION:

LESSER OF TWO EVENS: Write a function that returns
the lesser of two given numbers if both numbers are even,
 but returns the greater if one or both numbers are odd

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
 """
from numba.cpython.unicode import join_list
from sympy import false


def lesser_of_two(a,b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a,b))
    else:
        print(max(a,b))


lesser_of_two(2,6)
2

lesser_of_two(5,2)
5

####################################################################

"""ANIMAL CRACKERS: Write a function takes a two-word string 
and returns True if both words begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False

"""

def animal_cracker(words):
    word = words.split(" ")
    a = word[0][0]
    b = word[1][0]
    if a == b:
        print(True)
    else:
        print(False)

animal_cracker('Levelheaded Llama')
#True

animal_cracker('Crazy Kangaroo')
#False

####################################################################


"""MAKES TWENTY: Given two integers, return True if the sum 
of the integers is 20 or if one of the integers is 20. 
If not, return False


makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""

def twenty(a,b):
    if a == 20 or b == 20:
        return True
    elif a + b == 20:
        return True
    else:
        return False

print(twenty(20,3))
#True

print(twenty(10,10))
#True

print(twenty(5,17))
#False

####################################################################

"""LEVEL 1 PROBLEMS

OLD MACDONALD: Write a function that capitalizes the
 first and fourth letters of a name
 
 old_macdonald('macdonald') --> MacDonald
 
 """

def old_macdonald(word):
    for index, letter in enumerate(word):
        if index == 0:
            a = letter.upper()
            print(a,index)
        elif index == 3:
            b = letter.upper()
            print(b,index)
        else:
            print(letter)

old_macdonald("hellooo")
#H 0
#e
#l
#L 3
#o
#o
#o



def old_macdonald(word):
    for index, letter in enumerate(word):
        if index == 0:
            letter = letter.upper()
            print(letter)
        elif index == 3:
            letter = letter.upper()
            print(letter)
        else:
            print(letter)
    print(word)

old_macdonald("Helloo")
#H
#e
#l
#L
#o
#o
#Helloo

####################################################################

"""MASTER YODA: Given a sentence, return a sentence
 with the words reversed
 
 master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
 
 """

def master_yode(sentence):
    index = sentence.split(" ")
    a = index[2]
    b = index[1]
    c = index[0]
    print(a,b,c)

master_yode("Hello to everyone")

#OR

def master_yoda(text):
    return ' '.join(text.split()[::-1])

####################################################################

"""ALMOST THERE: Given an integer n, return True 
if n is within 10 of either 100 or 200

almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True


NOTE: abs(num) returns the absolute value of a number"""

def almost(num):
    if 90 < num < 110 or 190 < num < 210:
        print(True)
    else:
        print(False)

almost(98)
#True

almost(130)
#False


####################################################################

"""LEVEL 2 PROBLEMS

FIND 33:

Given a list of ints, return True if the 
array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

"""

def has_33(list):
    i = 0
    j = len(list) - 1
    while i < j:
        i = i + 1
        if list[i-1] == list[i]:
            print("True Has33")
            break



has_33([1, 3, 3])
#True

has_33([1,3,2,3,4,5,3,3])
#True

has_33([1,3,1])


####################################################################


"""
PAPER DOLL: Given a string, return a string where
 for every character in the original there are three characters
 
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

"""

def three(string):
    list = []
    for letters in string:
         three = letters + letters + letters
         list.append(three)

    print("".join(list))

three("Hello")
#HHHeeellllllooo

####################################################################

"""
BLACKJACK: Given three integers between 1 and 11, 
if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 ç
and there's an eleven, reduce the total sum
 by 10. Finally, if the sum (even after adjustment)
  exceeds 21, return 'BUST'
  
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19

"""
def blackjack(a,b,c):
    if (a != 11 and b != 11 and c != 11) and a + b + c > 21:
        print("BUST!")
    elif (a == 11 or b < 11 or c < 11) and a + b + c > 21:
        print(1 + b + c)
    elif (a < 11 or b == 11 or c < 11) and a + b + c > 21:
        print(1 + a + c)
    elif (a < 11 or b < 11 or c == 11) and a + b + c > 21:
        print(1 + a + b)
    elif (a <= 11 or b <= 11 or c <= 11) and a + b + c <= 21:
        print(a+b+c)

blackjack(1,2,3)
#6

blackjack(1,11,3)
#15

blackjack(11,11,3)
#15

blackjack(10,10,1)
#21

blackjack(10,10,10)
#BUST!


####################################################################

"""SUMMER OF '69: Return the sum of the numbers in the 
array, except ignore sections of numbers starting with
 a 6 and extending to the next 9 (every 6 will be followed
  by at least one 9). Return 0 for no numbers.
  
  
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14

"""

## COULD NOT COMPLETE BECAUSE i´M STUPID
def summer_69(list):
    list = []
    for index, nums in enumerate(list):
        if nums != 6:
            list.append(nums)
        elif nums == 6:
            break
        elif nums == 9:
            continue
    print(list)

summer_69([2, 1, 6, 9, 11])

#ANSWER GIVEN
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

####################################################################


"""CHALLENGING PROBLEMS
SPY GAME: Write a function that takes in a list of 
integers and returns True if it contains 007 in order

 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
 
 """

def spy(nums):
    i = 0
    list = []
    for index, num in enumerate(nums):
        x = index
        y = index + 3
        list.append(nums[x:y])
    print(list)

spy([1,2,4,0,0,7,5])
#[[1, 2, 4], [2, 4, 0], [4, 0, 0], [0, 0, 7], [0, 7, 5], [7, 5], [5]]



def spy(nums):
    i = 0
    list = []
    for index, num in enumerate(nums):
        x = index
        y = index + 3
        list.append(nums[x:y])
    if [0,0,7] in list:
        print(True)
    else:
        print("NOO")

spy([1,7,2,0,0,0,7])
#True

spy([1,7,2,0,0,0,4])
#NOO

####################################################################

"""COUNT PRIMES: Write a function that returns the
 number of prime numbers that exist up to and including 
 a given number
 
count_primes(100) --> 25"""

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
