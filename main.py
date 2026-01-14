# MILESTONE PROJECT 2

# Importing necessary libraries
import random

# set Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

game_on = True

# contruct card class (This class creates an instance of each card and assigns it a value)
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# construct deck class (This class creates a deck of 52 cards using the Card class)
class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # create a Card object and add it to the deck

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle the deck

    def deal(self):
        return self.deck.pop()  # deal a card from the deck

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips

    def win_bet(self, amount):
        self.chips += amount

    def lose_bet(self, amount):
        self.chips -= amount

    def standoff_bet(self, amount):
        pass  # No change in chips for a standoff

    def place_bet(self, amount):
        pass

if __name__ == "__main__":

    while True:
        try:
            player_numbers = int(input("Please enter the number of players: 1-5\n"))
            if player_numbers > 5 or player_numbers < 1:
                print("Players must be between 1 and 5 inclusive\n")
            else:
                break
        except ValueError:
            print("Invalid number - Please enter an integer from 1 to 5\n")

    while game_on == True:
        new_deck = Deck()
        new_deck = new_deck.shuffle()
        players = [] # create a list of all players, and the house
        player = Player("House")
        players.append(player)
        for num in range(1, player_numbers):
            player = Player(f"Player {num}")
            players.append(player)
        print(players)
          #  while True: #
          #      try:
          #          bet = int(input("{player.name}, place bet"))






