import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 10}


class card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


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

    def __init__(self):
        self.hand = []

    def bet(chips):
        pass

    def check_bust(self):
        total = 0
        for i in range(len(self.hand)):
            total += player.hand[i].value
        if total > 21:
            return True
        else:
            return False

new_deck = deck()
new_deck.shuffle()
player = player()
dealer = player()
for card in new_deck.all_cards:
    print(card)

while True:

    for i in range(2):
        player.hand.append(deck.deal_one())
        dealer.hand.append(deck.deal_one())

    print('Your cards are:')
    for i in range(len(player.hand)):
        print(card)
    print(f'The total value is {player.hand[0].value + player.hand[0].value}')

    print()
    choice = input('Hit or stand? (H or S)'.lower())
    while choice != 'h' and choice != 's':
        choice = input('Invalid input. Hit or stand? (H or S)'.lower())
    
    if choice == 'h':
        player.hand.append(deck.deal_one())
    if dealer.hand[0].value + dealer.hand[1].value < 17:
        
