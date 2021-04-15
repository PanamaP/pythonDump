#Elfar Snær Arnarson
#30 Ágúst 2019
#Skilaverkefni 1
import random
import time


ok = False
while ok == False:
    print("1. Verkefni 1")
    print("2. Verkefni 2")
    print("3. Verkefni 3")
    print("4. Verkefni 4")
    print("5. Verkefni 5")
    print("6. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        talanlisti = []
        sum = 0
        for x in range(7):
            tolur = int(input("Sláðu inn tölu: "))
            sum += tolur
            talanlisti.append(tolur)

        talanlisti.sort(reverse=True)
        #Stærsta talan
        print("Stærsta talan er:",max(talanlisti))
        #minnsta talan
        print("Minnsta talan er:",min(talanlisti))
        #Summa
        print("Summan er:",sum)
        #Medaltal
        medaltal = sum / 7
        print("Medaltalid er:", round(medaltal,2))

        #Listi sýndur með for lykkju
        yfirFimm = 0
        #Má laga
        teljarinn = 0
        print("Listinn er:")
        for l in talanlisti:
            if teljarinn < 6:
                print(l, end="-")
                teljarinn += 1
            else:
                print(l, end=" ")
            if l >= 50.5:
                yfirFimm += 1
        print()
        print("Tölur jafnt eða yfir 50.5 -",yfirFimm)

    elif val == 2:
        listi = []
        teljari = 0
        for x in range(70):
            teljari += 1
            f = (random.randint(1, 1500))
            listi.append(f)
            print(f, end=(" | " if teljari < 4 else "\n"))
            if teljari == 4:
                teljari = 0
        print()
        print("Stærsta talan er:",max(listi))
        print("Minnsta talan er:", min(listi))
        time.sleep(2)
        print("Öfugur listi:")
        time.sleep(1)
        print('2..')
        time.sleep(1)
        print("1..")
        time.sleep(1)
        ofugtlisti = sorted(listi, reverse=True)
        teljari = 0
        for y in ofugtlisti:
            teljari += 1
            print(y, end=(" | " if teljari < 6 else "\n"))
            if teljari == 6:
                teljari = 0
        print()

        tvofimm = 0
        fimmhun = 0
        for x in listi:
            if x >= 1 and x <= 250:
                tvofimm +=1
            if x >= 251 and x <= 500:
                fimmhun += 1
        print("Tölur á bilinu 1-250 eru:",tvofimm)
        print("Tölur á bilinu 251-500 eru:",fimmhun)
        time.sleep(2)



    elif val == 3:
        nafnalisti = []
        for x in range(5):
            nafn = input("Sláðu inn nafn: ")
            nafnalisti.append(nafn)

        ok1 = False
        while ok1 == False:
            print("1. Birta nöfnin óröðuð.")
            print("2. Raða nöfnum í stafrófsröð og birta.")
            print("3. Raða nöfnum í öfuga stafrófsröð og birta.")
            print("4. Birta eitt nafn í einu.")
            print("5. Hætta í verkefni 3.")
            val_3 = int(input("Sláðu inn val: "))

            if val_3 == 1:
                print(nafnalisti)

            if val_3 == 2:
                nyrNafnalisti = sorted(nafnalisti)
                print(nyrNafnalisti)

            if val_3 == 3:
                ofugtNafnalisti = sorted(nafnalisti, reverse=True)
                print(ofugtNafnalisti)

            if val_3 == 4:
                for x in range(5):
                    print(nafnalisti[x])

            if val_3 == 5:
                break

    elif val == 4:
        teningur = int(input("Hver oft viltu kasta teningnum? :"))

        telja = []
        for x in range(teningur):
            kast = random.randint(1, 6)
            telja.append(kast)
            print('Kast:', kast)

        tala1 = telja.count(1)
        tala2 = telja.count(2)
        tala3 = telja.count(3)
        tala4 = telja.count(4)
        tala5 = telja.count(5)
        tala6 = telja.count(6)

        print("Tala 1 kom upp:", tala1,'sinnum')
        print("Tala 2 kom upp:", tala2, 'sinnum')
        print("Tala 3 kom upp:", tala3, 'sinnum')
        print("Tala 4 kom upp:", tala4, 'sinnum')
        print("Tala 5 kom upp:", tala5, 'sinnum')
        print("Tala 6 kom upp:", tala6, 'sinnum')

        if tala1 > tala2 and tala1 > tala3 and tala1 > tala4 and tala1 > tala5 and tala1 > tala6:
            print("Tala 1 kemur oftast upp")
        elif tala2 > tala1 and tala2 > tala3 and tala2 > tala4 and tala2 > tala5 and tala2 > tala6:
            print("Tala 2 kemur oftast upp")
        elif tala3 > tala2 and tala3 > tala1 and tala3 > tala4 and tala3 > tala5 and tala3 > tala6:
            print("Tala 3 kemur oftast upp")
        elif tala4 > tala2 and tala4 > tala3 and tala4 > tala1 and tala4 > tala5 and tala4 > tala6:
            print("Tala 4 kemur oftast upp")
        elif tala5 > tala2 and tala5 > tala3 and tala5 > tala4 and tala5 > tala1 and tala5 > tala6:
            print("Tala 5 kemur oftast upp")
        elif tala6 > tala2 and tala6 > tala3 and tala6 > tala4 and tala6 > tala5 and tala6 > tala1:
            print("Tala 6 kemur oftast upp")
        else:
            print("Enginn ein tala kom oftast")


        if tala1 < tala2 and tala1 < tala3 and tala1 < tala4 and tala1 < tala5 and tala1 < tala6:
            print("Tala 1 kemur sjaldnast")
        elif tala2 < tala1 and tala2 < tala3 and tala2 < tala4 and tala2 < tala5 and tala2 < tala6:
            print("Tala 2 kemur sjaldnast")
        elif tala3 < tala2 and tala3 < tala1 and tala3 < tala4 and tala3 < tala5 and tala3 < tala6:
            print("Tala 3 kemur sjaldnast")
        elif tala4 < tala2 and tala4 < tala3 and tala4 < tala1 and tala4 < tala5 and tala4 < tala6:
            print("Tala 4 kemur sjaldnast")
        elif tala5 < tala2 and tala5 < tala3 and tala5 < tala4 and tala5 < tala5 and tala5 < tala6:
            print("Tala 5 kemur sjaldnast")
        elif tala6 < tala2 and tala6 < tala3 and tala6 < tala4 and tala6 < tala5 and tala6 < tala1:
            print("Tala 6 kemur sjaldnast")
        else:
            print("Engin ein tala kom sjaldnast")

    elif val == 5:
        fjoldi = int(input("Hversu margir eru í FOR1TÖ05BU? :"))
        hopur = []
        for x in range(fjoldi):
            nofn = input("Hvað heita þau: ")
            hopur.append(nofn)

        stafrosrodHopur = sorted(hopur)
        print("Nöfn í stafrófsröð:")
        for nofnin in stafrosrodHopur:
            print(nofnin)
        input("Ýttu á enter til að fara til baka...")


    elif val == 6:
        break




