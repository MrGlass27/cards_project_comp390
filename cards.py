import random


class Rank:
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return 'rank{}'.format(self.rank)

class Suite:
    suite = ["Clubs", "Hearts", "Spades", "Diamonds"]

    def __init__(self, suite):
        self.suite = suite

    def __str__(self):
        return 'suite{}'.format(self.suite)

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

        for suite in range(3):
            for rank in range(12):
                new_suite = Suite(suite)
                new_rank = Rank(rank)
                new_card = Card(new_suite, new_rank)
                self.add(new_card)

    def add(self, card):
        self.card.append(card)

    def print(self):
        for card in self.card:
            print(card)

    def shuffle(self):
        random.shuffle(self.card)

    def draw(self):
        drawn_card = self.card[0]
        self.card = self.card[1:]
        return drawn_card


deck = Deck()
deck.shuffle()
deck.print()