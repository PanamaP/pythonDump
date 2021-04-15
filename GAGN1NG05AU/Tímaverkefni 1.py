# Elfar Snær Arnarson
# 5 febrúar 2019
# Tímaverkefni 1

import random

ok = False
while ok == False:
    print("1. Listi")
    print("2. Strengur")
    print("3. Föll")
    print("4. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        listi = []
        listi1 = []
        listi2 = []
        talan112 = 0
        for i in range(400):
            tala = random.randint(100, 150)
            listi1.append(tala)
            if tala == 125:
                print()
            else:
                listi.append(tala)
            if tala == 134:
                listi2.append(25)
            else:
                listi2.append(tala)
            if tala == 112:
                talan112 += 1

        fyrstiListi = ";".join(map(str, listi1))
        print("Uprunnilegi listinn:", fyrstiListi)
        minnListi = ";".join(map(str, listi))
        print("Eytt 125 listinn:", minnListi)
        annarListi = ";".join(map(str, listi2))
        print("134 breytt í 25 listinn:", annarListi)
        print("Meðaltal seinasta listans er:", sum(listi2) / float(len(listi2)))
        print("Talan 112 kemur fyrir:", talan112, "sinnum")

    if val == 2:
        listi = []
        strengur = input("Sláðu inn orð, setningu: ")

        textaBil = strengur.count(" ")
        lengd = len(strengur) - textaBil

        print("Stengurinn er:", lengd, "stafir.")
        print("Fjöldi orða:", (textaBil + 1))

        telja = strengur.count("k")
        print("Fjöldi 'k' er:", telja)

        tolustafir = 0
        for x in strengur:
            if x.isnumeric():
                tolustafir += 1
        print("Tölustafir:", tolustafir)

    if val == 3:
        nafn = input("Sláðu inn nafn: ")
        aldur = int(input("Sláðu inn aldur: "))
        haed = int(input("Sláðu inn hæð í sentimetrum: "))


        def hundrad():
            ar = 100 - aldur
            if 100 - aldur > 0:
                print("Það eru", ar, "ár í að þú verðir 100 ára", nafn)
            else:
                print("Þú hefur náð hundrað ára!")

        def haedin():
            if haed < 150:
                print("Ekki hár í loftinu")
            elif haed > 150 and haed < 185:
                print("Já, það er bara svona.")
            else:
                print("þokkalega hávaxinn")


        hundrad()
        haedin()
