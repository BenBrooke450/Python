 



```python
####################################################################
###               Validating User Input
####################################################################

 

def user_choose():
    choice = "WRONG"
    while type(choice) != int:
        choice = input("Please enter a number between 0-10: ")
        try:
            return int(choice)
        except ValueError:
            print("Sorry that is not a digit")
    return choice
print(user_choose())

 

#Please enter a number between 0-10: five
#Sorry that is not a digit

#Please enter a number between 0-10: 6

6

 

####################################################################

 

 

 

while type(choice) != int:
    choice = input("Please enter a number between 0-10: ")
    try:
        a = int(choice)
        if type(a) == int and 0 < a < 10:
            return choice
        else:
            print("That is not within 0 to 10")
    except ValueError:
        print("Sorry that is not a digit")
return choice


print(user_choose())



#Please enter a number between 0-10: 11
That is not within 0 to 10

 

#Please enter a number between 0-10: five
Sorry that is not a digit

 

#Please enter a number between 0-10: 3
3

 

 

####################################################################



for index, nums in enumerate(prices):
    try:
        index_start = position_of_max + i

        max_num = max(prices[position_of_max + i:])
        position_of_max = prices.index(max_num,index_start)
        min_num = min(prices[position_of_min:position_of_max])
        position_of_min = prices.index(min_num,position_of_min)
        i = 1
        diff = max_num - min_num
        if diff > max_diff:
            max_diff = diff
    except ValueError as e:
        print(e)
        break
    else:
        pass
```
 

 