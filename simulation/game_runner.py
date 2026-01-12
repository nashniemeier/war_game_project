# Make the game, deal the cards, run the loop of the game

from game_state import GameState
from deck import Deck
from card import Card

def main():
    print("Welcome to War Research!")
    our_game = GameState()
    game_cap = 0
    player_b_strong_cards = 0
    player_b_weak_cards = 0

    player_a_strong_cards = 0
    player_a_weak_cards = 0

    # We need to make an initial deck of cards

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
        if game_cap > 10000: break

    #print(our_game.winner + " wins!")
    print(our_game.num_wars, " wars!")
    print(our_game.num_rounds, " rounds!")

    print("Player A had", player_a_strong_cards, " strong cards!")
    print("Player A had", player_a_weak_cards, " weak cards!")

    print("Player B had", player_b_strong_cards, " strong cards!")
    print("Player B had", player_b_weak_cards, " weak cards!")

if __name__ == "__main__":
    main()


