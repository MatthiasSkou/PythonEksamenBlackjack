from Player import Player
from Card import Card
import random
from GameLogic import GameLogic

class Dealer:

    gameLogic = GameLogic()

    def __init__(self, hand, isAI, isReveal, dealerTurn, roundOver): 
        self.hand = hand
        self.isAI = isAI
        self.isReveal = isReveal
        self.dealerTurn = dealerTurn
        self.roundOver = roundOver
                                # TODO
                                # List that stores cards in the dealers hand
                             # Bool that decides if dealer is Artificial Intelligence
                             # Bool that decides if dealer's 2nd card is revealed
                       # Bool that decides if it's dealer's turn to hit or stand                

    def takeTurn(self, player, deck):              # Method for when dealer needs to take his  turn
        self.isReveal = True                    # Dealers 2nd card is revealed
        self.printCardsAndSum()                 # Print hand and sum 
        self.checkWin(player)                # Check if the game is done
        self.dealerTurn = True                  # Set dealerTurn to true so we enter while loop
        while self.dealerTurn and not self.roundOver:                  # Loops while it's dealers turn to take an action
            sum = self.gameLogic.checkSum(self)       
            if sum <= 16:                       # If sum is 16 or lower, dealer needs to hit    
                print('Dealers sum is equal to or lower than 16 - dealer hits!')
                self.hand.append(self.gameLogic.dealCard(deck))   # Card is added to dealers hand
                self.printCardsAndSum()         # New hand and sum is printed
                self.checkWin(player)           # Check if anyone has won 

    def printCardsAndSum(self):                 # Method that prints out the dealers hand and total sum
        print("==============================================")
        if not self.isReveal:                   # If user is dealer, show both cards - else, keep 2nd card hidden
            print(" D E A L E R  H A N D ")
            print('┌───────┐')
            print(f'| {self.hand[0].value:<2}    |')
            print('|       |')
            print(f'|   {self.hand[0].suit}   |')
            print('|       |')
            print(f'|    {self.hand[0].value:>2} |')
            print('└───────┘') 
            print('┌───────┐')
            print('|///////|')
            print('|=======|')
            print('| ͡◉ ͜ʖ ͡◉)|')
            print('|=======|')
            print('|///////|')
            print('└───────┘') 
        else:
            print(" D E A L E R  H A N D ")
            for i in self.hand:
                print('┌───────┐')
                print(f'| {i.value:<2}    |')
                print('|       |')
                print(f'|   {i.suit}   |')
                print('|       |')
                print(f'|    {i.value:>2} |')
                print('└───────┘') 
            print(f"Dealer hand sum: {self.gameLogic.checkSum(self)}")
        print("==============================================")
        
    def checkWin(self, player):              # Method that checks if the game has ended
        playerSum = self.gameLogic.checkSum(player)
        sum = self.gameLogic.checkSum(self)               
        if sum > 21:                            # If dealers sum is larger than 21, dealer is bust
            print('Dealer exceeded 21 and has LOST the game!')
            player.balance += player.bet * 2    # TODO Set correct multiplier for all bets
            player.printBalance()
            self.dealerTurn = False             # Break out of while-loop
            self.roundOver = True
                                                # TODO Player instant win if hit blackjack?

        elif sum > playerSum and sum > 16:                   # TODO Draw over 16 even tho player is below 16?
            print(f'Dealer hit {sum} and WINS over the player with {playerSum}')
            player.balance = player.balance - player.bet
            player.printBalance()
            self.dealerTurn = False             # Break out of loop
            self.roundOver = True

        elif sum == playerSum and sum > 16:     # If both players are above 16 and they have equal values - game tied
            print(f"Game is tied! Both players hit {sum}")
            player.printBalance()
            self.roundOver = True

        elif sum < playerSum and sum > 16:      # If dealers sum is above 16 but less than players - player won
            print(f'Dealer hit {sum} and is still lower than players sum: {playerSum}')
            print('Player has won')
            player.balance += player.bet * 2    # TODO    
            player.printBalance()
            self.dealerTurn = False             # Break out of while-loop
            self.roundOver = True

        else:                                   # In any other case: It's still dealers turn to hit
            self.dealerTurn = True              # Set to true to keep looping TODO else needed? 