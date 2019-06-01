 # TODO:
    # os.system('clear')
    # Add .sleeps() for AI turns
    # 404 handling
    # Create start switch menu (Start game - See rules - Credits - Quit)
    # Fix aces for dealer
    # Betting
        # Splits
        # Double down
        # Safety 15 %
        # Super 7
    # Comments / Documentation
    # TODO Set correct multiplier for all bets
    # Change color depending on suit console
    # Incluce *args // **kwargs in method?
    # Set methods to return statements
    # Move dealer.dealCard to deck? 
    # Change method names and fields to_something_like_this

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
        deck.createDeck()   # Create 4 decks 
                            # Method that fills the deck with 52 cards
    deck.shuffleDeck()                              # Shuffle the deck randomly
    player = Player([], player.isAI, True, player.balance, 0)                               # Instantiate our player, dealer and deck
    dealer = Dealer([], dealer.isAI, False, False, False)
    if not player.isAI:
        player.bet = player.choseBetAmount()
        print(f"Bet amount: {player.bet}")
    if player.isAI:
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

    if player.balance == 0:
        print("You are out of money! Game is over!")
        endGame = True
        quit()

    while True:
        choice = input("Do you want to keep playing?(Y / N)")
        if choice == 'N':
            endGame = True
            break
        elif choice == 'Y':
            print("Playing one more round!")
            break
        else:
            print("Your input didn't match Y / N - Please try again!")