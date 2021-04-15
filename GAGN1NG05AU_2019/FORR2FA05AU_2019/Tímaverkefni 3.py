# Elfar Snær Arnarson
# 19 Nóvember 2019
# Tímaverkefni 3

import random

#Búið til klasa Dice, fyrir eitt einfald tenginga kast
class Dice:

    def __init__(self):
        self.number = 0
    #fall búið til, tekur inn eina handhófskennda tölu frá eitt til sex
    def kast(self):
        self.number = random.randint(1, 6)
        return self.number

#Klasi búinn til sem 'spilar' leikinn
class Game:
    #Greini frá listum sem föllinn munu nota
    def __init__(self):
        self.computer = []
        self.player = []

    #Bý til fall sem kallar á tengina kastið úr Dice klasa
    #Kasta síðan fimm sinnum á hvern spilara og bæti hverju kasti við viðeigandi lista
    def roll(self):
        dice = Dice()
        for i in range(1, 6):  # for i in range(5)
            self.computer.append(dice.kast())
            self.player.append(dice.kast())
        #prenta síðan út köstinn með viðeigandi nöfnum við.
        return f'Tölvan: {self.computer}\nSpilarinn: {self.player}'

    #Bý til fall sem sýnir summu beggja lista
    def summa(self):
        return f'T- {sum(self.computer)} / {sum(self.player)} -S'

    #bý til fall sem kallar á tvö önnur föll, köstinn og summu útreikning
    #Prenta þau svo út fyrir þæginlegri lesleika í lokinn.
    def spiladur(self):
        print(self.roll())
        print(self.summa())

    #bý til fall sem finnur út hver sigurvegarinn er eftir köstinn.
    def sigurvegari(self):
        if sum(self.computer) > sum(self.player):
            winner = 'Ég vann'
        elif sum(self.computer) < sum(self.player):
            winner = 'Þú vannst'
        else:
            winner = 'Jafntefli'
        print(winner) # Getur líka verið return winner, print er notað í þessu tilviki fyrir betri lesleika við
        # útprentum á leiknum hér fyrir neðan.

#Leikur spiladur

#bý til breytu sem hagar sér sem klasinn Game
leikur = Game()

print('Tenginga köst:')

#Kalla á fallið spiladur() sem prentar út önnur tvö föll.
leikur.spiladur()

print()

#kalla á fallið sigurvegari() sem finnur sigurvegarann
leikur.sigurvegari()
