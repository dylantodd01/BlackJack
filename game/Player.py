from Card import Card

# Class to represent the player object

class Player:

    def __init__(self):
        self.reset()


    def reset(self):
        self.hand = []
        self.card_total = 0

    def get_hand(self):
        for card in self.hand:
            print(card.get_info())

    def get_card_total(self):
        total = 0
        num_aces = 0
        for card in self.hand:
            total += card.get_value()
            if card.is_ace():
                num_aces += 1
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1
        return total


