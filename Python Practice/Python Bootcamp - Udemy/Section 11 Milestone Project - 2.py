import random

from astropy.io.fits import append
from sympy import list2numpy

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





def continue_playing():
    player = "PLACE HOLDER"

    while player not in ["y","n"]:
        player = input("Another card ? (y or n)")

        if player not in ["y","n"]:
            print("You must pick the yes or no")
        else:
            print("ok")

    return player



def another_card():
    player = "PLACE HOLDER"

    while player not in ["y","n"]:
        player = input("Another card ? (y or n)")

        if player not in ["y","n"]:
            print("You must pick the yes or no")
        else:
            print("ok")

    return player


class Deck:

    def __init__(self):
        self.all_cards = []
        for decks in range(0, 4):
            for suit in suits:
                for rank in ranks:
                    created_card = Card(suit,rank)
                    self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def remove_one(self):
        return self.all_cards.pop(0)





game_round = True


def game_round():

    Hand = []
    bot = []

    deck = Deck()

    deck.shuffle()

    begin_game = True

    while begin_game:

        deal = deck.remove_one()
        print("Your card:==",deal,"==")
        Hand.append(deal)

        list1 = []

        for cards in Hand:

            if another_card() == "y":
                pass
            else:
                break

        print("----------")
        list1.append(cards.value)
        cards_number = sum(list1)
        print("|Cards: ",cards," |Sum: ", cards_number)
        print("----------")

        if cards.rank != "Ace" and cards_number > 21:
            print("Out!")
            begin_game = False

        elif cards.rank == "Ace" and cards_number > 21:
            cards_number = cards_number - 10
            if cards_number > 21:
                print("Out!")
                bbegin_game = False
        elif cards_number == 21:
            print("WINN!!")
            begin_game = False

        else:
            begin_game = True






    Game = True

    while Game:
        deal = deck.deal_one()
        bot.append(deal)
        print(bot)

        cards_number_bot = 0

        list2 = []

        for cards in bot:
            list2.append(cards.value)
            cards_number_bot = sum(list2)

        if cards.rank != "Ace" and cards_number_bot > 21:
            print("Out!")

        elif cards.rank == "Ace" and cards_number_bot > 21:
            cards_number_bot = cards_number_bot - 10
            if cards_number_bot > 21:
                print("Out!")
                break
            print(bot, "You have: ", cards_number_bot)

        else:
            print(bot, "You have: ", cards_number_bot)







game_round()

####################################################################
#
####################################################################


