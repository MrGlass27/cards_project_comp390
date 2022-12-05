import random
from behave import *


class Rank:
    rank = None

    def __init__(self, rank):
        self.rank = rank

class Suite:
    suite = None

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


