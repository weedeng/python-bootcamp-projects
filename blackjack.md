Outline



Global variables:

Suits tuple

Ranks tuple

Values dictionary: ace =1 or 11, J, Q and K = 10



Classes:

Create card class (ie create a card with suit, rank and value) - takes in a suit and rank and then appends its value

Instantiate for self, rank, suit

Create card object for each suit, rank and card value

Create str to print card



Create deck class (ie create a deck of cards which we can shuffle) - takes in nothing, but need to get card value for each card from class Card

Instantiate the class

Self.rank = rank

Self.suit = suit

Self.value = values[rank]



For suit in suits

For rank in ranks

Create deck list

Def shuffle using Import Random

Def deal_card return using pop (if cards left = 0, then need to create new deck, shuffle and deal)



Create player class (takes in name eg Player 1 and sets chips t0 $1000)

Instantiate the class

Self.name = name

Def add_card (this is used to deal the players and the house the initial two cards). The player cards are face up ( but one house card is face up and one face down

Def player_bet (player places a bet note: no doubling, splitting etc). A bet must be placed initially  before the cards are dealt and then, a further opportunity arises once cards dealt

Print str

Return two face up or one up one down (if statement)



Create BankAccount class, takes in name (self.name = name)

Instantiate class

Def add funds (if win)

Def place bet (remove funds)



Game logic:

Enter number of players, between 1 and 5, player_number

Give each player a Bank Account with default cash, say $1000

Create new_deck

Call shuffle

Create loop for player_number, and add one for House (determine how to add House)

For each player, player&player_number = Player(player&player_number)

For each player place initial bet

Deal each player two cards

For each player make an additional bet

For each player, starting at one, ask if want further cards, until say no. Print player name and total card value (if Ace, give two card values)

House needs to stay on >=17. Assume hard 17. Therefore must draw on soft 17

When all stood, check who wins or standoff (take money back from stand off)



