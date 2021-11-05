import random
import os

suits = (2660, 2663, 2665, 2666)
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
stand = False
count = 0
bet = ''
splitting = 'n'
doubledown = 'n'


def clear():
    os.system('cls')


class card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return (f'{self.rank}{chr(self.suit)}')


class deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class player():

    def __init__(self, ident):
        self.hand = []
        self.ident = ident
        self.chips = 1000
        self.splithand = []

    def check_bust(self):
        if self.totalvalue_func() > 21:
            return True
        else:
            return False

    def totalvalue_func(self):
        total = 0
        for i in range(len(self.hand)):
            total += self.hand[i].value
        return total

    def totalvalue_split(self):
        total = 0
        for i in range(len(self.splithand)):
            total += self.splithand[i].value
        return total

    def display_cards(self):
        for i in self.hand:
            print(i)

    def check_blackjack(self):
        if self.ident == 1:
            if len(self.hand) == 2 and self.totalvalue_func() == 21:
                return True
            else:
                return False
        else:
            if self.hand[0].rank == 'Ace' and self.hand[1].value == 10:
                return True
            else:
                return False


new_deck = deck()
new_deck.shuffle()
player1 = player(1)
dealer = player(0)

while player1.chips > 0:
    for i in range(2):
        player1.hand.append(new_deck.deal_one())
        dealer.hand.append(new_deck.deal_one())

    while True:
        try:
            bet = int(
                input(f'How many chips would you like to bet? You have {player1.chips} chips'))
        except ValueError:
            print('That is not an integer. Please try again')
            continue
        except bet > player1.chips or bet < 0:
            print(
                f'Invalid input. Please enter a number below {player1.chips}')
            continue
        else:
            break

    player1.chips -= bet
    print('Your cards:')
    player1.display_cards()
    print()

    print("Dealer's card")
    print(f'{dealer.hand[0]} ?')
    print()

    while player1.check_bust() == False and stand == False:

        print('Your cards are:')
        for i in player1.hand:
            print(i)
        print(f'The total value is {player1.totalvalue_func()}')

        if splitting == 'y':
            print('Your second hand is:')
            for i in player1.splithand:
                print(i)
        print(f'The total value is {player1.totalvalue_split()}')

        print()

        if player1.hand[0].rank == player1.hand[1].rank:
            splitting = input('Would you like to split? (Y or N)'.lower())
            while splitting != 'y' and splitting != 'n':
                splitting = input(
                    'Invalid input. Would you like to split? (Y or N)'.lower())

        if player1.totalvalue_func() == 10 or player1.totalvalue_func() == 11:
            doubledown = input(
                'Would you like to double down? (Y or N)'.lower())
            while splitting != 'y' and splitting != 'n':
                splitting = input(
                    'Invalid input. Would you like to double down? (Y or N)'.lower())

        if splitting == 'y':
            player1.splithand = player1.hand.pop(0)

        if splitting == 'n' and doubledown == 'n':
            choice = input('Hit or stand? (H or S)'.lower())
            while choice != 'h' and choice != 's':
                choice = input('Invalid input. Hit or stand? (H or S)'.lower())

        if choice == 'h':
            player1.hand.append(new_deck.deal_one())
        else:
            stand = True
        count += 1

    while dealer.totalvalue_func() < 17:
        dealer.hand.append(new_deck.deal_one())

    print("Dealer's hand")
    dealer.display_cards()
    print()

    if player1.check_bust():
        print('You lose! You busted.')

    elif dealer.check_bust():
        print('You won! Dealer has busted.')

    elif player1.check_blackjack() and not dealer.check_blackjack():
        print("You got a blackjack and the dealer didn't! You win 2.5x bet!")
        player1.chips += bet * 2.5

    elif not player1.check_blackjack() and dealer.check_blackjack():
        print("The dealer got a blackjack and you didn't! You lose!")

    elif dealer.totalvalue_func() > player1.totalvalue_func():
        print(
            f'You lose. Dealer had a total of {dealer.totalvalue_func()} and you had a total of {player1.totalvalue_func()}')

    elif dealer.totalvalue_func() < player1.totalvalue_func():
        print(
            f'You win. You had a total of {player1.totalvalue_func()} and dealer had a total of {dealer.totalvalue_func()}')
        player1.chips += bet * 2

    elif dealer.totalvalue_func() == player1.totalvalue_func():
        print(
            f'Draw. Dealer and Player both had a total of {player1.totalvalue_func()}')
        player1.chips += bet

print('You lost all your chips. Fucking idiot')
