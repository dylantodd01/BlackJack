# Class to represent card objects

class Card:

    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self, colour, suit, rank):
        self.colour = colour
        self.suit = suit
        self.rank = rank


    def get_value(self):
        return Card.card_values[self.rank]

    def is_ace(self):
        return self.rank == 'A'

    def get_info(self):
        return (self.colour, self.rank, self.suit)


