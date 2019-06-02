from Player import Player
from Dealer import Dealer
from Deck import Deck
from GameLogic import GameLogic
import os

player = Player([], False, True, 200, 0)                               # Instantiate our player, dealer and deck
dealer = Dealer([], False, False, False, False)
gameLogic = GameLogic()

endGame = False

print("WELCOME TO THE BLACKJACK GAME")          # Welcome MSG TODO - Move to Menu class

while player.playerChoice:                      # Loop while player needs to make a choice
    player.playerChoice = player.chooseIfPlayerOrDealer(dealer)       # Method that let's user make choice to be a player or dealer

while not endGame:
    deck = Deck([])
    for i in range(4):
        deck.createDeck()                       # Create 4 decks in loop (208 cards)
    deck.shuffleDeck()                          # Shuffle the deck randomly
    player = Player([], player.isAI, True, player.balance, 0)   # Instantiate our player and dealer with their correct fields
    dealer = Dealer([], dealer.isAI, False, False, False)       # dealer ai, player ai and balance remains the same as previous round
    if not player.isAI:                         # if player is not ai, he has to choose bet amount
        player.bet = player.choseBetAmount()
        print(f"Bet amount: {player.bet}")
    if player.isAI:                             # Otherwise set AI bet to 50
        player.bet = 50                         

    player.hand.append(gameLogic.dealCard(deck.cardDeck))           # Player is dealt his first card
    player.hand.append(gameLogic.dealCard(deck.cardDeck))           # Player is dealt his 2nd card TODO Change dealCard() to accept amount to draw

    player.printCardsAndSum()                       # Prints the players hand and sum

    dealer.hand.append(gameLogic.dealCard(deck.cardDeck))           # Dealer is dealt his first card
    dealer.hand.append(gameLogic.dealCard(deck.cardDeck))           # Dealer is dealt his 2nd card

    dealer.printCardsAndSum()                       # Prints the dealers hand and sum

    player.playerChoice = True                      # Set playerChoice to True, since they have to decide on stand / hit now
    if player.isBlackjack():
        player.playerChoice = False  # Calls isBlackJack method that checks if the players starting hand is blackjack
    while player.playerChoice:                      # Loops while player needs to make a choice to hit or stand
        player.playerChoice = player.takeTurn(dealer, deck.cardDeck)             # Player needs to take his turn

    dealer.dealerTurn = True                  # Set dealerTurn to true so we enter while loop
    if gameLogic.checkSum(player) <= 21 and not dealer.roundOver:                     # If player's sum is 21 or lower 
        dealer.takeTurn(player, deck.cardDeck)                     # Player chose to stand - It's now dealers turn to play - 
                                                    # Players sum is added as parameter so we can measure later.

    if player.balance == 0:                         # If player is out of money - end the game
        print("You are out of money! Game is over!")   
        endGame = True
        quit()

    while True:                                     # Ask if the player / dealer wants to play another round
        choice = input("Do you want to keep playing?(Y / N)")
        if choice == 'N':                           # If N then stop the game
            endGame = True
            break
        elif choice == 'Y':                         # If Y keep playing
            print("Playing one more round!")
            break
        else:                                       # Bad input: repeat while statement
            print("Your input didn't match Y / N - Please try again!")