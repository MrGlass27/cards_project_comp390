import random
from behave import *


class Rank:
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, rank):
        self.rank = rank

class Suite:
    suite = ["Clubs", "Hearts", "Spades", "Diamonds"]

    def __init__(self, suite):
        self.suite = suite

class Card:
    suite = None
    rank = None

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return 'suite{}, rank{}'.format(self.suite, self.rank)

class Deck:
    card = []

    def __init__(self):
        self.card = []

        for suite in self.suite:
            for rank in self.rank:
                new_suite = Suite(suite)
                new_rank = Rank(rank)
                new_card = Card(new_suite, new_rank)
                self.add(new_card)