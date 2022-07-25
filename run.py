#Blackjack 
from http.cookiejar import DefaultCookiePolicy
import random

#card class definition 
class Card: 
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.card_value = card_value
        self.value = value
#create and print card function - sourced from askpython.com
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
        if card.value == '10':
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
        if card.value == '10':
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
#game function 
def blackjack(deck):

    #player and dealer cards
    player_cards = []
    dealer_cards = []

    #dealer/player scores 
    player_score = 0
    dealer_score = 0
    #initial deal
    while len(player_cards) <2:
        #deal a random card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        player_score += player_card.card_value
        #if both cards are ace make first ace value 1
        if len(player_cards) ==2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        print("Your cards: ")
        print_cards(player_cards, False)
        print("Your current score= ", player_score)
        input("Press enter to continue")

        #deal random card to dealer and update dealer score
        dealer_card= random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value

        #print dealer cards, hiding the second
        print("Dealers cards: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("dealers score = ", dealer_score)
        else: 
            print_cards(dealer_cards[:-1], True)
            print("Dealers Score =", dealer_score - dealer_cards[-1].card_value)

        #check for both dealers cards being aces 
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10

        input("Press return to continue: ")

    #if player gets a blackjack 
    if player_score == 21:
        print("You have a BlackJack! \n You Win!!!")
        restart = input("Would you like to play again? Y or N? ")
        if restart == "Y":
            blackjack(deck)


    #check if player gets blackjack
    #if player get blackjack autowin
    #check for player bust
    #dealers moves
    #if dealer gets blackjack
    #if dealer busts

    #if game is a tie
    #if player wins 
    #if dealer wins
    


#suits
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs":"\u2667", "Diamonds":"\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8","9", "10", "J", "Q", "k"]
card_values = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,"9":9, "10":10, "J":10, "Q":10, "k":10}
deck = []