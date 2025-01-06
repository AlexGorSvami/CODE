from operator import itemgetter
from collections import defaultdict

RESULT = ["Loss", "Tie", "Win"]

SUITS = {
    'S': ('Spades', 1),
    'H': ('Hearts', 1),
    'D': ('Diamonds', 1),
    'C': ('Clubs', 1)
}

RANKS = {
    'A': 14,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}


MADE_HANDS = {
    'straight flush': 9,
    '4 of a kind': 8,
    'full house': 7,
    'flush': 6,
    'straight': 5,
    'set': 4,
    'two pair': 3,
    'one pair': 1,
    'high card': 0
}

class PokerHand(object):
    """Create an object representing a Poker Hand based on an input of a
    string which represents the best 5 card combination from the player's hand
    and board cards.

    Attributes:
        vals: a list of card's values

        suits: a list of card's suits

        hand: a sorted list of tuples representing face value and card value ordered
        by highest card in descending order

        val_cnt: a dict containing each card and the number of times it appears in the hand

        hand_value: the hand value according to MADE_HANDS


    Methods:
        compare_with(self, villain): takes in Hero's Hand (self) and Villain's
            Hand (villain) and compares both hands according to rules of Texas Hold'em.
            Returns one of 3 strings (Win, Loss, Tie) based on wether Hero's hand
            is better than villain's hand.
    Helper Methods:
        _is_straight(self): returns True if hand is a straight
        _is_flush(self): returns True if hand is a flush
        """

    def __init__(self, hand):
        """Initialize a poker hand based on a 10 character string input representing
        5 cards.
        """
        hand = hand.replace(' ', '')
        self.vals = [c for c in hand if c in RANKS.keys()]
        self.suits = [c for c in hand if c in SUITS.keys()]
        self.hand = sorted([RANKS[c] for c in self.vals], reverse=True)
        self.val_cnt = defaultdict(int)

        for card in self.vals:
            self.val_cnt[card] += 1
        self._total_value = self._total_value()

    def _total_value(self):
        """Return a tuple containing of an int representing hand value and a tuple
        of sorted high card values."""
        if self._is_five_high_straight:
            del self.hand[0]
            self.hand.append(1)
        if self._hand_value in [1, 4]:
            sorted_d = sorted(self.val_cnt.items(), reverse=True)
            return (self._hand_value, sorted_d[0][0], tuple(self.hand))
        return (self._hand_value, tuple(self.hand))

    @property
    def _is_five_high_straight(self):
        if sum(self.hand) == 28:
            return True

    @property
    def _is_straight(self):
        """Return True if hand is a straight."""
        if self._is_five_high_straight: return True
        previous_card = self.hand[-1] - 1
        for card in sorted(self.hand):
            if previous_card + 1 != card: return False
            previous_card = card
        return True

    @property
    def _is_flush(self):
        """Return True if hand is a flush."""
        return True if len(set(self.suits)) == 1 else False

    @property
    def _hand_value(self):
        """Return a value based on hand strength."""
        hand_value = 0
        """Check if hand is pair plus"""
        if len(set(self.val_cnt.values())) > 1:
            sorted_d = sorted(self.val_cnt.values(), reverse = True)
            if sorted_d[0] == 2 and sorted_d[1] == 2: return 3
            for pair_plus in sorted_d:
                if pair_plus == 1: return hand_value
                elif pair_plus == 4:
                    return 8
                elif pair_plus == 3:
                    hand_value = 4
                elif pair_plus == 2:
                    if hand_value == 4:
                        return 7
                    else:
                        return 1
        if self._is_straight:
            if self._is_flush:
                return 9
            else:
                return 5
        if self._is_flush:
            return 6
        if len(set(self.val_cnt.values())) == 1: return hand_value

    def compare_with(self, other):
        """Return one of 3 outcomes from result const."""
        if self._total_value > other._total_value:
            return 'Win'
        elif self._total_value < other._total_value:
            return 'Loss'
        else:
            return 'Tie'
