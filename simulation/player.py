# Customizes a player
# Gives the ability to give statistics
# Holds and exposes states

from deck import Deck

class Player:

    def __init__(self, player_number):
        self.playing_deck = Deck()
        self.winning_deck = Deck()
        self.player_number = player_number
        self.num_shuffles = 0
        self.num_wins = 0

    def give_next_card(self):
        if not self.playing_deck.deck: # If the deck is empty

            if len(self.winning_deck.deck) == 0: return "Loser"

            self.winning_deck.shuffle()
            while self.winning_deck.deck:
                to_add_value = self.winning_deck.deck.pop()
                self.playing_deck.deck.append(to_add_value)

        return self.playing_deck.remove_top_card()

    def collect_cards(self, cards):
        for add_this_card in cards:
            self.winning_deck.deck.append(add_this_card)


    def war_valid(self):
        if len(self.winning_deck.deck) + len(self.playing_deck.deck) < 3:
            return False
        else:
            return True





