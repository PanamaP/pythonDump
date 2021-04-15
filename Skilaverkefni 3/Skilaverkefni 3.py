#Elfar Snaer Arnarson
#03 feb 2020
# Skilaverkefni 3

import pickle
from Nemar import *

nemendalisti = []
# skraningnemenda = nemar.SkraningNemenda()

choice = "0"
while choice != "7":
    print("1. Opna nemaskrá")
    print("2. Skrá grunnskólanema.")
    print("3. Skrá framhaldsskólkanema.")
    print("4. Skrá Háskólanema.")
    print("5. Vista nemaskrá")
    print("6. Prenta nemendalista")
    print("7. Hætta")

    choice = str(input("Sláðu inn val: "))
    if choice == "1":
        with open('nema_listi', 'rb') as file:
            nemendalisti = pickle.load(file)
    elif choice == "2":
        grunnskolanemi = nemi.Grunnskolanemi('2905992379', 'Jón Arnar Árnason', 'kk', 'Svarthamar 26', '58712345',
                                             'jonarnar@gmail.com', 'Árni Árnason', 'Borgarskóli')
        nemendalisti.append(grunnskolanemi)
    elif choice == "3":
        framhaldsskolanemi = nemi.Framhaldsskolanemi('2815005485', 'Arnar Sigurðsson', 'kk', 'Logafold 13'
                                                , '5874584', 'arnarsig@gmail.com', 'Tölvubraut', 'Nei')
        nemendalisti.append(framhaldsskolanemi)
    elif choice == "4":
        haskolanemi = nemi.Haskolanemi('2504884828', 'Snæbjörn Fjarðarsson', 'kk', "Dúfnahóll 14"
                                  , '8485784', "snaebjorn12@gmail.com", 'PHd', 'Já')
        nemendalisti.append(haskolanemi)
    elif choice == "5":
        with open("nema_listi", 'wb') as file:
            pickle.dump(nemendalisti, file)
    elif choice == "6":
        print(nemendalisti)