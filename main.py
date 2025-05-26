from game import Game
from deck import Deck
from hand import Hand
from money import Money
import sys

print('Welcome to BlackJack')
money=Money(5000)
while True:
    if money.amount <=0:
        print("It is good that you weren't playing with real money")
        print("Thanks for playing")
        sys.exit()
    print("Money: ",money.amount)
    bet = money.get_bet()
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand(dealer = True)
    for i in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    print('Bet: ',bet)
    while True:
        dealer_hand.display()
        player_hand.display()
        print()
        if player_hand.get_value() > 21:
            break
        game = Game()
        move = game.get_move(player_hand.get_value(), money.amount - bet)
        if move == 'D':
            additional_bet = money.get_bet()
            bet += additional_bet
            print(f"Bet increased to {bet}.")
            print("Bet: ", bet)
        if move in ('H','D'):
            new_card =deck.deal()
            rank = new_card.get_rank()
            suit = new_card.get_suit()
            print(f"You drew a {rank} of {suit}.")
            player_hand.add_card(new_card)
            if player_hand.get_value() > 21:
                continue
        if move == 'S':
            break
    if player_hand.get_value() <= 21:
        while dealer_hand.get_value() < 17:
            print("The dealer hits..")
            dealer_hand.add_card(deck.deal())
            dealer_hand.display()
            player_hand.display()
            if dealer_hand.get_value() > 21:
                break
            input("Press Enter to continue..")
            print('\n\n')
    dealer_hand.display(show_dealer=True)
    player_hand.display()
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    if dealer_value > 21:
        print(f"Dealer busts! You win ${bet}!")
        money.add_money(bet)
    elif player_value > 21 or player_value < dealer_value:
        print("You lost!")
        money.sub_money(bet)
    elif player_value > dealer_value:
        print("You win ${bet}!")
        money.add_money(bet)
    elif player_value == dealer_value:
        print("It is a draw and the bet is returned to you!")
        input("Press Enter to continue..")
        print('\n\n')









