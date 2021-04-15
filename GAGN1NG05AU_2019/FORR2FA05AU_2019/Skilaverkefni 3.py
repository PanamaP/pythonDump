#Elfar Snær Arnarson
#13 október 2019
#Skilaverkefni 3

import random

#Bý til fall sem sýnir sitthvort tuplið
def prentaTuple(fyrsti,seinni):
    print('Fyrri listinn: ')
    teljari = 0
    for x in fyrsti:
        if teljari != 5:
            print(x, end=', ')
            teljari += 1
        else:
            print(x)
            teljari = 0

    print('Seinni listinn: ')
    for y in seinni:
        if teljari != 5:
            print(y, end=', ')
            teljari += 1
        else:
            print(y)
            teljari = 0
    print('-----------------')
#Bý til fall sem para tuplunum saman
def paraRod(tup1, tup2):
    for x in range(6):
        print(tup1[x], "og", tup2[x])
    print("------------------")
#Bý til fall sem parar random pari saman, það má laga þetta
def paraRandom(tup1, tup2):
    for x in range(6):
        print(tup1[random.randint(0,5)], 'og', tup2[random.randint(0, 5)])
#Bý til fall sem tekur inn nafn og finnur viðeigandi númer í skránni
def simaskrainn():
    nafn = input("Sláðu inn nafn: ")

    for key in simaskra.keys():
        if nafn == key:
            print("Símanúmer hjá", nafn, 'er', simaskra[key])
#Bý til fall sem prentar út all nemendur með aldri. Mætti fín pússa útprentið
def prentaNemendur(nemendur):
    for key in nemendur.keys():
        print(" ", key, "--", nemendur[key])
#Bý til fall sem finnur hvaða nemendur eru átján ára eða eldri og prenta út nafn og aldur
# Mætti fín pússa útprentið
def prentaNofn(nemendur):
    print('Nemendur orðnir 18:')
    for key in nemendur.keys():
        if nemendur[key] >= 18:
            print(" ", key, "--", nemendur[key])
#Bý til fall sem reiknar út meðaldur bekkjarins
def medalaldur(nemendur):
    summa = 0
    for values in nemendur.values():
        summa += values
    medaltal = summa / len(nemendur)
    print('Meðalaldur bekksins:', round(medaltal, 2), 'ár')

#bý til while breytu sem heldur utan um valmyndina
ok = False
while ok == False:
    print("1. Danspörin")
    print("2. Símaskrá")
    print("3. Skráning í bekk")

    val = int(input("Sláðu inn val: "))
    #Bý til if setningu sem tekur á moti innsetningu á valmynd
    if val == 1:
        #Bý til tvo tuples sem geyma dansherra og dansdömur
        dansherra = ('Konráð', 'Snorri', 'Ásgeir', 'Elmar', 'Matti', 'Steini')
        dansdomur = ('Rósa', 'Sigríður', 'Laufey', 'Erla', 'Ásdís', 'Sigrún')

        #Kalla framm fyrsta fallið
        prentaTuple(dansherra, dansdomur)

        #Kalla framm seinna fallið
        paraRod(dansherra, dansdomur)

        #Kalla framm þriðja fallið
        paraRandom(dansherra, dansdomur)

    if val == 2:
        print('Símaskráinn:')
        #Bý til dictonary sem inniheldur 10 nofn og numer
        simaskra = {'Elfar Snær': "8681147", 'Laufey Erla': "5784515", 'Gabriel Arnar': "5684975",
                    'Matti': '8652548', 'Sindri': '7584586', 'Alex': '6584585', 'Mikki': '8651458',
                    'Robert': '7586524', 'Arnar': '5689568', 'Bragi': '4587586'}
        teljari = 1
        lengdin = len(simaskra)
        for x in simaskra:
            if teljari != lengdin:
                print(x, end=", ")
                teljari += 1
            else:
                print(x)
                teljari = 1
        #Kalla framm Símaskrá fallið
        simaskrainn()


    if val == 3:
        #Bý til dict fyrir nemendur
        nemendur = {'Elfar': 20, 'Jakob': 19, 'Kacper': 18, 'Matti': 20, 'Alex': 23, 'Arnar': 19,
                    'Sindri': 17, 'Bragi': 21, 'Heimir': 24, 'Axel': 18, 'Steinar': 21,
                    'Mælgin': 18, 'Valgeir': 22, 'Sigrún': 21, 'Móglí': 20}
        #Kalla framm fyrsta fallið, mætti bæta útprentun
        prentaNemendur(nemendur)

        #Kalla framm fallið, mætti bæta útprentun
        prentaNofn(nemendur)

        #Kalla framm fallið
        medalaldur(nemendur)