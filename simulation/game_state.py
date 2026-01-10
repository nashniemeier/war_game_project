from player import Player

class GameState:

    def __init__(self):
        self.player_a = Player(1)
        self.player_b = Player(2)
        self.num_rounds = 0
        self.num_wars = 0


    def play_round(self):
        self.num_rounds += 1
        player_a_card = self.player_a.give_next_card()
        player_b_card = self.player_b.give_next_card()

        if player_a_card == "Loser":
            print("Player B Wins!")
            return
        if player_b_card == "Loser":
            print("Player A Wins! Big time")
            return

        winning_cards_list = [player_a_card, player_b_card]

        result = player_a_card.compare(player_b_card)
        if result == 1: # Player A wins
            self.player_a.collect_cards(winning_cards_list)

        if result == -1: # Player A loses
            self.player_b.collect_cards(winning_cards_list)

        if result == 0: # War
            self.war()

    def war(self):
        self.num_wars += 1


        # Can either player run the game?
        if not self.player_a.war_valid():
            print("Player B Wins!")
            return
        if self.player_b.war_valid():
            print("Player A Wins!")
            return

        war_cards = []

        for i in range(2):
            war_cards.append(self.player_a.give_next_card())
            war_cards.append(self.player_b.give_next_card())

        player_a_card = self.player_a.give_next_card()
        player_b_card = self.player_b.give_next_card()

        war_cards.append(player_a_card)
        war_cards.append(player_b_card)

        result = player_a_card.compare(player_b_card)
        if result == 1:
            self.player_a.collect_cards(war_cards)
        if result == -1:
            self.player_b.collect_cards(war_cards)
        if result == 0:
            return self.war()






