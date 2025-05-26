import sys


class Money:
    def __init__(self, amount):
        self.amount = amount

    def add_money(self, amount):
        self.amount += amount

    def sub_money(self, amount):
        self.amount -= amount

    def get_bet(self):
        while True:
            try:
                bet = input("How much do you bet? (1-5000 or QUIT): ")
                if bet.lower() == "quit":
                    print("Thanks for playing!")
                    sys.exit()
                bet = int(bet)
                if 1 <= bet <= min(5000, self.amount):
                    return bet
                else:
                    print(f"Invalid bet amount. Please enter a number between 1 and {min(5000, self.amount)}.")
            except ValueError:
                print("Invalid input. Please enter a number or type 'QUIT'.")
