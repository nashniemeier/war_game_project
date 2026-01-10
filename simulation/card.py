# A card needs a rank and a function to compare itself to another card
# Rank will be an integer

class Card:

    def __init__(self, rank):
        self.rank = rank

    def show(self):
        print(self.rank)

    def compare(self, other):
        if self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        else: # Go to a war
            return 0 # CHANGE LATER