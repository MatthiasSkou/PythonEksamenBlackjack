class GameLogic:

    def dealCard(self, deck):        
        return deck.pop()                  # Pop removes last card in list by default

    def checkSum(self, user):                         # Method that returns sum of a players hand
        sum = 0                                 # Sum that increments with each card we add 
        amountOfAces = 0                        # Incrementing variable that stores amount of aces in your hand
        faceCards = ['K', 'Q', 'J']
        for i in user.hand:                     # For-loop traversing card objects in hand
            if i.value in faceCards:  # If card is King, Queen or Jack(face cards)
                sum += 10                       # Add 10 to sum if it's a face card

            elif i.value == 'A':                # Else-if the card is an ace
                amountOfAces += 1               # Increment our aces variable

            else:                               # Else(if it's a number) add the number to our sum 
                sum += int(i.value)             # Casts to int and adds number to sum
                
        for i in user.hand:                     # For-loop traversing card objects in hand
            if i.value == 'A':                  # If we hit an ace
                if self.aceValue(sum, amountOfAces):  # Call our aceValue method with (list, index, sum, amountOfAces)
                    sum += 1                    # If aceValue is true - increment our sum variable
                else:                           # If aceValue is false
                    sum += 11                   # Add 11 to sum variable
                amountOfAces -= 1               # Decrement amountOfAces in case player has another ace and method is called again

        return sum

    def aceValue(self, sum, amountOfAces): # Method that returns true if an ace should be valued as 1 
                                                        # and returns false if the ace should be valued as 11
        if sum + 11 + amountOfAces-1 > 21:      # If the sum and the ace = 11 plus the amount of remaining aces is greater than 21
            return True                         
        return False                        # If the ace + 11 + amount of aces is LESS than or equal to 21