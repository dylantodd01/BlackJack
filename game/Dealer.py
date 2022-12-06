from Player import Player
from Deck import Deck


# Class to represent dealer object

class Dealer(Player):

    def __init__(self, player):
        self.reset()
        self.deck = Deck(6)
        self.player = player

    
    def reset(self):
        super().reset()
        self.player_bust = False
        self.dealer_bust = False

    def get_hand(self, hide=True):
        if len(self.hand) <= 2 and hide:
            print(self.hand[0].get_info())
            print('(****, **, *****)')
            return
        super().get_hand()

    def deal(self):
        for i in range(2):
            self.player.hand.append(self.deck.draw_card())
            self.hand.append(self.deck.draw_card())

    def player_hit(self):
        if not self.player_bust:
            self.player.hand.append(self.deck.draw_card())
            self.check_player_bust()

    def player_stand(self):
        self.play()

    def check_player_bust(self):
        if self.player.get_card_total() > 21:
            self.player_bust = True

    def play(self):
        if self.player_bust: return
        while self.get_card_total() < 17:
            self.hand.append(self.deck.draw_card())
        if self.get_card_total() > 21:
            self.dealer_bust = True

    def check_winner(self):
        # Returns -1 for a dealer win, 0 for a draw and 1 for a player win 
        self.check_player_bust()
        if self.player_bust or self.player.get_card_total() < self.get_card_total():
            return -1
        elif self.dealer_bust or self.player.get_card_total() > self.get_card_total():
            return 1
        else:
            return 0


