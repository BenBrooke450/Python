


####################################################################
#                      Validating User Input
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



def user_choose():

    choice = "PLACE HOLDER" #OR choice = ""

    #TWO CONDITIONS TO CHECK
    #MAKE SURE IS AN INTREGER OR WITHIN RANGE

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
#Please enter a number between 0-10: 8
8


####################################################################
#                      Simple User Interaction
####################################################################

game_list = [1,2,3]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

display_game(game_list)
#Here is the current list:
#[1, 2, 3]




def position_choice():

    choice = "PLACE HOLDER"

    while choice not in [0,1,2]:

        choice =  input("Pick a postion (0,1,2): ")

        if choice not in ["0","1","2"]:
            print("Sorry invalid choice! ")

        return int(choice)

position_choice()
#Pick a postion (0,1,2): 2



def replacement_choice(game_list,position):

    user_placement =input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list

print(replacement_choice(game_list,1))
#Type a string to place at position: hello
#[1, 'hello', 3]





def game_choice():

    choice = "PLACE HOLDER"

    while choice not in ["Y","N"]:

        choice =  input("Keep playing? (Y of N) ")

        if choice not in ["Y","N"]:
            print("Sorry invalid choice! ")

    if choice == "Y":
        return True
    else:
        return False

print(game_choice())






game_on = True
game_list = [0,1,2]

while game_on:  #Or while game_on == True

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = game_choice()

#Pick a postion (0,1,2): 1
#Type a string to place at position: E
#Here is the current list:
#['G', 'E', 'N']

#Keep playing? (Y of N) Y
#Here is the current list:
#['G', 'E', 'N']

#Pick a postion (0,1,2): 0
#Type a string to place at position: B
#Here is the current list:
#['B', 'E', 'N']

#Keep playing? (Y of N) N



