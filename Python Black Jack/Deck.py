import random
from Card import Card

class Deck:
    def __init__(self, cardDeck):
    # Deck of cards
    # cardDeck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
        self.cardDeck = cardDeck                              # List of cards in the deck

    def createDeck(self):                       # Method that fills the deck with 52 cards as a standard deck of cards without jokers
        deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']   # List of possible card values
        for suit in ['♥','♦','♣','♠']:  # For-loop traversing through the 4 unique suits
            for value in deck:                  # Inner for-loop traversing through the deck list
                self.cardDeck.append(Card(suit, value))         # Add a card object with its suit and value

    def shuffleDeck(self):                      # Method that shuffles the cards in the deck randomly
        random.shuffle(self.cardDeck)       
