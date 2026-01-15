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
    def __init__(self, name, chips = 1000):
        self.name = name
        self.chips = chips
        self.bet = 0
        self.hand = []

    def win_bet(self, amount):
        self.chips += (amount * 2) # get back your bet + winnings

    def standoff_bet(self, amount):
        self.chips += amount  # Get back your bet only

    def place_bet(self, amount):
        self.bet = 0
        self.chips -= amount # take bet out of chips
        self.bet = amount # store bet

    def hand_value(self):
        total = 0
        aces = 0

        for card in self.hand:
            total += card.value
            if card.rank == 'Ace':
                aces += 1

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self, x, hide_first_card=False):
        if hide_first_card and self.name == "House" and x == 0:
            return f"[Hidden card]" # show second card only
        elif hide_first_card and self.name == "House" and x == 1:
            return f"[Hidden], {self.hand[1]}" # show second card
        else:
            return ', '.join(str(card) for card in self.hand)

    def __str__(self):

        return f"{self.name}"



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



    players = [] # create a dictionary of all players, and the house
    for z in range(player_numbers):
        player = Player(f"Player {z + 1}")
        players.append(player)

    player = Player("House", 100000)
    players.append(player)

    while game_on:

        new_deck = Deck()
        new_deck.shuffle()

        # Reset all players cards and bets, including house
        for player in players:
            player.bet = 0
            player.hand = []



        # Prompt each player to place their bet
        for player in players[:-1]: # exclude house from betting

            while True: #
                try:
                    bet = int(input(f"{player.name}, place bet: "))
                    if bet > 0:
                        if bet > player.chips:
                            print(f"Please re-bet. You only have {player.chips} chips: ")
                        else:
                            player.place_bet(bet)
                            break


                except ValueError:
                    print("Invalid input - please enter a positive integer.\n")
        # Deal two cards to each player and the House
        for x in range(2): # deal two cards
            for current_player in players: # iterate through all players and deal two cards
                new_card = new_deck.deal()
                current_player.add_card(new_card)


                cards_value = current_player.hand_value()
                if current_player.name == "House":
                    print(f"{current_player.name}: {current_player.show_hand(x, hide_first_card=True)}")
                else:
                    print(f"{current_player.name}: {current_player.show_hand(x)}")

        for current_player in players[:-1]: # iterate through all players

                while True:
                    print(f"{current_player.name}: {current_player.show_hand(x, hide_first_card=False)}") # default is False
                    player_move = (input(f"{current_player.name}, Would you like to Stand(S) or Take a Card (C): "))
                    player_move = player_move.upper()

                    if player_move == "C":
                        new_card = new_deck.deal()
                        current_player.add_card(new_card)


                        cards_value = current_player.hand_value()

                        if cards_value > 21:
                            print(f"{current_player.name}: {current_player.show_hand(x, hide_first_card=False)}")
                            print(f"{current_player.name} you are BUST. Lost {current_player.bet}")
                            break
                        continue
                    elif player_move == "S":
                        print(f"{current_player.name} stands with a hand value of {current_player.hand_value()}\n")
                        break
                    else:
                        print("Invalid input - Please enter S to Stand or C to take a Card.\n")
                        continue

        # Reveal House's hand and play out House's cards
        current_player = players[-1] # House is the last player in the list
        print(f"{current_player.name}: {current_player.show_hand(x, hide_first_card=False)}\n")
        cards_value = current_player.hand_value()

        while True:
            # House must hit until cards_value is at least 17
            if cards_value < 17:
                    new_card = new_deck.deal()
                    current_player.add_card(new_card)


                    cards_value = current_player.hand_value()
                    print(f"{current_player.name}: {current_player.show_hand(x, hide_first_card=False)}\n")

                    if cards_value > 21:
                        print(f"{current_player.name} is BUST. Pay out winners!\n")
                        break

            else:
                break

        house_count = 0

        house_count = current_player.hand_value()
        # Determine winners and losers
        for current_player in players: # iterate through all players
            if current_player.name != "House":
                if house_count > 21 and current_player.hand_value() < 22:
                    current_player.win_bet(current_player.bet)
                    print(f"{current_player.name} paid out: {current_player.bet} Chip count: {current_player.chips}\n")
                elif house_count == current_player.hand_value() and house_count < 22:
                    current_player.standoff_bet(current_player.bet)
                    print(f"{current_player.name} has a standoff. Bet returned. Chip count: {current_player.chips}\n")
                elif house_count < 22 and current_player.hand_value() > house_count and current_player.hand_value() < 22:
                    current_player.win_bet(current_player.bet)
                    print(f"{current_player.name} paid out: {current_player.bet} Chip count: {current_player.chips}\n")
                else:
                    print(f"{current_player.name} you lost {current_player.bet} Chip count: {current_player.chips}\n")
            else:
                print("New hand to be dealt")
                continue

        deal_hand = input("Deal again - Y/N: ")
        if deal_hand == "Y":
            continue
        else:
            print("Game ended")
            break





