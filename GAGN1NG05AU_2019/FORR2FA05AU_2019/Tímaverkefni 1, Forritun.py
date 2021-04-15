#Elfar Snær Arnarson
#27 september 2019
#Tímaverkefni 1
import random

def randomListi(byrjun, endir, fjoldi):
    listi = []
    for x in range(fjoldi):
        listi.append(random.randint(byrjun, endir))
    return listi

def einsTolur(listi1, listi2):
    listi3 = []
    for y in listi1:
        if y in listi2 and y not in listi3:
            listi3.append(y)
    print(f'Tölur sem báðir listar hafa: {sorted(listi3)}')

def snuaVid(strengur):
    return strengur[::-1]

def reiknaGroda(soluv, innkv, vsk):
    return soluv - (innkv + vsk)
    #agodi = soluv - (innkv + vsk)
    #return agodi

def prenta(agodi):
    if agodi < 0:
        print("Hér hefur eitthvað farið úrskeiðis.")
    elif agodi == 0:
        print("Hækkaðu álagninguna á vörunni þinni.")
    elif agodi > 0:
        print("Ágóðinn er:", str(agodi) + "Kr")


ok = False
while ok == False:
    print("1. Listi")
    print("2. Strengur")
    print("3. Föll")
    print("4. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        listiA = randomListi(50, 100, 100)
        #listiA.sort()

        listiB = randomListi(75, 200, 150)
        #listiB.sort()

        #print("Listi A -", listiA)
        print(f'Listi A: {sorted(listiA)}')
        print(f"Listi B: {sorted(listiB)}")
        einsTolur(listiA, listiB)


    if val == 2:
        strengur = input("Sláðu inn orð, setningu: ")

        textaBil = strengur.count(" ")
        lengd = len(strengur) - textaBil

        print("Stengurinn er:", lengd, "stafir.")
        print("Fjöldi orða:", (textaBil + 1))

        telja = strengur.count("b")
        teljaB = strengur.count("B")
        #print(f"það eru {strengur.upper().count("B")} b/B í setningunni
        print("Fjöldi 'b/B' er:", telja + teljaB)

        tolustafir = 0
        for x in strengur:
            if x.isnumeric():
                tolustafir += 1
        print("Tölustafir:", tolustafir)

        ofugurStrengur = snuaVid(strengur)
        print("Strengur öfugur:", ofugurStrengur)

    if val == 3:

        soluv = int(input("Sláðu inn söluverð í kr: "))
        innkv = int(input("Sláðu inn innkaupsverð í kr: "))
        vsk = int(input("Sláðu inn virðisaukaskatt í kr: "))

        agodi = reiknaGroda(soluv, innkv, vsk)
        prenta(agodi)

    if val == 4:
        break