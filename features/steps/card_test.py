from behave import *
import cards


@Given('I have created a new deck object')
def step_impl():
    pass


@When('I create the new deck')
def step_impl(context):
    new_deck = cards.Deck()
    assert new_deck is not None
    context.deck_holder = new_deck


@Then('the number of cards in the deck should be 52')
def step_impl(context):
    assert len(context.deck_holder) == 52


@Given('I have a deck of cards')
def step_impl(context):
    context.new_deck = cards.Deck()
    assert context.new_deck is not None


@When('I draw a card')
def step_impl(context):
    context.num_of_cards = len(context.new_deck)
    context.drawn_card = context.new_deck.draw()
    assert context.drawn_card is not None


@Then('It is removed from the deck')
def step_impl(context):
    assert len(context.new_deck) < context.num_of_cards
    assert context.drawn_card not in context.new_deck.count == 51


@Given('I have a deck of cards')
def step_impl(context):
    context.new_deck = cards.Deck()
    assert context.new_deck is not None


@When('I shuffle the deck')
def step_impl(context):
    context.shuffled_deck = context.new_deck.shiffle()
    assert context.shuffled_deck is not None


@Then('The shuffled deck should not be in the same order as the original')
def step_impl(context):
    assert context.new_deck != context.shuffled_deck
