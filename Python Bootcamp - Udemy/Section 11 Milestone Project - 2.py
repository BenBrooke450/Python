from sympy.core.random import shuffle, choice

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5,
          'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12,
          'King':13, 'Ace':14}


class Card:
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

Card1 = Card(suit = "Hearts",rank= "Two",value = 2)

print(Card1.__str__())
#Two of Hearts







deck = []

def all():
    for suit in suits:
        for rank in ranks:
            deck.append(rank +" of "+ suit)
    print(deck)




all()
['Two of Hearts', 'Three of Hearts', 'Four of Hearts',
 'Five of Hearts', 'Six of Hearts', 'Seven of Hearts',
 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts',
 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
 'Ace of Hearts', 'Two of Diamonds', 'Three of Diamonds',
 'Four of Diamonds', 'Five of Diamonds', 'Six of Diamonds',
 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds',
 'Ten of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
 'King of Diamonds', 'Ace of Diamonds', 'Two of Spades',
 'Three of Spades', 'Four of Spades', 'Five of Spades',
 'Six of Spades', 'Seven of Spades', 'Eight of Spades',
 'Nine of Spades', 'Ten of Spades', 'Jack of Spades',
 'Queen of Spades', 'King of Spades', 'Ace of Spades',
 'Two of Clubs', 'Three of Clubs', 'Four of Clubs',
 'Five of Clubs', 'Six of Clubs', 'Seven of Clubs',
 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs',
 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs']


print(len(deck))
52

shuffle(deck)

print(deck)
#['Jack of Clubs', 'Four of Spades', 'Jack of Hearts'....

print(type(deck))
#<class 'list'>


deck1 = deck[0:25]
deck2 = deck[26:52]



def pickplayer():

    player = "PLACE HOLDER"

    while player not in ["player1","player2"]:
        player = input("Please pick player1 or player2")

        if player not in ["player1","player2"]:
            print("You must pick the player1 or player2")
        else:
            print("Let the game begin")

    return player



def Game_mechanics_player1(num):
    while True:
        print("Please pick a card dec1",num)
        user_input = input(f"Enter a card from dec1: ")
        if user_input in num:
            return user_input
        else:
            print("Invalid input. Please try again.")


def Game_mechanics_player2():
    while True:
        print(deck2)
        user_input = input(f"Enter a card from dec2: ")
        if user_input in deck2:
            return user_input
        else:
            print("Invalid input. Please try again.")


def startgame():

    deck1 = deck[0:25]
    deck2 = deck[26:52]

    all()

    end = True

    player = pickplayer()

    if player == "player1":
        print("player1 has cards:")
        while end:
            a = Game_mechanics_player1(deck1)
            str_of_a = str(a)
            b = choice(deck2)
            print("player2 choses: ",b)
            str_of_b = str(b)
            c = str(a.split()[0])
            x = values.get(c)
            d = str(b.split()[0])
            y = values.get(d)
            if x > y:
                deck1.append(str_of_b)
                deck2.remove(str_of_b)
                print(f"Player 1 wins the card!, they add {b} to their deck")
                print(f"player 2 looses {b}")
                print("Deck1: ",deck1)
                print("Deck2: ",deck2)

            elif x < y:
                deck2.append(str_of_a)
                deck1.remove(str_of_a)
                print(f"Player 2 wins the card!, they add {a} to their deck")
                print(f"player 1 looses {a}")
                print("Deck2: ",deck2)
                print("Deck1: ",deck1)

            elif x == y:
                print("They are the same, try again")

            elif len(deck1) == 0 or len(deck2) == 0:
                print("Game over")
                end = False






    elif player == "player2":
        print("player2 has cards:")
        while True:
            a = Game_mechanics_player2()
            print("player2 choses")
            b = choice(deck1)
            print(b)
            c = a.split(" ", 1)
            print(c)
            values.get(c)
            d = b.split(" ", 1)
            values.get(d)
            if c > d:
                deck2.append(a)
            elif d < c:
                deck1.append(d)
            else:
                print("They are the same, try again")
                pass
    else:
        print("No player chosen")


startgame()










