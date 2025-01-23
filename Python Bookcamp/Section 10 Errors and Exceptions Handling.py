




####################################################################
#                      Errors and exceptions
####################################################################

def add(n1,n2):
    print(n1 + n2)


print(add(10,20))
30

number1 = 10
number2 =  input("Please provide a number: ")

#add(number1,number2)
"""TypeError: unsupported operand type(s) for +: 'int' and 'str'"""



####################################################################

try:

    result = 10 + "10"

except:
    print("Hey it looks like you aren´t adding correcly")

else:
    print("Add went well")
    print(result)

#Hey it looks like you aren´t adding correcly



####################################################################

try:

    result = 10 + 10

except:
    print("Hey it looks like you aren´t adding correcly")

else:
    print("Add went well")
    print(result)

#Add went well


####################################################################


def ask_for_int():
    try:
        result = int(input("Please provide number"))
        print(result)
    except:
        print("That´s not a number")
    finally:
        print("end of try/except/finally")

ask_for_int()
5
#end of try/except/finally




def ask_for_int():


    while True:

        try:
            result = int(input("Please provide number"))
            print(result)

        except:
            print("That´s not a number")
            continue

        else:
            print("Yes thank you")
            break

        finally:
            print("end of try/except/finally")
            print("I will always run at the end")


ask_for_int()


#Please provide numberfive
#That´s not a number
#end of try/except/finally
#I will always run at the end


#Please provide number5
5
#Yes thank you
#end of try/except/finally
#I will always run at the end
