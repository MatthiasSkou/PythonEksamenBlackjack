from GameLogic import GameLogic
class Player:

    gameLogic = GameLogic()

    def __init__(self, hand, isAI, playerChoice, balance, bet): 
        self.hand = hand                        # Hand list that will contain the cards the player has drawn
        self.isAI = isAI                        # Bool that shows if player is Artificial Intelligence or not
        self.playerChoice = playerChoice        # Bool that shows if it's players turn to hit or stand
        self.balance = balance                  # The initial balance of a player
        self.bet = bet                          # The bet each round

    def choseBetAmount(self):
        while True:                             # Loop
            choice = input("Please chose your desired bet(10, 20, 30, 40 or 50)")
            betList = [10, 20, 30, 40, 50]      # List containing possible bet amounts
            if int(choice) not in betList:      # If the entered bet is not in the bet list, repeat loop
                print("Your desired amount didn't match any of the allowed amounts - Try again!")
            elif self.balance - int(choice) >= 0:   # If their bet doesn't exceed their balance
                return int(choice)                  # Return the bet amount
            elif self.balance - int(choice) < 0:    # If their entered bet is higher than their current balance
                print("You don't have enough balance to place this bet - try again!")

    def checkBust(self):                        # Method that checks if the player exceeds 21, hits 21 or is below 21 in sum
        sum = self.gameLogic.checkSum(self)     # Call checkSum() method and recieve total sum of hand
        if sum > 21:                            # If the sum is greater than 21
            print(f"Player has lost the game with {sum} value!")    # Prints lost msg to user with total sum
            self.balance = self.balance - self.bet  # Update balance and print it
            self.printBalance()
            return False                        # Sets playerChoice to false so it breaks out of while-loop
        elif sum == 21:                         # If players total sum is exactly 21
            print(f"Player has hit {sum} - Dealers turn")   
            return False                        # Player is forced to stand - sets playerChoice to false to break out of while-loop
        else:                                   # If players total sum is below 21
            return True                         # Set playerChoice to True so while-loop repeats

    def printCardsAndSum(self):                 # Method that formats and prints players cards and total sum
        print("==============================================")
        print(" P L A Y E R  H A N D ")
        for i in self.hand:                     # For-loop traversing through cards in hand and printing them. Ex. 3 of Spades
            print('┌───────┐')
            print(f'| {i.value:<2}    |')
            print('|       |')
            print(f'|   {i.suit}   |')
            print('|       |')
            print(f'|    {i.value:>2} |')
            print('└───────┘') 
        print()
        print(f"Player hand sum: {self.gameLogic.checkSum(self)}")
        print("==============================================")

    def takeTurn(self, dealer, deck):             # Method that prompts user to tell if they want to stand or hit
        sum = self.gameLogic.checkSum(self)       # Get the total sum of hand
        choice = -1                               # Make sure we won't get error in if-statement
        if not self.isAI:                         # if player is not AI, give them option to hit or stand
            choice = input(f"The sum of your hand is {sum}, would you like to stand or hit?(type 1 for stand and 0 for hit)")
        if choice == '1' or self.isAI and sum > 16:     # If user's input is 1 - They want to stand - or if AI and sum above 16
            print('Player chose to stand - Dealers turn(Dealers 2nd card is revealed)')
            return False           # Set playersTurn to False to break out of while-loop

        elif choice == '0' or self.isAI and sum <= 16:  # Else-if the user input is 0 - They want to hit - or user is AI and below 17
            self.hand.append(self.gameLogic.dealCard(deck)) # Add new card to users hand
            self.printCardsAndSum()             # Print users cards and total sum
            return self.checkBust()                    # Check if user is bust after newly added card
                                                # TODO Make 404-else to prevent bad user input
        
    def isBlackjack(self):                      # Method that checks if players starting hand is blackjack(10 value card + Ace)
        ten = ['Q', 'K', 'J', '10']             # Initialize list with all card values that is equal to 10        
        if self.contains(self.hand, lambda x: x.value == 'A'):  # Call the contain method with our lambda expression
                                                                # that checks if object.value is equal to 'A' (Ace)
            for i in ten:                       # For-loop traversing through ten list                  
                if self.contains(self.hand, lambda x: x.value == i):    # Contain method if value is equal to either 10 value cards
                    print('Player has hit blackjack! Dealers turn..')   
                
                    return True   # If we have hit blackjack - end players turn and break out of while-loop
                                                # TODO Should player win instantly if blackjack is hit? 

    def contains(self, list, filter):           # Contain method that recieves a list and a lambda expression
        for x in list:                          # For-loop traverse through list
            if filter(x):                       # If given lambda expression is met
                return True                     
        return False                            # If lambda expression is NOT met

                                                # TODO Move this method to Menu / Client class when if created
    def chooseIfPlayerOrDealer(self, dealer):   # User is prompted if they want to play as player or dealer
        choice = input("Would you like to play as a player or a dealer? (type 1 for player and 0 for dealer)")

        if choice == '1':                       # If user types 1 and wants to be the player
            dealer.isAI = True                  # Dealer is Artificial Intelligence
            print("You are the player...")
            return False           # Break out of while-loop 

        elif choice == '0':                     # If user types 0 and wants to be dealer
            self.isAI = True                    # Player is Artificial Intelligence
            print("You are the dealer... You will now deal the cards.")
            dealer.isReveal = True              # Dealer can look at his own 2nd card
            return False           # Break out of while-loop

        else:                                   # If 404 bad input - print error msg and continue while-loop
            print(f"Your input: {choice} didn't match any of the cases - Please try again!")


    def printBalance(self):
        print(f"|| Bet placed: {self.bet}      ||      Total balance: {self.balance} ||")
