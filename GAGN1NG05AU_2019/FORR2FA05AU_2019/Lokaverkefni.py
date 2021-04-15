# Elfar Snær Arnarson
# 26 Nóvember 2019
# Lokaverkefni Blackjack

from random import randint


class Card:
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
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value
        return f"{val} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # Return the top card
    def drawCard(self):
        return self.cards.pop()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print(f"Hi! Welcome {self.name}!")
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for i in range(num):
            card = deck.drawCard()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def totalhand(self):
        total = 0
        for c in self.hand:
            total += c.value
        return total

    # Display all the cards in the players hand
    def showhand(self):
        list = []
        for card in self.hand:
            list.append(card.show())
        return list


# main

name = input("What's your name? ")
player = Player(name)
computer = Player('Computer')

playLoopStop = False
winsPlayer = 0
winsComputer = 0

# Menu
ok = False
player.sayHello()
while not ok:
    print("1. Play Blackjack")
    print("2. Quit")
    val = int(input("Put in your choice:"))
    if val == 1:
        player.hand.clear()
        computer.hand.clear()
        playLoopStop = False

        mydeck = Deck()
        mydeck.shuffle()
        player.draw(mydeck, 2)
        computer.draw(mydeck, 2)

        print(f'Computer Hand: {computer.showhand()} with a total value of {computer.totalhand()}')
        print(f"{name}'s Hand: {player.showhand()} with a total value of {player.totalhand()}")
        if player.totalhand() > 21:
            print(f"Oh no! {name} Busted!")
            winsComputer += 1
            playLoopStop = True
        elif computer.totalhand() > 21:
            print("The Computer is Busted!")
            winsPlayer += 1
            playLoopStop = True
        elif computer.totalhand() == 21 and player.totalhand() == 21:
            print("It's a Tie!")
            playLoopStop = True

        while playLoopStop == False:
            hitorstand = input("Hit or Stand/Done (h or s): ")
            if hitorstand == 'H' or hitorstand == 'h':
                player.draw(mydeck)
                if player.totalhand() < 21:
                    print(f"{name}'s has these cards {player.showhand()} with a total value of {player.totalhand()}")
                elif player.totalhand() == 21:
                    print(f"{name}'s has these card {player.showhand()} with a total value of {player.totalhand()}")
                    print(f"Blackjack! {name} wins!")
                    winsPlayer += 1
                    playLoopStop = True
                else:
                    print(f"Oh no! {name} busted. Total value of {player.totalhand()}")
                    winsComputer += 1
                    playLoopStop = True
            if hitorstand == "S" or hitorstand == "s":
                print(f"{name} stands on {player.totalhand()}. Dealers Turn.")
                if computer.totalhand() > 21:
                    winsPlayer += 1
                    print(f"The computer is busted!")
                    print(f"{name} wins!")
                    playLoopStop = True
                elif player.totalhand() == computer.totalhand():
                    print("It's a tie!")
                    break
                elif computer.totalhand() > 18 and computer.totalhand() > player.totalhand():
                    if computer.totalhand() > player.totalhand():
                        print("Computer wins!")
                        winsComputer += 1
                        break

                    elif player.totalhand() > computer.totalhand():
                        print(f"{name} wins!")
                        winsPlayer += 1
                        break

                    elif player.totalhand() == computer.totalhand():
                        print("It's a tie!")
                        break

                elif computer.totalhand() <= 18:
                    if computer.totalhand() > player.totalhand():
                        print(f"The computer has: {computer.showhand()} with a total value of {computer.totalhand()}")
                        print("Computer wins!")
                        winsComputer += 1
                        break

                    while computer.totalhand() <= 18 and computer.totalhand() < player.totalhand():
                        computer.draw(mydeck)
                    print(f"The computer has: {computer.showhand()} with a total value of {computer.totalhand()}")

                    if computer.totalhand() > 21:
                        winsPlayer += 1
                        print(f"The computer is busted!")
                        print(f"{name} wins!")
                        playLoopStop = True
                    elif computer.totalhand() > player.totalhand():
                        print("Computer wins!")
                        winsComputer += 1
                        break

                    elif player.totalhand() > computer.totalhand():
                        print(f"{name} wins!")
                        winsPlayer += 1
                        break

                    elif player.totalhand() == computer.totalhand():
                        print("It's a tie!")
                        break

    if val == 2:
        break

    print(f"Wins, {name} = {winsPlayer}  computer = {winsComputer}")
