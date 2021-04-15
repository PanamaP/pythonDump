#Elfar Snær Arnarson
#27 Ágúst 2019
#Strengjavinnsla

import datetime

dagsetning = datetime.date.today()
ok = False
while ok == False:
    print("1. Kennitala")
    print("2. Búa til nýtt orð")
    print("3. Sneið af streng")
    print("4. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        ok1 = False
        while ok1 == False:
            kennitala = int(input("Sláðu inn kennitölu: "))
            lengdKennitala = str(kennitala)

            fyrstuTvaer = lengdKennitala[0] + lengdKennitala[1]

            tala_3 = lengdKennitala[2]
            tala_4 = lengdKennitala[3]
            manudurRettur = tala_3 + tala_4

            faedingarAr = lengdKennitala[4] + lengdKennitala[5]
            old = lengdKennitala[-1]

            if len(lengdKennitala) == 10:
                if int(fyrstuTvaer) <= 32:
                    if int(manudurRettur) <= 12:
                        if int(old) == 0 and int(faedingarAr) <= 19 or int(old) == 9:
                            print("Vel gert þú slóst inn rétta kennitölu:", kennitala)
                            haetta = input("Sláðu inn 'q' til að komast aftur í valmynd: ")
                            if haetta == "q" or haetta == "Q":
                                break
                        else:
                            print("Reyndu aftur. ")

    if val == 2:
            stuttur = False
            ord = input("Sláðu inn fimmstafa orð: ")

            tvaerB = ord[0:2]
            tvaerLok = ord[-2] + ord[-1]

            ordSaman = tvaerB + tvaerLok
            ordStort = ordSaman.upper()
            ordLitid = ordSaman.lower()

            while stuttur == False:
                if int(len(ord)) >= 5:
                    print("Nýji strengurinn er:", ordSaman)
                    print("Nýji strengurinn í upphafstöfum:", ordStort)
                    print("Nýji strengurinn í lágstöfum:", ordLitid)
                    stuttur = True
                elif int(len(ord)) <= 5:
                    ord = input("Sláðu inn fimmstafa orð: ")

    if val == 3:
        nafn = input("Sláðu inn nafn: ")
        for stafur in range(len(nafn)):
            print(nafn[stafur:len(nafn)])

    if val == 4:
        break





