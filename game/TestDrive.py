from Card import Card
from Deck import Deck
from Player import Player
from Dealer import Dealer


def test_drive():
    deck = Deck(6)
    player = Player()
    dealer = Dealer(player)
    
    while True:

        if input("\nEnter 'q' to quit or 'h' for a new hand\n") == 'q':
            break
        
        player.reset()
        dealer.reset()
        dealer.deal()

        print("\nPlayer:")
        player.get_hand()
        print("\nDealer:")
        dealer.get_hand()

        while not dealer.player_bust:
            move = input("\nHit (h) or Stand (s)").lower()
            if move == 'h':
                dealer.player_hit()
                print("\nPlayer:")
                player.get_hand()
                if dealer.player_bust:
                    print("Player BUST")
            if move == 's':
                break
        
        if dealer.player_bust:
            continue
        dealer.player_stand()
        print("\nDealer:")
        dealer.get_hand(hide=False)
        if dealer.dealer_bust:
            print("Dealer BUST")

        outcome = dealer.check_winner()
        if outcome == -1:
            print("\nDealer Wins!\n")
        elif outcome == 0:
            print("\nIt's a Tie!\n")
        elif outcome == 1:
            print("\nPlayer Wins!\n")







    #print(player.get_card_total())



if __name__ == '__main__':
    test_drive()
