import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r))

    def shuffledeck(self):
        random.shuffle(self.deck)

    def dealcard(self):
        return self.deck.pop()

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f'Player{self.name} has {len(self.all_cards)} cards.'

    def remove_one (self):
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

player_one = Player("One")
player_two = Player("Two")
newdeck = Deck()
newdeck.shuffledeck()
for x in range(26):
    player_one.add_card(newdeck.dealcard())
    player_two.add_card(newdeck.dealcard())

gamewin = False
round_num = 0
atwar = False

while gamewin == False:
    round_num += 1
    print(f'Round {round_num}')
    if len(player_one.all_cards) == 0:
        print('Player One, you lost! Player two you win!')
        gamewin = True
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, you lost! Player One you win!')
        gamewin = True
        break
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    p2value = 0
    p1value = 0
    if player_one_cards[-1].value == player_two_cards[-1].value:
        if len(player_two.all_cards) < 5:
            print('player two loses not enough cards for war!')
            gamewin = True
        elif len(player_one.all_cards) < 5:
            print('player one loses not enough cards for war!')
            gamewin = True
        else:
            atwar = True
        print('You are at war!')
    elif player_one_cards[-1].value > player_two_cards[-1].value:
        player_one.add_card(player_two_cards)
        player_one.add_card(player_one_cards)
        print("player 1 wins")
    else:
        player_two.add_card(player_two_cards)
        player_two.add_card(player_one_cards)
        print("player 2 wins")
    while atwar == True:
        for x in range(5):
            player_two_cards.append(player_two.remove_one())
            player_one_cards.append(player_one.remove_one())
        for x in range(6):
            p2value += player_two_cards[x].value
        for x in range(6):
            p1value += player_two_cards[x].value
        if p1value == p2value:
            if len(player_two.all_cards) < 5:
                print('player two loses not enough cards for war!')
                gamewin = True
                break
            elif len(player_one.all_cards) < 5:
                print('player one loses not enough cards for war!')
                gamewin = True
                break
            else:
                atwar = True
            print('You are still at war!')
        elif p1value > p2value:
            player_one.add_card(player_two_cards)
            player_one.add_card(player_one_cards)
            print("player 1 wins")
            atwar = False
        else:
            player_two.add_card(player_two_cards)
            player_two.add_card(player_one_cards)
            print("player 2 wins")
            atwar = False


