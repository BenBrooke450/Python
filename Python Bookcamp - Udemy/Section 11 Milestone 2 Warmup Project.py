import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5,
          'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12,
          'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


three_of_clubs = Card(suit = "Clubs", rank = "Three")

print(three_of_clubs)
#Three of Clubs

print(three_of_clubs.rank)
#Three



two_hearts = Card("Heart","Two")

print(two_hearts.suit)
#Heart

print(two_hearts.rank)
#Two







####################################################################






class Deck():


    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()



new_deck = Deck()



second_deck = Deck()

print(new_deck.all_cards[0])
#Two of Hearts

print(new_deck.all_cards[1])
#Three of Hearts




second_deck.shuffle()

print(second_deck.all_cards[0])
#Seven of Spades

print(len(second_deck.all_cards))
52




for card in new_deck.all_cards:
    print(card)

"""
Two of Hearts
Three of Hearts
Four of Hearts
Five of Hearts
Six of Hearts
Seven of Hearts
Eight of Hearts
Nine of Hearts
Ten of Hearts
Jack of Hearts
Queen of Hearts
King of Hearts
Ace of Hearts
Two of Diamonds
Three of Diamonds
Four of Diamonds
Five of Diamonds
Six of Diamonds
Seven of Diamonds
Eight of Diamonds
Nine of Diamonds
Ten of Diamonds
Jack of Diamonds
Queen of Diamonds
King of Diamonds
Ace of Diamonds
Two of Spades
Three of Spades
Four of Spades
Five of Spades
Six of Spades
Seven of Spades
Eight of Spades
Nine of Spades
Ten of Spades
Jack of Spades
Queen of Spades
King of Spades
Ace of Spades
Two of Clubs
Three of Clubs
Four of Clubs
Five of Clubs
Six of Clubs
Seven of Clubs
Eight of Clubs
Nine of Clubs
Ten of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs
Ace of Clubs
"""






####################################################################







class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"player {self.name} has {len(self.all_cards)} cards"

Ben = Player("ben")


print(Ben)
#player ben has 0 cards


Ben.add_cards("big fat card")

print(Ben.all_cards)
['big fat card']

print(Ben)
#player ben has 1 cards


print(Ben)
#player ben has 0 cards







####################################################################



player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(player_one)
#player one has 26 cards

print(len(player_one.all_cards))
26




####################################################################




game_on = True
round = 0


while game_on:

    round += 1
    print(f"Round {round}")

    if len(player_one.all_cards) == 0:
        print("no cards, no game, player one loses")
        game_false = False
        break

    if len(player_two.all_cards) == 0:
        print("no cards, no game, player two loses")
        game_false = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 7:

                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 7:

                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
                # Otherwise, we're still at war, so we'll add the next cards

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

"""
Round 1
Round 2
Round 3
Round 4
Round 5
Round 6
Round 7
Round 8
Round 9
Round 10
Round 11
Round 12
Round 13
Round 14
Round 15
Round 16
Round 17
Round 18
Round 19
Round 20
Round 21
WAR!
Round 22
Round 23
Round 24
Round 25
Round 26
Round 27
WAR!
Round 28
Round 29
Round 30
Round 31
WAR!
WAR!
Round 32
Round 33
Round 34
Round 35
Round 36
Round 37
Round 38
Round 39
WAR!
Round 40
Round 41
Round 42
Round 43
Round 44
Round 45
Round 46
Round 47
Round 48
Round 49
Round 50
Round 51
Round 52
Round 53
Round 54
Round 55
Round 56
Round 57
Round 58
Round 59
Round 60
Round 61
Round 62
Round 63
Round 64
Round 65
Round 66
Round 67
Round 68
Round 69
Round 70
Round 71
Round 72
Round 73
Round 74
Round 75
WAR!
Round 76
Round 77
Round 78
Round 79
Round 80
WAR!
Round 81
Round 82
Round 83
Round 84
Round 85
Round 86
Round 87
Round 88
Round 89
Round 90
Round 91
Round 92
Round 93
WAR!
Round 94
Round 95
Round 96
Round 97
Round 98
WAR!
Round 99
Round 100
Round 101
Round 102
Round 103
Round 104
Round 105
Round 106
Round 107
Round 108
Round 109
Round 110
Round 111
Round 112
Round 113
WAR!
Player Two unable to play war! Game Over at War
Player One Wins! Player One Loses!
"""

####################################################################
#HOW TO DO IT IN THE ACTUAL COURSE WITH CLASSES
####################################################################





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

    else:
        print("Player 2 is a bot, you need to pick player 1! :)")


startgame()



















