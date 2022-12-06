from Card import Card
import random

# Class to represent the deck object

class Deck:

    colours = ["Red", "Black"]
    suits = ["Spade", "Club", "Heart", "Diamond"]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


    def __init__(self, num_decks=6):
        self.deck = self.create_deck(num_decks) 

    def draw_card(self):
        return self.deck.pop()
    
    def get_deck(self):
        return self.deck

    def create_deck(self, num_decks):
        deck = []
        for i in range(num_decks):
            for colour in Deck.colours:
                for suit in Deck.suits:
                    for rank in Deck.ranks:
                        deck.append(Card(colour, suit, rank))
        random.shuffle(deck)
        return deck

