



def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


print(create_cubes(10))
#[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



for x in create_cubes(10):
    print(x)
0
1
8
27
64
125
216
343
512
729


####################################################################




def create_cubes(n):
    for x in range(n):
        yield x**3

print(create_cubes(10))
#<generator object create_cubes at 0x1027ef920>

for x in create_cubes(10):
    print(x)

1
8
27
64
125
216
343
512
729




print(list(create_cubes(10)))
#[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



####################################################################





def gen_fibon(n):


    a = 1
    b = 1

    for i in range(n):
        yield  a
        a, b = b, a+b

for number in gen_fibon(10):
    print(number)
1
1
2
3
5
8
13
21
34
55



####################################################################




def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

0
1
2


g = simple_gen()

print(g)
#<generator object simple_gen at 0x102a08d00>

print(next(g))
0

print(next(g))
1



####################################################################


s = 'hello'

for letter in s:
    print(letter)
#h
#e
#l
#l
#o



s_inter = iter(s)

print(next(s_inter))
#h

