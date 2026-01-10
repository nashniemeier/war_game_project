import random

from card import Card

class Deck:
    def __init__(self): # Make the deck
        self.deck = [] # Add nothing yet, keep it simple

    def shuffle(self):
        if len(self.deck) > 0:
            random.shuffle(self.deck)
            return len(self.deck)
        else:
            return -1 # Deck is empty

    def get_top_card(self):
        return self.deck[0]

    def get_bottom_card(self): # Just in case this is needed for later
        return self.deck[-1]

    def remove_top_card(self):
        return self.deck.remove(self.get_top_card())

    def add_card(self, card):
        self.deck.append(card)







