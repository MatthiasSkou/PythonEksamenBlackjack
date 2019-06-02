
import unittest
from Player import Player
from Dealer import Dealer
from Deck import Deck
from Card import Card
from GameLogic import GameLogic

class GameTestCases(unittest.TestCase):
    # PLAYER: hand, isAI, playerChoice, balance, bet
    # DEALER: hand, isAI, deck, isReveal, dealerTurn

    # UTest 01.1: if blackjack registers 21
    def test_blackjack_true(self):
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'J')], False, True, 500, 0)
        self.assertTrue(player.isBlackjack(), f"player.isBlackjack = {player.isBlackjack()} // If player has 21 when isBlackJack is called - method should return True")

    # UTest 01.2: if blackjack registers input that isn't 21
    def test_blackjack_false(self): 
        player = Player([Card('Hearts', '2'), Card('Clubs', 'J')], False, True, 500, 0)
        self.assertFalse(player.isBlackjack(), f"player.isBlackjack() = {player.isBlackjack()} // If player doesn't have blackjack(21), method should return False")

    # UTest 01.3: if both players have same value(18)
    def test_game_draw(self): 
        player = Player([Card('Hearts', '8'), Card('Clubs', 'J')], False, False, 500, 0)
        dealer = Dealer([Card('Hearts', '8'), Card('Clubs', 'J')], True,  True, True, False)
        dealer.checkWin(player)
        self.assertTrue(dealer.roundOver, f"dealer.roundOver = {dealer.roundOver} // If both players are above 16 and under 21 and has equal sum - game over should be True")
   
    # UTest 01.4: if both players are draw at 21
    def test_draw_21(self): 
        player = Player([Card('Hearts', 'J'), Card('Clubs', '5'), Card('Clubs', '6')], False, False, 500, 0)
        dealer = Dealer([Card('Hearts', 'J'), Card('Clubs', '5'), Card('Clubs', '6')], True,  True, True, False)
        dealer.checkWin(player)
        self.assertTrue(dealer.roundOver, f"dealer.roundOver = {dealer.roundOver} // If both players are 21 - game over should be True")

    # UTest 01.5: if sum is equal to 21 with ace and jack
    def test_sum(self):
        gameLogic = GameLogic()          
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'J')], False, True, 500, 0)
        self.assertEqual(gameLogic.checkSum(player), 21, f"gameLogic.checkSum(player) = {gameLogic.checkSum(player)} // Ace and Jack should sum to 21")

class AceTest(unittest.TestCase):

    # UTest 02.1: if ace counts at eleven when it won't exceed 21 
    def test_check_ace_eleven(self):    
        gameLogic = GameLogic()          
        player = Player([Card('Hearts', 'A'), Card('Clubs', '2')], False, False, 500, 0)
        self.assertEqual(gameLogic.checkSum(player), 13, f"gameLogic.checkSum(player) = {gameLogic.checkSum(player)} // Player hand should sum to 13 because A is valued as 11")

    # UTest 02.2: if ace counts as 1, when 11 would exceed 21
    def test_check_ace_one(self):
        gameLogic = GameLogic() 
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'J'), Card('Clubs', '9')], False, False, 500, 0)
        self.assertEqual(gameLogic.checkSum(player), 20, f"gameLogic.checkSum(player) = {gameLogic.checkSum(player)} // Player hand should sum to 20 because A is valued as 1")

    # UTest 02.3: if double aces counts as 1 when they would exceed 21 as 11
    def test_check_double_ace(self):
        gameLogic = GameLogic() 
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'A')], False, False, 500, 0)
        self.assertEqual(gameLogic.checkSum(player), 12, f"gameLogic.checkSum(player) = {gameLogic.checkSum(player)} // Player hand should be 12 because one A is valued as 11 and one as 1")

    # UTest 02.4: if tripple aces counts as 1 when they would exceed 21 as 11
    def test_check_tripple_ace(self):
        gameLogic = GameLogic() 
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'A'), Card('Clubs', 'A')], False, False, 500, 0)
        self.assertEqual(gameLogic.checkSum(player), 13, f"gameLogic.checkSum(player) = {gameLogic.checkSum(player)} // Player hand should be 13 because one A is valued as 11 and two as 1")

    # UTest 02.5: if quadra aces counts as 1 when they would exceed 21 as 11
    def test_check_quadra_ace(self):
        gameLogic = GameLogic() 
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'A'), Card('Clubs', 'A'), Card('Clubs', 'A')], False, False, 500, 0)
        self.assertEqual(gameLogic.checkSum(player), 14, f"gameLogic.checkSum(player) = {gameLogic.checkSum(player)} // Player hand should be 14 because one A is valued as 11 and three as 1")

    # UTest 02.6: if double ace and a normal card wouldn't exceed 21 by setting value to 11
    def test_check_double_ace_and_normal_card(self):
        gameLogic = GameLogic() 
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'A'), Card('Clubs', '10')], False, False, 500, 0)
        self.assertEqual(gameLogic.checkSum(player), 12, f"gameLogic.checkSum(player) = {gameLogic.checkSum(player)} // Player hand should be 12 because both aces are valued as 1")

