# Make the game, deal the cards, run the loop of the game
import random

TEST_MODE = False

from game_state import GameState
from deck import Deck
from card import Card
import statistics

import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
        winner TEXT,
        num_rounds INTEGER,
        num_wars INTEGER,
        hit_round_cap INTEGER
    )
               """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS initial_conditions (
        game_id INTEGER,
        player_id TEXT,
        avg_rank REAL,
        std_rank REAL,
        num_high_cards INTEGER,
        num_low_cards INTEGER,
        num_aces INTEGER
    )
               """)

def main():


    if TEST_MODE:
        seeds = [42, 1337]
        games_per_seed = 20
    else:
        seeds = random.sample(range(1, 10_000_000), 500)
        games_per_seed = 50

    for seed in seeds:
        # We need to make an initial deck of cards
        for game_number in range(games_per_seed):
            random.seed(seed)

            our_game = GameState()
            game_cap = 0
            player_b_strong_cards = 0
            player_b_weak_cards = 0
            player_a_strong_cards = 0
            player_a_weak_cards = 0

            player_a_aces = 0
            player_b_aces = 0
            hit_round_cap = 0

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
            player_a_ranks = []
            for card in our_game.player_a.playing_deck.deck:
                player_a_ranks.append(card.rank)
                if card.rank > 9:
                    player_a_strong_cards += 1
                    if card.rank == 13: player_a_aces += 1
                elif card.rank < 4:
                    player_a_weak_cards += 1
            avg_rank_a = statistics.mean(player_a_ranks)
            std_rank_a = statistics.stdev(player_a_ranks)


            player_b_ranks = []
            for card in our_game.player_b.playing_deck.deck:
                player_b_ranks.append(card.rank)
                if card.rank > 9:
                    player_b_strong_cards += 1
                    if card.rank == 13: player_b_aces += 1
                elif card.rank < 4:
                    player_b_weak_cards += 1
            avg_rank_b = statistics.mean(player_b_ranks)
            std_rank_b = statistics.stdev(player_b_ranks)


            while not our_game.game_over:
                our_game.play_round()
                game_cap += 1
                if game_cap > 10000:
                    our_game.game_over = True
                    hit_round_cap = 1



            cursor.execute("""
            INSERT INTO games (winner, num_rounds, num_wars, hit_round_cap) 
            VALUES (?, ?, ?, ?)
            """, (our_game.winner, our_game.num_rounds, our_game.num_wars, hit_round_cap))

            game_id = cursor.lastrowid

            cursor.execute("""
            INSERT INTO initial_conditions (game_id, player_id, avg_rank, std_rank, num_high_cards, num_low_cards, num_aces) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (game_id, "A", avg_rank_a, std_rank_a, player_a_strong_cards, player_a_weak_cards, player_a_aces))

            cursor.execute("""
            INSERT INTO initial_conditions (game_id, player_id, avg_rank, std_rank, num_high_cards, num_low_cards, num_aces)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (game_id, "B", avg_rank_b, std_rank_b, player_b_strong_cards, player_b_weak_cards, player_b_aces))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()


