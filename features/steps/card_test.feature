Feature: testing all card classes
  Scenario: test that the deck of cards created an entire deck
    Given I have made a deck of cards
    When I check the number of cards in the deck
    Then the number of cards in the deck should be 52

  Scenario: drawing a card removes it from the list
    Given I have a deck of cards
    When I draw a card
    Then It is removed from the stack

  Scenario: shuffling the deck changes the order
    Given I have a deck of cards
    When I shuffle them
    Then The order has changed