class DealerTest(unittest.TestCase):

    # UTest 03.1: if dealer is bust after exceeding 21 
    def test_dealer_bust(self):
        player = Player([Card('Hearts', 'A'), Card('Clubs', 'J')], False, True, 500, 0)
        dealer = Dealer([Card('Hearts', '10'), Card('Clubs', '10'), Card('Clubs', '6')], True,  True, True, False)
        dealer.checkWin(player)
        self.assertTrue(dealer.roundOver, f"dealer.roundOver = {dealer.roundOver} // If dealer is bust - game over should be True")

    # UTest 03.2: if dealer wins when he has more than 16 sum and beat the player
    def test_dealer_win(self):
        player = Player([Card('Hearts', '10'), Card('Clubs', '7')], False, True, 500, 0)
        dealer = Dealer([Card('Hearts', '10'), Card('Clubs', '8')], True,  True, True, False)
        dealer.checkWin(player)
        self.assertTrue(dealer.roundOver, f" dealer.roundOver = {dealer.roundOver} // If dealer has won - game over should be True")

    # UTest 03.3: if dealer ai will draw a card when he is below 17 value
    def test_dealer_draw(self):
        deck = Deck([])
        deck.createDeck()                         
        deck.shuffleDeck()   
        player = Player([Card('Hearts', '10'), Card('Clubs', '7')], False, True, 500, 0)
        dealer = Dealer([Card('Hearts', '4')], True,  True, True, False)
        dealer.takeTurn(player, deck.cardDeck)
        self.assertTrue(len(dealer.hand) > 1, f"len(dealer.hand) = {len(dealer.hand)} // Dealers hand should contain more than 1 card after draw")

    # UTest 03.4: if dealer will stand when he is above 16 value
    def test_dealer_stand(self):
        deck = Deck([])
        deck.createDeck()                         
        deck.shuffleDeck()   
        player = Player([Card('Hearts', '1'), Card('Clubs', '7')], False, True, 500, 0)
        dealer = Dealer([Card('Hearts', '10'), Card('Hearts', '6')], True,  True, True, False)
        dealer.takeTurn(player, deck.cardDeck)
        self.assertEqual(len(dealer.hand), 3, f"len(dealer.hand) = {len(dealer.hand)} // Dealers hand should contain 3 cards, because he only draws one and then stands")

class PlayerTest(unittest.TestCase):

    # UTest 04.1: if player will be bust after exceeding 21 value
    def test_player_bust(self):
        player = Player([Card('Hearts', '10'), Card('Clubs', '10'), Card('Clubs', '10')], False, True, 500, 0)
        self.assertFalse(player.checkBust(), f"player.checkBust() = {player.checkBust()} // checkBust should return False is player busted")

    # UTest 04.2: if players turn ends automatically when he hits 21
    def test_player_21(self):
        player = Player([Card('Hearts', '10'), Card('Clubs', '10'), Card('Clubs', 'A')], False, True, 500, 0)
        player.checkBust()
        self.assertFalse(player.checkBust(), f"player.checkBust() = {player.checkBust()} // checkBust should return False if player hit 21")

    # UTest 04.3: if players turn continues when he is not bust or 21
    def test_player_not_bust_or_21(self):
        player = Player([Card('Hearts', '10'), Card('Clubs', '10')], False, False, 500, 0)
        self.assertTrue(player.checkBust(), f"player.checkBust() = {player.checkBust()} // checkBust should return True if not bust or 21")

    # UTest 04.4: if player wins when he has higher value than dealer and dealers turn is already over
    def test_player_win(self):
        player = Player([Card('Hearts', '10'), Card('Clubs', '7')], False, False, 500, 0)
        dealer = Dealer([Card('Hearts', '10'), Card('Hearts', '8')], True,  True, True, False)
        dealer.checkWin(player)
        self.assertTrue(dealer.roundOver, f"dealer.roundOver = {dealer.roundOver} // If player has won - game over should be true")

    # UTest 04.5: if player ai will hit when below 17 value
    def test_player_ai_hit(self):
        deck = Deck([])
        deck.createDeck()                         
        deck.shuffleDeck() 
        player = Player([Card('Hearts', '5'), Card('Clubs', '5')], True, False, 500, 0)
        dealer = Dealer([Card('Hearts', '10'), Card('Hearts', '8')], True,  True, True, False)
        player.takeTurn(dealer, deck.cardDeck)
        self.assertTrue(len(player.hand) > 2, f"len(player.hand) = {len(player.hand)} // Player ai didn't draw a card when it was supposed to hit!")

    # UTest 04.6: if player ai will stand when he is 17 to 21 value
    def test_player_ai_stand(self):
        deck = Deck([])
        deck.createDeck()                         
        deck.shuffleDeck() 
        player = Player([Card('Hearts', '10'), Card('Clubs', '7')], True, False, 500, 0)
        dealer = Dealer([Card('Hearts', '10'), Card('Hearts', '8')], True,  True, True, False)
        player.takeTurn(dealer, deck.cardDeck)
        self.assertEqual(len(player.hand), 2, f"len(player.hand) = {len(player.hand)} // Player ai drew a card when it was supposed to stand!")

if __name__ == '__main__':
    unittest.main()