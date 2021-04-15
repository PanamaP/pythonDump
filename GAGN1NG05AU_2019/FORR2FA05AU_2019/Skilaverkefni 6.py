#Elfar Snær Arnarson
#15 Nóvember 2019
#Skilaverkefni 6

import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def show(self):
        print(f'{self.value} of {self.suit}')

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []

    def draw(self):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()
#deck.show()

player = Player()
player.draw().draw()
player.draw()

player.showHand()


if min(player.hand[0], player.hand[1]) < player.hand[2] < max(player.hand[0], player.hand[1]):
    print("Winner!")
else:
    print("You Lose!")
