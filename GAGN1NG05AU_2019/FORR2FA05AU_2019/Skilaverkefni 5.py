# Elfar Snær Arnarson
# 08 Nóvember 2019
# Skilaverkefni 5

import math


class Sivalingur:

    def __init__(self, radius, haed):
        self.radius = radius
        self.haed = haed

    def __str__(self):
        return f"radíus: {self.radius} hæð: {self.haed}"

    def ummal(self):
        return 2 * self.radius * math.pi

    def yfirbordsflatarmal(self):
        return 2 * self.radius ** 2 * math.pi + self.haed * self.radius ** 2 * math.pi

    def rummal_sivalings(self):
        return self.radius ** 2 * math.pi * self.haed


class Foll:

    def __init__(self, x, z):
        self.x = x
        self.z = z

    def __str__(self):
        return f'x: {self.x} z: {self.z}'

    def fyrriFormula(self):
        return (4 * self.x) * 4 + (2 * self.x) ** 3

    def seinniFormula(self):
        return (self.z ** 2 + self.x ** 2) * 4 + (3 * self.x)


class Hnitakerfi:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x hnitið er {self.x} og y hnitið er {self.y}'

    def hlutiHnitakerfis(self):
        if self.x > 0:
            if self.y > 0:
                return f'hnitin eru í hluta 1'
            else:
                return f'hnitin eru í hluta 4'
        elif self.x < 0:
            if self.y > 0:
                return f'hnitin eru í hluta 2'
            else:
                return f'hnitin eru í hluta 3'
        elif self.x == 0 and self.y == 0:
            return print(f'Hnitinn eru ekki í einum hluta.')

    def stystaLeid(self):
        return round(math.sqrt(abs(self.x * 1 - self.x * 2) ** 2 + abs(self.y * 1 - self.y * 2) ** 2), 3)

#class ReikningarUtFraPunktum:


sivalingur1 = Sivalingur(1, 1)
print(sivalingur1.ummal())
print(sivalingur1.yfirbordsflatarmal())
print(sivalingur1.rummal_sivalings())
print(sivalingur1)

f1 = Foll(2, 6)
print(f1)
print(f'X = {f1.fyrriFormula()}')
print(f'Z = {f1.seinniFormula()}')

hnit = Hnitakerfi(4, -5)
print(hnit)
print(f'Stysta leiði: {hnit.stystaLeid()}')
print(hnit.hlutiHnitakerfis())


