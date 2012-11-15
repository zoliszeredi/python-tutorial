"""
Problem 2
Texas Hold'em 

Use-cases:
1. Shuffle deck of cards
2. Sort deck of cards
3. Deal cards
4. Players should receive a Hand  2 Cards
5. Draw 5 Cards after card deal

"""

import unittest
import random

class ClassicPokerSet(object):
    """
    Ranks: 2-10, JQKA
    Suites: Hearts, Clubs, Diamonds, Spades
    """
    def __init__(self):
        """ """ 
        self.suites = set(['hearts', 'diamonds', 'clubs', 'spades'])
        self.ranks = set([str(rank) for rank in range(2, 11)]) | set('JQKA')
        self.card_set = set(
            (suite, rank) 
            for suite in self.suites
            for rank in self.ranks
            )

    def __str__(self):
        """Pretty printing"""
        string = '';
        for suite, rank in self.card_set:
            string += 'the {} of {}'.format(rank, suite)
        return string
    
class Deck(object):
    """
    Shuffles, sorts and deals Cards.
    """
    def __init__(self, card_set):
        """ """
        self.card_set = card_set
        self.card_stack = list(card_set)

    def deal(self, count=1):
        """Deals top-most n cards from the deck"""
        to_be_dealt = self.card_stack[:count]
        self.card_stack = self.card_stack[count:]
        return to_be_dealt

    def shuffle(self):
        """Randomizes the card stack"""
        random.shuffle(self.card_stack)

    def sort(self):
        """Orderes the card stack to it's original state"""
        self.card_stack = list(self.card_set)

    def change_card_set(self, new_card_set):
        """Switch with another card set"""
        self.card_set = new_card_set
        self.card_stack = list(new_card_set)

    def __len__(self):
        """Returns the card count"""
        return len(self.card_stack)

class Dealer(object):
    """Gives hands of two, and draw table"""
    def __init__(self, card_set):
        self.deck = Deck(card_set)
        self.deck.shuffle()
    
    def deal_hand(self):
        """Deals two cards"""
        return self.deck.deal(2)

    def deal_table(self):
        """Deals five cards"""
        return self.deck.deal(5)

class DeckTest(unittest.TestCase):
    """Tests the decks dealing, sorting, shuffling, deck change"""
    def setUp(self):
        poker_set = ClassicPokerSet()
        self.card_set = poker_set.card_set
        self.card_count = len(self.card_set)
        self.ordered_stack = list(self.card_set)
        self.deck = Deck(self.card_set)

    def test_deck_size(self):
        """Should have the same card count as from the passed card set"""
        expected_card_count = len(self.card_set)
        actual_card_count = len(self.deck)
        self.assertEquals(expected_card_count, actual_card_count)        

    def test_deal_one(self):
        """
        Tests that the card stack got decremented by one,
        and verifies the dealt cards
        """
        expected_size = len(self.card_set)-1
        expected_card = self.ordered_stack[0]
        actual_card = self.deck.deal(1)[0]
        actual_size = len(self.deck)
        self.assertEquals(expected_size, actual_size)
        self.assertTupleEqual(expected_card, actual_card)

    def test_deal_two(self):
        """
        Tests that the card stack got decremented by two,
        and verifies the dealt cards
        """
        expected_size = len(self.card_set)-2
        expected_cards = self.ordered_stack[:2]
        actual_cards = self.deck.deal(2)
        actual_size = len(self.deck)
        self.assertEquals(expected_size, actual_size)
        self.assertListEqual(expected_cards, actual_cards)

    def test_deal_five(self):
        """
        Tests that the card stack got decremented by two,
        and verifies the dealt cards
        """
        expected_size = len(self.card_set)-5
        expected_cards = self.ordered_stack[:5]
        actual_cards = self.deck.deal(5)
        actual_size = len(self.deck)
        self.assertEquals(expected_size, actual_size)
        self.assertListEqual(expected_cards, actual_cards)

    def test_shuffle(self):
        """
        Checks that the shuffled deck differs from the previous one
        """
        self.deck.shuffle()
        shuffled_stack = self.deck.deal(self.card_count)
        self.assertNotEqual(self.ordered_stack, shuffled_stack)
    
    def test_sort(self):
        """
        Checks that the deck is ordered coresponding to the original card set
        """
        self.deck.shuffle()
        self.deck.sort()
        stack = self.deck.deal(self.card_count)
        self.assertEquals(self.ordered_stack, stack)

    def test_change_card_set(self):
        """
        Checks for the size of the augmented desk to be one greater than the previous
        """
        poker_set = ClassicPokerSet()
        augmented_set = poker_set.card_set | set([('weird', '99')])
        self.deck.change_card_set(augmented_set)
        expected_size = len(poker_set.card_set)+1
        actual_size = len(augmented_set)
        self.assertEqual(expected_size, actual_size)

class DealerTest(unittest.TestCase):
    """Tests the player and hand deals"""
    def setUp(self):
        poker_set = ClassicPokerSet()
        card_set = set(poker_set.card_set)
        self.dealer = Dealer(card_set)

    def test_deal_hand(self):
        """Verifies that two cards get dealt"""
        cards = self.dealer.deal_hand()
        expected_count = 2
        actual_count = len(cards)
        self.assertEquals(expected_count, actual_count)

    def test_draw_table(self):
        """Verifies that five cards get dealt"""
        cards = self.dealer.deal_table()
        expected_count = 5
        actual_count = len(cards)
        self.assertEquals(expected_count, actual_count)

class TexasHoldemGame(object):
    """
    Game of player_count
    Deals to all players two cards each.
    Draws five table cards after all players receive their hands
    """

    def __init__(self, player_count):
        poker_set = ClassicPokerSet()
        card_set = set(poker_set.card_set)
        self.dealer = Dealer(card_set)
        self.player_count = player_count
        self.player_hands = []
        self.table_hand = []

    def serve_players(self):
        """Deals each player a hand of two card"""
        for _ in range(self.player_count):
            self.player_hands.append(self.dealer.deal_hand())

    def draw_table(self):
        """Draw the five cards on the table"""
        self.table_hand = self.dealer.deal_table()

    def hands(self):
        """See hands of all players"""
        return self.player_hands

    def table(self):
        """See whats on the table"""
        return self.table_hand
    

class TexasHoldemGameTest(unittest.TestCase):
    """Tests the serve players and table"""
    def setUp(self):
        self.players = 9
        self.game = TexasHoldemGame(player_count = self.players)

    def test_init(self):
        """Tests that no players have any cards yet"""
        self.assertListEqual(self.game.hands(), [])
        self.assertListEqual(self.game.table(), [])

    def test_serve_players(self):
        """
        Tests that there should be exacly the same number of hands
        dealt as players and that each player has a hand of two cards
        """
        self.game.serve_players()
        expected_hand_count = self.players
        player_hands = self.game.hands()
        actual_hand_count = len(player_hands)
        self.assertEquals(expected_hand_count, actual_hand_count)
        for hand in player_hands:
            self.assertEquals(2, len(hand))

    def test_draw_table(self):
        """The table should have a hand of five cards"""
        self.game.draw_table()
        table = self.game.table()
        self.assertEquals(5, len(table))

if __name__ == '__main__':
    unittest.main()
