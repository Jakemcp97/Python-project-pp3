# Blackjack
import random



class Card:
    """
    Card class definition
    """
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.card_value = card_value
        self.value = value


# create and print card function - sourced from askpython.com
def print_cards(cards, hidden):

    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == "10":
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == "10":
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)

    print()


# game function
def blackjack(deck):
    """
    A simple blackjack game where the goal is to get a total of,
    or as close to 21 in card value while competing against the dealer.
        """
    # player and dealer cards
    player_cards = []
    dealer_cards = []

    # dealer/player scores
    player_score = 0
    dealer_score = 0
    # initial deal
    while len(player_cards) < 2:
        # deal a random card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        player_score += player_card.card_value
        # if both cards are ace make first ace value 1
        
        if len(player_cards) == 2:
            val1 = player_cards[0].card_value
            val2 = player_cards[1].card_value
            if val1 == 11 and val2 == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        print("Your cards: ")
        print_cards(player_cards, False)
        print("Your current score= ", player_score)
        input("Press enter to continue \n")

        # deal random card to dealer and update dealer score
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value

        # print dealer cards, hiding the second
        print("Dealers cards: ")
        dprint = dealer_cards[-1].card_value
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("dealers score = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("Dealers Score =", dealer_score - dprint)

        # check for both dealers cards being aces
        dcard1 = dealer_cards[0].card_value
        dcard2 = dealer_cards[1].card_value
        if len(dealer_cards) == 2:
            if dcard1 == 11 and dcard2 == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10

        input("Press enter to continue: \n")

    # if player gets a blackjack
    if player_score == 21:
        print("You have a BlackJack! \n You Win!!!")
        restart()

    # print dealer and player cards
    print("Dealers cards: ")
    print_cards(dealer_cards[:-1], True)
    print("Dealers score =", dealer_score - dprint)
    print()
    print("Your Cards: ")
    print_cards(player_cards, False)
    print("Your score = ", player_score)

    # players moves
    while player_score < 21:
        choice = input("press H to hit or S to stand: \n")

        # validate input
        if len(choice) != 1 or (choice.upper() != "H" and choice.upper() != "S"):
            print("you have entered an incorrect answer, Please try again!")
        # hit function
        if choice.upper() == "H":
            # deal new card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
            player_score += player_card.card_value

            # update player score when dealing with an ace
            x = 0
            while player_score > 21 and x < len(player_cards):
                if player_cards[x].card_value == 11:
                    player_cards[x].card_value = 1
                    player_score -= 10
                    x += 1
                else:
                    x += 1

            # print next round of cards
            print("Dealers cards: ")
            print_cards(dealer_cards[:-1], True)
            print("Dealers score = ", dealer_score - dprint)
            print()
            print("Your cards: ")
            print_cards(player_cards, False)
            print("Your score = ", player_score)

        # stand function player input
        if choice.upper() == "S":
            break

    # final card print
    print(" Your cards: ")
    print_cards(player_cards, False)
    print("Your Score = ", player_score)

    print()
    print("The dealer is showing his hidden card!")

    print("Dealers cards: ")
    print_cards(dealer_cards, False)
    print("The Dealers score is = ", dealer_score)

    # check for player blackjack again
    if player_score == 21:
        print("You have a Blackjack \n You Win!!!")
        restart()
    # check for player bust
    if player_score > 21:
        print("You have busted! \n Dealer Wins!")
        restart()
    input("Press enter to continue \n")

    # Dealers move management
    while dealer_score < 17:
        print("Dealer must hit: ")

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.card_value

        # check for dealer having aces and reflecting in score
        y = 0
        while dealer_score > 21 and y < len(dealer_cards):
            if dealer_cards[y].card_value == 11:
                dealer_cards[y].card_value = 1
                dealer_score -= 10
                y += 1
            else:
                y += 1

        # print for dealer management
        print("Your cards: ")
        print_cards(player_cards, False)
        print("Your score = ", player_score)

        print()

        print("Dealer cards: ")
        print_cards(dealer_cards, False)
        print("Dealers score = ", dealer_score)

        input("press enter to continue: \n")
    # check for dealer bust
    if dealer_score > 21:
        print("Dealer has gone bust! \n You win!")
        restart()

    # check for dealer blackjack
    if dealer_score == 21:
        print("The Dealer has a Blackjack! You lose this hand!")
        restart()

    # acknowledge if its a tie game
    if dealer_score == player_score:
        print("Tie Game, No Winners!")
        restart()

    # if player wins via score
    elif player_score > dealer_score:
        print("You win this hand!")
        restart()
    else:
        print("The dealer has won this hand!")
        restart()

# A function allowing user to restart on game end
def restart():
    while True:
        end_game = input("Would you like to restart? Y or N?")
        if len(end_game) != 1 or (
            end_game.upper() != "Y" and end_game.upper() != "N"
            ):
            print("you have entered an incorrect answer, Please try again!")
        if end_game.upper() == "Y":
            blackjack(deck)
        if end_game.upper() == "N" or "n":
            print("Thanks for playing!! ")
            quit()


# suits
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {
    "Spades": "\u2664",
    "Hearts": "\u2661",
    "Clubs": "\u2667",
    "Diamonds": "\u2662",
}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k"]
card_values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "k": 10,
}
deck = []

# loop to create deck
for suit in suits:
    for card in cards:
        deck.append(Card(suits_values[suit], card, card_values[card]))

blackjack(deck)
