from docutils.parsers.rst.directives import choice


def choice_player():

    choice = "PLACE HOLDER"

    while choice not in ["o","x"]:

        choice = input("Choose a player (o or x)?")

        if choice not in ["o","x"]:
            print("Please pick o or x")

        return choice




list = [0,1,2,3,4,5,6,7,8]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)




def player_position():

    choice = "PLACE HOLDER"

    while choice not in [0,1,2,3,4,5,6,7,8]:
        choice = input("Pick your number for position 0-8: ")
        choice = int(choice)

        if choice not in [0,1,2,3,4,5,6,7,8]:
            print("You must pick a number between 1 and 9: ")

        return choice



def game_keep_going():

    choice = "PLACE HOLDER"

    while choice not in ["Y","N"]:

        choice =  input("Keep playing? (Y of N) ")

        if choice not in ["Y","N"]:
            print("Sorry invalid choice! ")

    if choice == "Y":
        return True
    else:
        return False




list = [0,1,2,3,4,5,6,7,8]
game_on = True

while game_on:

    choice = choice_player()

    display_game(list)

    position = player_position()

    list[position] = choice

    display_game(list)

    game_on = game_keep_going()

#Choose a player (o or x)?o
#Here is the current list:
#[0, 1, 2, 3, 4, 5, 6, 7, 8]
#Pick your number for position 0-8: 3
#Here is the current list:
#[0, 1, 2, 'o', 4, 5, 6, 7, 8]
#Keep playing? (Y of N) Y



#Choose a player (o or x)?x
#Here is the current list:
#[0, 1, 2, 'o', 4, 5, 6, 7, 8]
#Pick your number for position 0-8: 0
#Here is the current list:
#['x', 1, 2, 'o', 4, 5, 6, 7, 8]
#Keep playing? (Y of N) N



from docutils.parsers.rst.directives import choice
import numpy as np




def choice_player():

    choice = "PLACE HOLDER"

    while choice not in ["o","x"]:

        choice = input("Choose a player (o or x): ")

        if choice not in ["o","x"]:
            print("Please pick o or x")

    return choice




board = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])


list = [0,1,2,3,4,5,6,7,8]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)






def player_position():

    choice = "PLACE HOLDER"

    while choice not in ["0","1","2","3","4","5","6","7","8"]:
        choice = input("Pick your number for position 0-8: ")

        if choice not in ["0","1","2","3","4","5","6","7","8"]:
            print("You must pick a number between 0 and 8: ")

    return int(choice)




def play_position_board(position):
    if   position == 0:
        return 0,0
    elif position == 1:
        return 0,1
    elif position == 2:
        return 0,2
    elif position == 3:
        return 1,0
    elif position == 4:
        return 1,1
    elif position == 5:
        return 1,2
    elif position == 6:
        return 2,0
    elif position == 7:
        return 2,1
    elif position == 8:
        return 2,2





def game_keep_going():

    choice = "PLACE HOLDER"

    while choice not in ["Y","N"]:

        choice =  input("Keep playing? (Y of N) ")

        if choice not in ["Y","N"]:
            print("Sorry invalid choice! ")

    if choice == "Y":
        return True
    else:
        return False


list = [0,1,2,3,4,5,6,7,8]
game_on = True


while game_on:

    choice = choice_player()

    display_game(board)

    position = player_position()

    board_position = play_position_board(position)

    board[board_position] =  choice

    display_game(board)

    game_on = game_keep_going()













































































