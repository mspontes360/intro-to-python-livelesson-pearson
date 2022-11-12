"""
Deal a hand of 5 cards
"""
import random

suits = ['♠︎', '♣︎', '♥︎', '♦︎']
values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

cards = []
hand = []

for suit in suits:
    for value in values:
        cards.append(suit + value)

#print(f'number of cards: {len(cards)}')

for n in range(5):
    card = random.choice(cards)
    cards.remove(card)
    hand.append(card)

print(hand)

#print(f'number of cards: {len(cards)}')
