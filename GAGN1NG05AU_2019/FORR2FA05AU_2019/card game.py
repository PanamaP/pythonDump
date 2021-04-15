from random import randint


class card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return f'{self.suit} {self.value}'

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def show(self):
        return f'{self.value} of {self.suit}'
    
class deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['spades', 'clubs', 'Diamonds', 'Hearts']:
            for v in range(1, 14):
                self.cards.append(card(s, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            print(card.show)


class player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print(f"Hi my name is {self.name}")

    def draw(self, deck, num=1):
        for i in range(num):
            card = deck.drawCard()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def showHand(self):
        for card in self.hand:
            print(card.show())
