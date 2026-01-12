from player import Player

class GameState:

    def __init__(self):
        self.player_a = Player(1)
        self.player_b = Player(2)
        self.num_rounds = 0
        self.num_wars = 0
        self.game_over = False
        self.winner = ""


    def play_round(self):
        self.num_rounds += 1

        print("Player A has", len(self.player_a.playing_deck.deck) + len(self.player_a.winning_deck.deck), "cards!")
        print("Player B has", len(self.player_b.playing_deck.deck) + len(self.player_b.winning_deck.deck), "cards!\n")

        player_a_card = self.player_a.give_next_card()
        player_b_card = self.player_b.give_next_card()

        if player_a_card == "Loser":
            print("Player B Wins!")
            self.game_over = True
            return
        if player_b_card == "Loser":
            print("Player A Wins! Big time")
            self.game_over = True
            return

        winning_cards_list = [player_a_card, player_b_card]

        result = player_a_card.compare(player_b_card)
        if result == 1: # Player A wins
            self.player_a.collect_cards(winning_cards_list)

        if result == -1: # Player A loses
            self.player_b.collect_cards(winning_cards_list)

        if result == 0: # War
            self.war(winning_cards_list)

    def war(self, cards_list):
        self.num_wars += 1
        self.num_rounds += 1

        # Can either player run the game?
        if not self.player_a.war_valid():
            print("Player B Wins!")
            self.game_over = True
            self.winner = "Player B"
            self.player_b.move_all_cards(self.player_a)
            return
        if not self.player_b.war_valid():
            print("Player A Wins!")
            self.game_over = True
            self.winner  = "Player A"
            self.player_a.move_all_cards(self.player_b)
            return

        for i in range(2):
            cards_list.append(self.player_a.give_next_card())
            cards_list.append(self.player_b.give_next_card())

        player_a_card = self.player_a.give_next_card()
        player_b_card = self.player_b.give_next_card()

        cards_list.append(player_a_card)
        cards_list.append(player_b_card)

        result = player_a_card.compare(player_b_card)
        if result == 1:
            self.player_a.collect_cards(cards_list)
        if result == -1:
            self.player_b.collect_cards(cards_list)
        if result == 0:
            return self.war(cards_list)






