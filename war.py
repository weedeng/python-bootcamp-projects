suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",
         "Queen", "King")
value = {"Ace": 14, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
         "Nine": 9, "Ten": 10, "Jack": 11,"Queen": 12, "King": 13}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self):
        return self.hand.pop(0)


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Deal all the cards to both players
    for x in range(26):
        card1 = deck.deal()
        player1.add_card(card1)
        card2 = deck.deal()
        player2.add_card(card2)

    # Game loop
    at_war = True
    game_on = True
    player1_war_cards = []
    player2_war_cards = []

    while game_on:

        #print card counts
        print(f"Player 1 has {len(player1.hand)} cards. Player 2 has {len(player2.hand)} cards.")

        #check to see if a player is out of cards
        if len(player1.hand) == 0:
            print("Player 1 out of cards! Player 2 Wins!")
            game_on = False
            break
        if len(player2.hand) == 0:
            print("Player 2 out of cards! Player 1 Wins!")
            game_on = False
            break

        # Each player plays one card
        card1 = player1.play_card()
        card2 = player2.play_card()

        if card1.value > card2.value:
            print(f"{player1.name} wins with {card1} against {card2}")
            player1.add_card(card1)
            player1.add_card(card2)
            if len(player1_war_cards) > 0:
                for card in player1_war_cards + player2_war_cards:
                    player1.add_card(card)

                player1_war_cards = []
                player2_war_cards = []


        elif card2.value > card1.value:
            print(f"{player2.name} wins with {card2} against {card1}")
            player2.add_card(card1)
            player2.add_card(card2)
            if len(player2_war_cards) > 0:
                for card in player1_war_cards + player2_war_cards:
                    player2.add_card(card)
                player1_war_cards = []
                player2_war_cards = []


        else:
            print("It's a tie. Therefore WAR!!!!")

            # Check to see if a player is out of cards:
            if len(player1.hand) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player2.hand) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break

            # Otherwise, we're still at war, so we'll add the next cards
            # WAR logic. Each player sets aside five cards PLUS the tied card
            player1_war_cards = [card1] + [player1.play_card() for _ in range(5)]
            player2_war_cards = [card2] + [player2.play_card() for _ in range(5)]


