#Elfar Snær Arnarson
#19 október 2019
#Skilaverkefni 4 JSON

import csv
#Föll

def oddatolurListi():
    oddatolur = []
    for x in range(3000, 4002):
        oddatolur.append(x)
    return oddatolur

def skrifaISkra(listi, nafnSkra):
    with open(nafnSkra, 'w') as f:
        teljari = 0
        for x in listi:
            if x == listi[-1]:
                f.write(str(x))
            elif teljari < 4:
                f.write(str(x) + " ")
                teljari += 1
            else: #teljari > 4:
                f.write(str(x) + '\n')
                teljari = 0

def lesaSkra(nafnSkra):
    with open(nafnSkra, 'r') as f:
        listi = []
        for line in f:
            line = line.strip(" ")
            listi.append(line)
        return listi

def prenta(listi):
    teljari = 0
    for x in listi:
        if teljari < 15:
            print(str(x))
            teljari += 1
        else:  # teljari > 4:
            print(str(x) + '\n')
            teljari = 0

def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fibonacci(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst

ok = False
while ok == False:
    print("1. Oddatölur")

    val = int(input("Sláðu inn val: "))

    if val == 1:
        print(oddatolurListi())

        #skrifaISkra(oddatolurListi(), "oddatolur.txt")

        print(lesaSkra("oddatolur.txt"))

        #listi = lesaSkra("oddatolur.txt")

        #prenta(listi)


    if val == 2:

        print(fibonacci(22))

    if val == 3:
        thisdict = {
            'brand': 'Ford',
            "model": 'Mustang',
            "year"
        }