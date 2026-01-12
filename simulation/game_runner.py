# Make the game, deal the cards, run the loop of the game

from game_state import GameState
from deck import Deck
from card import Card

import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
        winner TEXT,
        num_rounds INTEGER,
        num_wars INTEGER
    )
               """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS initial_conditions (
        game_id INTEGER,
        player_id TEXT,
        avg_rank REAL,
        std_rank REAL,
        num_high_cards INTEGER,
        num_low_cards INTEGER
    )
               """)

def main():



    # We need to make an initial deck of cards
    for v in range(100):

        our_game = GameState()
        game_cap = 0
        player_b_strong_cards = 0
        player_b_weak_cards = 0
        player_a_strong_cards = 0
        player_a_weak_cards = 0
        winner = ""


        entire_deck = Deck()
        for i in range(0, 4):
            for j in range(1, 14):
                entire_deck.add_card(Card(j))

        # Entire deck is made!
        entire_deck.shuffle()
        while entire_deck.deck:
            our_game.player_a.playing_deck.add_card(entire_deck.deck.pop())
            our_game.player_b.playing_deck.add_card(entire_deck.deck.pop())

        # Get the stats
        for card in our_game.player_a.playing_deck.deck:
            if card.rank > 9:
                player_a_strong_cards += 1
            elif card.rank < 4:
                player_a_weak_cards += 1

        for card in our_game.player_b.playing_deck.deck:
            if card.rank > 9:
                player_b_strong_cards += 1
            elif card.rank < 4:
                player_b_weak_cards += 1



        while not our_game.game_over:
            our_game.play_round()
            game_cap += 1
            if game_cap > 10000: our_game.game_over = True



if __name__ == "__main__":
    main()


