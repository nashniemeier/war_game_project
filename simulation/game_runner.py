# Make the game, deal the cards, run the loop of the game

from game_state import GameState
from deck import Deck
from card import Card

def main():
    our_game = GameState()

    # We need to make an initial deck of cards

    entire_deck = Deck()
    for i in range(0, 4):
        for j in range(1, 15):
            entire_deck.add_card(Card(j))

    # Entire deck is made!

    while entire_deck:
        our_game.player_a.playing_deck.add_card(entire_deck.deck.pop())
        our_game.player_b.playing_deck.add_card(entire_deck.deck.pop())

    while not our_game.game_over:
        our_game.play_round()

